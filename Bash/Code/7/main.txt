#!/bin/bash

echo "Product Quantity:"
read quantity

echo "Product Price:"
read price

printf "\n"

function discount() {
	if (( quantity == 5 ))
	then
		count=$(echo 'scale=2;' "($price - ((10 / 100) * $price))" | bc -l )
		echo "Discount Price = $count"
		
	elif (( quantity == 7 ))
	then
		count=$(echo 'scale=2;' "($price - ((15 / 100) * $price))" | bc -l )
		echo "Discount Price = $count"
		
	elif (( quantity == 10 ))
	then
		count=$(echo 'scale=2;' "($price - ((20 / 100) * $price))" | bc -l )
		echo "Discount Price = $count"
		
	else
		echo "You have no discount available!"
		
	fi
}

echo "PRODUCT DETAILS"
echo "Product Quantity = $quantity"
echo "Regular Price = $price"
discount