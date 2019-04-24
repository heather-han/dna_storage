import os
import copy
import random
from tqdm import tqdm


def main(path, error_rate=0.1):
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
		bases = [val for (key, val) in encoding.items()]

		# read in file, convert from dna to bits
		with open(fn_in, 'r') as f_in:
			dna = f_in.read()

			# determine if error should be introduced
			if error_rate > 0.0:
				print('introducing error with error rate %.3f...' %error_rate)
				dna = add_error(dna, bases, error_rate)

			print('decoding to bits...')
			bits = decode(dna, reverse_encoding)

			print('converting from bits to original format...')
			bits_to_bytes(bits, fn_bits)

	print('Decoding finished!')


def add_error(dna, bases, error_rate, coverage=20):
	dna_list2 = [i for i in dna]
	dna_list = copy.deepcopy(dna_list2)
	record = [[] for i in dna]
	recover_list = []
	for coverages in tqdm(range(coverage)):
		for i in range(int(len(dna) * error_rate)):
			idx = random.randint(0, len(dna) - 1)
			# exclude the current base from possible bases
			cur_base = dna_list[idx]
			possible_bases = copy.deepcopy(bases)
			possible_bases.remove(cur_base)
			new_base = random.choice(possible_bases)
			dna_list[idx] = new_base
			record[idx].append(new_base)
	for i in tqdm(range(len(record))):
		base_dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
		base_l = ['A', 'C', 'G', 'T']
		for j in record[i]:
			base_dic[j] += 1
		base_dic[dna_list2[i]] = coverage - len(record[i])
		base_list = []
		for item in base_dic.items():
			base_list.append(item[1])
		# print(base_list, base_l[base_list.index(max(base_list))])
		recover_list.append(base_l[base_list.index(max(base_list))])
	dna = ''.join(recover_list)
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
	main('convert')