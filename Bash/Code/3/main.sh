#!/bin/bash

echo "Please enter a filename:"
read filename

printf "\n"

total_characters=0
total_words=0
total_lines=0

while read line 
do
	characters=`echo $line | wc -c`
	total_characters=$((total_characters+$characters))
	
	words=`echo $line | wc -w`
	total_words=$((total_words+$words))
	
	total_lines=$((total_lines+1))
done<$filename

echo "Total number of characters = $total_characters"
echo "Total number of words = $total_words"
echo "Total number of lines = $total_lines"