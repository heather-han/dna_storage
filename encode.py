import sys
import binascii
import numpy as np
from tqdm import tqdm


def main():
	fn_in = sys.argv[1]
	fn_out = fn_in.split('.')[0] + '.dna'

	# encoding to use for converting bits to genomic sequence
	encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
	reverse_encoding = {val: key for (key, val) in encoding.items()}

	# read in file, convert to bits, and encode to dna
	with open(fn_in, 'r') as f_in:
		s = f_in.read()	
		print('converting to bits...')
		bits = convert_to_bits(s)
		print('encoding...')
		dna = encode(bits, encoding)
		with open(fn_out, 'w') as f_out:
			f_out.write(dna)


def convert_to_bits(fn_in):
	""" Convert input data into bits """
	result = []
	for c in fn_in:
		bits = bin(ord(c))[2:]
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
	main()