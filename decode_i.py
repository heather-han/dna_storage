import os

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
			print('decoding to bits...')
			bits = decode(dna, reverse_encoding)
			print('converting from bits to original format...')
			bits_to_bytes(bits, fn_bits)
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
	main('convert')