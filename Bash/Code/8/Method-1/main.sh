#!/bin/bash

arr=(sayeed sakib shaon pranto hasib anik evan shaon sayeed hasib)

unset dupes
declare -A dupes

for i in "${arr[@]}"
do
	if [[ -z ${dupes[$i]} ]]
    	then
        	newarr+=("$i")
    	fi
    	dupes["$i"]=" "
done

echo "Array:"
echo "${arr[@]}"

printf "\n"

echo "After removing and sorting duplicate elements:"
for i in "${newarr[@]}"
do
	echo "$i"
done | sort -u