import os
import random
from tqdm import tqdm

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
		fn_bits = fn_in.split('.')[0] + '_recovered.' + fn_in.split('.')[1]
		# encoding to use for converting bits to genomic sequence
		encoding = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
		reverse_encoding = {val: key for (key, val) in encoding.items()}

		# read in file, convert from dna to bits
		with open(fn_in, 'r') as f_in:
			dna = f_in.read()
			bits = decode(dna, reverse_encoding)
			# convert input file data into bits and write to file
			# with open(fn_bits, 'wb') as f_out:
			# 	bits = decode(dna, reverse_encoding)
			# 	f_out.write(bits)

			# # convert bits into original data and write to file
			convert_from_bites2(bits, fn_bits)
			# with open(fn_bits, 'wb') as f_out:
			# 	data = convert_from_bits(bits)
			# 	f_out.write(data)
	print('decode Done')


def decode(dna, reverse_encoding, error_rate=0.0001):
	""" Decode DNA sequence into bits """
	bits = ''.join([reverse_encoding[base] for base in dna])
	bits_list = []
	for i in bits:
		bits_list.append(i)
	for i in tqdm(range(int(len(bits) * error_rate))):
		a = random.randint(0, len(bits) - 1)
		if bits[a] == '0':
			bits_list[a] = '1'
		else:
			bits_list[a] = '0'
	bits = ''.join(bits_list)
	return bits


def convert_from_bits(bits):
	""" Convert from bits to original file content """
	bits_int = int(bits, 2)
	bits_hex = hex(bits_int)
	byte_arr = bytearray.fromhex(bits_hex[2:])
	return byte_arr

def convert_from_bites2(bits, out_file):
	f = open(out_file, 'wb')
	for i in range(0, len(bits), 8):
		a = bits[i: i+8]
		bits_int = int(a, 2)
		byte_arr = bytes([bits_int])
		f.write(byte_arr)

if __name__ == '__main__':
	main('convert')