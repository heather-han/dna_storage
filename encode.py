# encode.py
# Encodes a given input file, and outputs a DNA sequence
#
# usage: python encode.py <input_file_path>


import sys
import os

def main(path, file_type):
	name_list = []
	file_list = []
	for fpathe, dirs, i in os.walk(path):
		for ff in i:
			a = ff.split('.')
			if a[1] == file_type:
				name_list.append(a[0])
				file_list.append(os.path.join(fpathe, ff))
			else:
				continue
	for files in file_list:
		fn_in = files
		fn_out = fn_in.split('.')[0] + '.dna'

		# encoding to use for converting bits to genomic sequence
		encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
		reverse_encoding = {val: key for (key, val) in encoding.items()}

		# read in file, convert to bits, and encode to dna
		with open(fn_in, 'rb') as f_in:
			data = f_in.read()
			print('converting to bits...')
			bits = convert_to_bits(data)
			print('encoding...')
			dna = encode(bits, encoding)
			with open(fn_out, 'w') as f_out:
				f_out.write(dna)


def convert_to_bits(data):
	""" Convert input data into bits """
	result = []
	for c in data:
		bits = bin(c)[2:]
		bits = '00000000'[len(bits):] + bits
		result.extend(bits)
		# result.extend([int(b) for b in bits])
	return ''.join([i for i in result])


def encode(bits, encoding):
	""" Encode bits into DNA sequence """
	dna = ""
	length = len(bits) - len(bits)%2
	for i in range(0, length, 2):
		dna += encoding[bits[i:i+2]]
	return str(dna)
	

if __name__ == '__main__':
	main('convert', 'png')
	# print(sys.argv[1])