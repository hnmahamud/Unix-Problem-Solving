#!/bin/bash

echo -n "Enter any number of 10 digits: "
read num

declare -A arr

evenCounter=0
while read -n1 i; do
    arr[$i]=""
    if [ $(($i%2)) -eq 0 ]
    then
		evenCounter=$((evenCounter+1))
    fi
done < <(echo -n "$num")

timesCounter=0
for i in "${!arr[@]}"
do
   while read -n1 j; do
    	if [ $i == $j ]
    	then
    		timesCounter=$((timesCounter+1))
    	fi
    done < <(echo -n "$num") # If you want to ignore whitespace from string then replace "$words" with "${num// /}"
    echo "$i - $timesCounter times"
    timesCounter=0
done

echo "$evenCounter even digits exist in the input"