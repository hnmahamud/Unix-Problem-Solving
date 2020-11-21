#!/bin/bash

echo "Please enter a filename:"
read filename

printf "\n"

echo "Please enter a search word:"
read search

printf "\n"

total=`grep -c $search $filename`
echo "$total times the word $search is appeared in $filename file."