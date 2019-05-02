#!/usr/bin/env bash

ERROR_RATE=0.001

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
for (( i=0;i<${#files[@]};i++ )); do
	filename=`cut -d "." -f1 <<< ${files[i]}`
	ending=`cut -d "." -f2 <<< ${files[i]}`

	# time encoding the file
	echo "Encoding ${files[i]}..."
	enc_time="$(time (python encode.py ${files[i]}) 2>&1 1>/dev/null )"
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py ${files[i]} $ERROR_RATE) 2>&1 1>/dev/null )"
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime"

	# Compute the hex level accuracy of the recovered file against the original file
	xxd ${files[i]} > $filename".hex"
	xxd $filename"_recovered.$ending" > $filename"_recovered.hex"
	diff=`cmp -l $filename".hex" $filename"_recovered.hex" | wc -l`
	numlines=`wc -l $filename".hex" | awk '{print $1}'`
	hex_size="$((16 * $numlines))"  # approximate number of hex characters
	accuracy=`bc -l <<< "$diff/$hex_size*100"`
	echo "Error ${files[i]}: $diff/$hex_size=$accuracy%" >> "results/runtime"

	rm $filename".hex"
	rm $filename"_recovered.hex"
done


# runtimes for zip compressed files
rm results/runtime_zip
rm results/file_sizes_zip
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
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_zip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py ${files[i]}.zip $ERROR_RATE) 2>&1 1>/dev/null )"
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_zip"

	# Compute the hex level accuracy of the recovered file against the original file
	xxd ${files[i]} > $filename".hex"
	xxd $filename"_recovered.$ending" > $filename"_recovered.hex"
	diff=`cmp -l $filename".hex" $filename"_recovered.hex" | wc -l`
	numlines=`wc -l $filename".hex" | awk '{print $1}'`
	hex_size="$((16 * $numlines))"  # approximate number of hex characters
	accuracy=`bc -l <<< "$diff/$hex_size*100"`
	echo "Error ${files[i]}: $diff/$hex_size=$accuracy%" >> "results/runtime_zip"

	rm $filename".hex"
	rm $filename"_recovered.hex"
done


# runtimes for gzip compressed files
rm results/runtime_gzip
rm results/file_sizes_gzip
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
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_gzip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py ${files[i]}.gz $ERROR_RATE) 2>&1 1>/dev/null )"
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_gzip"

	# Compute the hex level accuracy of the recovered file against the original file
	xxd ${files[i]} > $filename".hex"
	xxd $filename"_recovered.$ending" > $filename"_recovered.hex"
	diff=`cmp -l $filename".hex" $filename"_recovered.hex" | wc -l`
	numlines=`wc -l $filename".hex" | awk '{print $1}'`
	hex_size="$((16 * $numlines))"  # approximate number of hex characters
	accuracy=`bc -l <<< "$diff/$hex_size*100"`
	echo "Error ${files[i]}: $diff/$hex_size=$accuracy%" >> "results/runtime_gzip"

	rm $filename".hex"
	rm $filename"_recovered.hex"
done


# runtimes for 7zip compressed file
rm results/runtime_7zip
rm results/file_sizes_7zip
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
	echo "Encode ${files[i]}: $enc_time" >> "results/runtime_7zip"

	# time decoding the file
	echo "Decoding ${files[i]}..."
	dec_time="$(time (python decode.py ${files[i]}.7z $ERROR_RATE) 2>&1 1>/dev/null )"
	echo "Decode ${files[i]}: $dec_time" >> "results/runtime_7zip"

	# Compute the hex level accuracy of the recovered file against the original file
	xxd ${files[i]} > $filename".hex"
	xxd $filename"_recovered.$ending" > $filename"_recovered.hex"
	diff=`cmp -l $filename".hex" $filename"_recovered.hex" | wc -l`
	numlines=`wc -l $filename".hex" | awk '{print $1}'`
	hex_size="$((16 * $numlines))"  # approximate number of hex characters
	accuracy=`bc -l <<< "$diff/$hex_size*100"`
	echo "Error ${files[i]}: $diff/$hex_size=$accuracy%" >> "results/runtime_7zip"

	rm $filename".hex"
	rm $filename"_recovered.hex"
done
