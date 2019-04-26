#!/usr/bin/env bash

# remove all files not containing raw data from the data folder
rm data/*recovered*
rm data/*.dna
rm data/*.zip
rm data/*.gz
rm data/*.7z

# get list of all data files
files=($(ls "data/"*))

# save a file with sizes of all files in the data directory
ls -l data/* > results/original_file_sizes

# runtimes for uncompressed files
rm results/runtime
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode.py ${files[i]}) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py $filename.dna 0.0) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime"
done


# runtimes for zip compressed files
rm results/runtime_zip
rm results/file_sizes_zip
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time zipping the file
	echo "Zipping ${files[i]}..."
	zip_time="$(time (zip -r ${files[i]}.zip ${files[i]}) 2>&1 1>/dev/null )"
	echo "Zip ${files[i]}: $zip_time" >> "results/runtime_zip"
	
	# get file size of compressed file
	file_size="$(ls -l ${files[i]}.zip)"
	echo "$file_size" >> "results/file_sizes_zip"

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode.py ${files[i]}.zip) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_zip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py $filename.zip 0.0) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_zip"
done


# runtimes for gzip compressed files
rm results/runtime_gzip
rm results/file_sizes_gzip
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time zipping the file
	echo "Zipping ${files[i]}..."
	zip_time="$(time (gzip -k ${files[i]}) 2>&1 1>/dev/null )"
	echo "Zip ${files[i]}: $zip_time" >> "results/runtime_gzip"
	
	# get file size of encoded file
	file_size="$(ls -l ${files[i]}.gz)"
	echo "$file_size" >> "results/file_sizes_gzip"

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode.py ${files[i]}.gz) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_gzip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py $filename.gz 0.0) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_gzip"
done


# runtimes for 7zip compressed file
rm results/runtime_7zip
rm results/file_sizes_7zip
enc_times=()
dec_times=()
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`

	# time zipping the file
	echo "Zipping ${files[i]}..."
	zip_time="$(time (7z a ${files[i]}.7z ${files[i]}) 2>&1 1>/dev/null )"
	echo "Zip ${files[i]}: $zip_time" >> "results/runtime_7zip"
	
	# get file size of encoded file
	file_size="$(ls -l ${files[i]}.7z)"
	echo "$file_size" >> "results/file_sizes_7zip"

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode.py ${files[i]}.7z) 2>&1 1>/dev/null )"
	enc_times=( ${enc_times[@]} enc_time )
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_7zip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py $filename.7zip 0.0) 2>&1 1>/dev/null )"
	dec_times=( ${dec_times[@]} dec_time )
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_7zip"
done
