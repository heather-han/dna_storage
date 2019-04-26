# decode.py
# Decodes a given input file, and outputs a decoded file in bits, as well 
# as the orginal recovered file
#
# usage: python decode.py <input_file_path> <error_rate>


import sys
import copy
import random
from tqdm import tqdm


def main():
	fn = sys.argv[1].split('.')
	fn_dna = fn[0] + '.dna'
	fn_recovered = fn[0] + '_recovered.' + fn[1]
	print(fn, fn_recovered)

	# var to specify how much error to introduce
	error_rate = float(sys.argv[2])

	# encoding to use for converting bits to genomic sequence
	encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
	reverse_encoding = {val: key for (key, val) in encoding.items()}
	bases = [val for (key, val) in encoding.items()]

	# read in file, convert from dna to bits, then write to bytes to recover the original data
	with open(fn_dna, 'r') as f_dna:
		dna = f_dna.read()

		# determine if error should be introduced
		if error_rate > 0.0:
			print('introducing error with error rate %.3f...' %error_rate)
			dna = add_error(dna, bases, error_rate)

		print('decoding to bits...')
		bits = decode(dna, reverse_encoding)

		print('converting from bits to original format...')
		bits_to_bytes(bits, fn_recovered)

	print('Decoding finished!')


def add_error(dna, bases, error_rate):
	dna_list = [i for i in dna]
	for i in tqdm(range(int(len(dna) * error_rate))):
		idx = random.randint(0, len(dna) - 1)

		# exclude the current base from possible bases
		cur_base = dna_list[idx]
		possible_bases = copy.deepcopy(bases)
		possible_bases.remove(cur_base)
		new_base = random.choice(possible_bases)
		dna_list[idx] = new_base
	dna = ''.join(dna_list)
	return dna


def decode(dna, reverse_encoding):
	""" Decode DNA sequence into bits """
	bits = ''.join([reverse_encoding[base] for base in dna])
	return bits


# def convert_from_bits(bits):
# 	""" Convert from bits to original file content """
# 	bits_int = int(bits, 2)
# 	bits_hex = hex(bits_int)
# 	byte_arr = bytearray.fromhex(bits_hex[2:])
# 	return byte_arr


def bits_to_bytes(bits, out_file):
	""" Convert from bits to bytes and write to output file """
	with open(out_file, 'wb') as f:
		for i in range(0, len(bits), 8):
			a = bits[i: i+8]
			bits_int = int(a, 2)
			byte_arr = bytes([bits_int])
			f.write(byte_arr)


if __name__ == '__main__':
	main()
