#!/bin/bash

echo "Please enter a filename with extension:"
read filename

#Declaring an associative array
declare -A resultArray

counter=0
while read line;
do
# reading each line
if [ $counter -gt 0 ] #ignoring the first line
then
	#Getting the cgpa from end of the line
	CGPA=$(echo "$line" | rev | cut -d" " -f1  | rev )
	Info=$( echo "$line" | cut -d' ' -f2- | sed 's/ *$//g')
	if [ -n "$line" ] # ignoring empty lines
    	then
       	resultArray+=(["$CGPA"]=$Info)
    	fi
fi
counter=$((counter+1))
done < $filename

for k in "${!resultArray[@]}"
do
    echo $k' : '${resultArray["$k"]}
done | sort -rn | awk '{$1=NR}1'