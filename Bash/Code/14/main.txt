#!/bin/bash

echo "Please enter a filename with extension:"
read filename

echo "Please enter student ID:"
read id

printf "\n"

while read line
do
	echo "$line"
done < $filename | grep "^[0-9]" | grep $id | awk '{$1="Output:"}1'