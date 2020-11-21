#!/bin/bash

echo "Please enter a text data of minimum 3 words:"
read text

printf "\n"

echo "Output:"
echo "$text" | rev | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }'