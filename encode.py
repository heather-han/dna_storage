import sys
import binascii


def main():
	fn_in = sys.argv[1]
	fn_out = fn_in.split('.')[0] + '.dna'

	# encoding to use for converting bits to genomic sequence
	encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
	reverse_encoding = {val: key for (key, val) in encoding.items()}

	# read in file, convert to bits, and encode to dna
	with open(fn_in, 'rb') as f_in:
		with open(fn_out, 'w') as f_out:
			data = f_in.read()
			# convert input file data into dna
			bits = convert_to_bits(data)
			dna = encode(bits, encoding)
			f_out.write(dna)


def convert_to_bits(data):
	""" Convert input data into bits """
	hexa = data.hex()
	deci = int(hexa, 16)
	bits = bin(deci)[2:].zfill(8)
	return bits


def encode(bits, encoding):
	""" Encode bits into DNA sequence """
	dna = ""
	length = len(bits) - len(bits)%2
	for i in range(0, length, 2):
		dna += encoding[bits[i:i+2]]
	return str(dna)
	

if __name__ == '__main__':
	main()