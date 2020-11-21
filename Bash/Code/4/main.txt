#!/bin/bash

echo "Please enter a number:"
read num

printf "\n"

if (( $num < 2 ))
then
	echo "$num is not prime by definition!"
else
	for (( i=2; i<=num/2; i++ ))
	do
  		if [ $((num%i)) -eq 0 ]
  		then
    			echo "$num is not a prime number."
    			exit
  		fi
	done
	echo "$num is a prime number."
fi
