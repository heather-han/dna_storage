# decode.py
# Decodes a given input file, and outputs a decoded file in bits, as well 
# as the orginal recovered file
#
# usage: python decode.py <input_file_path>


import sys


def main():
	fn_in = sys.argv[1]
	fn_recovered = fn_in.split('.')[0] + '.recovered'

	# encoding to use for converting bits to genomic sequence
	encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
	reverse_encoding = {val: key for (key, val) in encoding.items()}

	# read in file, convert from dna to bits, then recover the original data
	with open(fn_in, 'r') as f_in:
		dna = f_in.read()
		print('decoding to bits...')
		bits = decode(dna, reverse_encoding)
		print('converting from bits to original format...')
		bits_to_bytes(bits)
	print('Decoding finished!')


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
	with open(out_file, 'wb') as f:
		for i in range(0, len(bits), 8):
			a = bits[i: i+8]
			bits_int = int(a, 2)
			byte_arr = bytes([bits_int])
			f.write(byte_arr)


if __name__ == '__main__':
	main()
