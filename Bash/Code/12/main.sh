#!/bin/bash

#Part-A:
declare -A arr
arr=( [sayeed]=75 [sakib]=70 [shaon]=90 [pranto]=78 [hasib]=79 [anik]=80 [evan]=81 [rafi]=82 [pial]=83 [masud]=84 )

max=${arr[sayeed]}
min=${arr[sayeed]}

for key in ${!arr[*]}
do
	for i in ${arr[$key]}
	do
    		if (( $i > $max ))
    		then
    			max=$i
    			maxname="$key"
    		fi
    
    		if (( $i < $min ))
    		then
    			min=$i
    			minname="$key"
    		fi
	done
done
echo "$maxname achieved highest($max) number!"
echo "$minname achieved lowest($min) number!"

#Part-B:
printf "\n"

n=0
for key in ${!arr[*]}
do
	for i in ${arr[$key]}
	do
    		if (( $i > 80 ))
    		then
    			echo "$key = $i"
    			n=$(( n+1 ))
    		fi
	done
done
echo "--------------------------------------------------"
echo "Total $n students got the marks more than 80"
