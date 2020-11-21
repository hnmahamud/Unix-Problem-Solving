#!/bin/bash

#Part A:
echo "Please enter a filename with extension:"
read filename

printf "\n"

echo "File content:"
while read line
do
	echo $line
done < $filename

printf "\n"

echo "Total number of words:"
totalword=`wc -w < $filename`
echo $totalword

#Part B:
echo -n "Are you sure to delete any line from file?(y/n): "
read confirmation

echo -e "$(sed '1d' $filename)\n" > $filename

printf "\n"

echo "After delete any line from the file total number of words:"
totalword2=`wc -w < $filename`
echo $totalword2