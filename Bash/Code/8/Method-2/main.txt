#!/bin/bash

arr=(sayeed sakib shaon pranto hasib anik evan shaon sayeed hasib)

echo "Array:"
echo "${arr[@]}"

printf "\n"

echo "After removing and sorting duplicate elements:"
printf "%s\n" "${arr[@]}" | sort -u
