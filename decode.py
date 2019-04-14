import os
import struct


def main(path):
	name_list = []
	file_list = []
	# walk through the folder, pick out the .dna file
	for fpathe, dirs, i in os.walk(path):
		for ff in i:
			a = ff.split('.')
			if a[-1] == 'dna':
				name_list.append(a[0])
				file_list.append(os.path.join(fpathe, ff))
			else:
				continue
	for file in file_list:
		fn_in = file
		fn_bits = fn_in.split('.')[0] + '2.' + fn_in.split('.')[1]
		fn_recovered = fn_in.split('.')[0] + '.' + fn_in.split('.')[1] + '.recovered'

		# encoding to use for converting bits to genomic sequence
		encoding = {b'00': 'A', b'01': 'C', b'10': 'G', b'11': 'T'}
		reverse_encoding = {val: key for (key, val) in encoding.items()}

		# read in file, convert from dna to bits
		with open(fn_in, 'r') as f_in:
			dna = f_in.read()
			# convert input file data into bits and write to file
			with open(fn_bits, 'wb') as f_out:
				bits = decode(dna, reverse_encoding)
				f_out.write(bits)

			# # convert bits into original data and write to file
			# with open(fn_recovered, 'w') as f_out:
			# 	data = convert_from_bits(bits)
			# 	f_out.write(data)


def decode(dna, reverse_encoding):
	""" Decode DNA sequence into bits """
	bits = b""
	for base in dna:
		bits += reverse_encoding[base]
	return bits


def convert_from_bits(bits):
	""" Convert from bits to original file content """
	pass

if __name__ == '__main__':
	main('convert')