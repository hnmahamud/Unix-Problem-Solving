#!/bin/bash

echo "Enter a text data of minimum 3 words: "
read text

read -a arr <<< "$text"

newlist=()

for val in "${arr[@]}"
do
	len=${#val}
	for((i=$len-1;i>=0;i--))
	do
		reverse="$reverse${val:$i:1}"
	done
	newlist+=("$reverse")
	reverse=""
done

echo "Output:"
echo "${newlist[@]}"
