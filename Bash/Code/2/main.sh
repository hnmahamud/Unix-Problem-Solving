#!/bin/bash

echo "Please enter a line of text:"
read text

printf "\n"

IFS=', '

read -a arr <<< "$text"

for (( i=${#arr[@]} - 1; i >= 0; i-- ))
do
    arr2=("${arr2[@]}" "${arr[i]}")
done

echo "${arr2[@]}"