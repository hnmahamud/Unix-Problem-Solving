#!/bin/bash

id=$1
name=$2

function info() {
	echo "ID: $id"
	echo "Name: $name"
}

if (( $4 >= 80 && $4 <= 100 ))
then
	info
	echo "Grade: A+"
	
elif (( $4 >= 70 && $4 <= 79 ))
then
	info
	echo "Grade: A"
	
elif (( $4 >= 60 && $4 <= 69 ))
then
	info
	echo "Grade: A-"
	
elif (( $4 >= 50 && $4 <= 59 ))
then
	info
	echo "Grade: B"
	
elif (( $4 >= 40 && $4 <= 49 ))
then
	info
	echo "Grade: C"
	
elif (( $4 >= 33 && $4 <= 39 ))
then
	info
	echo "Grade: D"
	
elif (( $4 >= 0 && $4 <= 32 ))
then
	info
	echo "Grade: F"

else
	echo "Invalid number!"
fi