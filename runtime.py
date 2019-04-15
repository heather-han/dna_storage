# runtime.py
# This takes in the runtime output files from runtime.sh and calculates
# the total pipeline runtime for each file

import matplotlib.pyplot as plt


def main():
	# take in file sizes, generated by ' ls -l data/' > file_sizes
	file_sizes = {}
	ignore = ['.dna', '.zip', '.gz', '.7z', '.recovered']
	with open('file_sizes', 'r') as f:
		total_size = f.readline()

		for line in f:
			line = line.strip().split()
			filename = line[-1]
			if any(ending in filename for ending in ignore):
				continue
			file_sizes[filename] = line[4]

	#
	files = ['runtime', 'runtime_zip', 'runtime_gzip', 'runtime_7zip']
	total_runtimes = {}
	for file in files:
		total_runtime = calc_runtime(file, file_sizes)
		total_runtimes[file] = total_runtime
		# print('\n', file)
		# print(total_runtime)
	plot(total_runtimes)


def calc_runtime(runtime_f, file_sizes):
	total_runtimes = {}

	with open(runtime_f, 'r') as f:
		# determine if a zip method was used or not
		line = f.readline()
		zipped = 'Zip' in line
		file_start = 'Zip' if zipped else 'Encode'
		filename = line.strip().split()[1][:-1].split('/')[1]
		file_size = file_sizes[filename]

		runtime = 0
		for line in f:
			line = line.strip().split()
			# initialize variables for the new file
			if file_start in line:
				total_runtimes[file_size] = runtime
				runtime = 0
				filename = line[1][:-1].split('/')[1]
				file_size = file_sizes[filename]
			# ignore 
			elif 'Encode' in line or 'Decode' in line:
				continue
			# add to runtime
			else:
				time = float(line[1].split('m')[1][:-1])
				runtime += time

	# add last file and print results
	total_runtimes[file_size] = runtime
	return total_runtimes


def plot(total_runtimes):
	plt.figure()
	for file, runtimes in total_runtimes.items():
		runtimes_sorted = sorted(runtimes.items(), key=lambda kv: kv[1])
		sizes = [i[0] for i in runtimes_sorted]
		times = [i[1] for i in runtimes_sorted]
		plt.plot(sizes, times, label=file)
	plt.title('Runtimes for Various File Sizes')
	plt.xlabel('File Sizes (bytes)')
	plt.ylabel('Runtimes (seconds)')
	plt.legend()
	plt.savefig('runtimes.png')
	plt.show()


if __name__ == '__main__':
	main()