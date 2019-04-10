import sys
import binascii


def main():
	fn_in = sys.argv[1]
	fn_bits = fn_in.split('.')[0] + '.bits'
	fn_recovered = fn_in.split('.')[0] + '.recovered'

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

		# convert bits into original data and write to file
		with open(fn_recovered, 'w') as f_out:
			data = convert_from_bits(bits)
			f_out.write(data)


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
	main()