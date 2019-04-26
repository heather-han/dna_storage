# runtime.py
# This takes in the runtime output files from runtime.sh and calculates
# the total pipeline runtime for each file

import glob
import pandas as pd
import matplotlib.pyplot as plt


def main():
	# get total file sizes
	original_file_sizes = get_file_sizes('results/original_file_sizes')

	# ===== RUNTIMES =====
	# get runtimes for each compression method
	runtime_files = set(glob.glob("results/runtime*")) - set(glob.glob("results/runtime*.png"))
	all_runtimes = {}; 
	for runtime_file in runtime_files:
		# get runtime for each file
		method = runtime_file.split('/')[1].split('_')
		method = method[1] if len(method) > 1 else 'no_comp'
		total_runtime = get_runtimes(runtime_file)
		all_runtimes[method] = total_runtime

	# create dataframe with filename, orig file size, and compression ratio
	df_runtime = pd.DataFrame.from_dict(all_runtimes)
	df_runtime['size'] = df_runtime.index.map(original_file_sizes)
	plot_runtimes(df_runtime)

	# ===== COMPRESSION RATIOS =====
	# get compressed file sizes for each compression method
	file_sizes_files = glob.glob("results/file_sizes*")
	all_ratios = {}
	for file_size_file in file_sizes_files:
		# get compression ratio for each file
		method = file_size_file.split('/')[1].split('_')[-1]
		# method = method[-1] if method[-1] != 'sizes' else 'no_comp'
		compression_ratios = get_comp_ratio(file_size_file, original_file_sizes)
		all_ratios[method] = compression_ratios

	df_ratio = pd.DataFrame.from_dict(all_ratios)
	plot_ratios(df_ratio, df_runtime)


def get_file_sizes(orig_file_sizes_f):
	""" Extract all file sizes from the given file """
	file_sizes = {}
	with open(orig_file_sizes_f, 'r') as f:
		for line in f:
			line = line.strip().split()
			filename = line[-1].split('/')[1].split('.')[0]
			# get file size and convert to byte
			file_size = float(line[4])/1000.0
			file_sizes[filename] = file_size 
	return file_sizes


def get_runtimes(runtime_f):
	""" extract total runtimes for each file """
	total_runtimes = {}

	with open(runtime_f, 'r') as f:
		# determine if a zip method was used or not
		line = f.readline()
		file_start = 'Zip' if 'Zip' in line else 'Encode'

		# get file name and original file size
		filename = line.strip().split()[1][:-1].split('/')[1].split('.')[0]

		# get runtimes for each file
		runtime = 0
		for line in f:
			line = line.strip().split()
			# initialize variables for the new file
			if file_start in line:
				total_runtimes[filename] = runtime
				runtime = 0
				filename = line[1][:-1].split('/')[1].split('.')[0]
			# get runtime 
			elif 'real' in line:
				time = float(line[1].split('m')[1][:-1])
				runtime += time

	# add last file and print results
	total_runtimes[filename] = runtime
	return total_runtimes


def get_comp_ratio(sizes_f, original_file_sizes):
	""" extract and calculate compression ratios for each file """
	comp_ratios = {}
	file_sizes = get_file_sizes(sizes_f)
	for (key, value) in file_sizes.items():
		comp_ratio = value/original_file_sizes[key]
		comp_ratios[key] = comp_ratio
	return comp_ratios


def plot_runtimes(df_runtime):
	df_runtime = df_runtime.sort_values('size').set_index('size')
	df_runtime.plot()
	plt.title('Runtimes for Various Input File Sizes')
	plt.xlabel('File Sizes (Kbs)')
	plt.ylabel('Runtime (seconds)')
	plt.legend(loc='best')
	plt.savefig('results/runtimes.png')
	plt.show()


def plot_ratios(df_ratio, df_runtime):
	cols = df_ratio.columns
	plt.figure()
	for col in cols:
		plt.scatter(df_ratio[col], df_runtime[col], label=col)
	plt.title('Runtimes vs. Compression Ratios')
	plt.xlabel('Compression ratios')
	plt.ylabel('Runtime (seconds)')
	plt.legend(loc='best')
	plt.savefig('results/ratios.png')
	plt.show()


if __name__ == '__main__':
	main()