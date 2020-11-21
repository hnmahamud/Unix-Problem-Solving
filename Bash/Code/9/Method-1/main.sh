#!/bin/bash

echo "Please enter a filename with extension:"
read filename

printf "\n"

while read line
do
	echo "$line"
done < $filename | grep "^[0-9]" | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }' | sort -g -rk1 | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }' | awk '{$1=NR}1'