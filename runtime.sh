#!/usr/bin/env bash

files=($(ls "data/"*))


# runtimes for uncompressed files
rm runtime
touch runtime
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode_h.py ${files[i]}) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "runtime"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode_h.py $filename.dna) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "runtime"
done


# runtimes for zip compressed files
rm runtime_zip
touch runtime_zip
zip_times=()
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time zipping the file
	echo "Zipping ${files[i]}..."
	zip_time="$(time (zip -r ${files[i]}.zip ${files[i]}) 2>&1 1>/dev/null )"
	echo "Zip ${files[i]}: $zip_time" >> "runtime_zip"
	
	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode_h.py ${files[i]}.zip) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "runtime_zip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode_h.py $filename.dna) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "runtime_zip"
done


# runtimes for gzip compressed files
rm runtime_gzip
touch runtime_gzip
gzip_times=()
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time zipping the file
	echo "Zipping ${files[i]}..."
	zip_time="$(time (gzip -k ${files[i]}) 2>&1 1>/dev/null )"
	echo "Zip ${files[i]}: $zip_time" >> "runtime_gzip"
	
	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode_h.py ${files[i]}.gz) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "runtime_gzip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode_h.py $filename.dna) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "runtime_gzip"
done