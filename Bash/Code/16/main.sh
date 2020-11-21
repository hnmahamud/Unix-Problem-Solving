#!/bin/bash

echo "Enter a string that defines number in words: "
read num

declare -A array2=( [one]=1 [two]=2 [three]=3 [four]=4 [five]=5 [six]=6 [seven]=7 [eight]=8 [nine]=9 [ten]=10 [eleven]=11 [twelve]=12 [thirteen]=13 [fourteen]=14 [fifteen]=15 [sixteen]=16 [seventeen]=17 [eighteen]=18 [nineteen]=19 [twenty]=2 [thirty]=3 [forty]=4 [fifty]=5 [sixty]=6 [seventy]=7 [eighty]=8 [ninety]=9 [One]=1 [Two]=2 [Three]=3 [Four]=4 [Five]=5 [Six]=6 [Seven]=7 [Eight]=8 [Nine]=9 [hundreds]="" [hundred]="" )

declare -A array3=( [one]=1 [two]=2 [three]=3 [four]=4 [five]=5 [six]=6 [seven]=7 [eight]=8 [nine]=9 [ten]=10 [eleven]=11 [twelve]=12 [thirteen]=13 [fourteen]=14 [fifteen]=15 [sixteen]=16 [seventeen]=17 [eighteen]=18 [nineteen]=19 [twenty]=20 [thirty]=30 [forty]=40 [fifty]=50 [sixty]=60 [seventy]=70 [eighty]=80 [ninety]=90 [One]=1 [Two]=2 [Three]=3 [Four]=4 [Five]=5 [Six]=6 [Seven]=7 [Eight]=8 [Nine]=9 [hundreds]="" [hundred]="" )

declare -A array4=( [one]=1 [two]=2 [three]=3 [four]=4 [five]=5 [six]=6 [seven]=7 [eight]=8 [nine]=9 [One]=1 [Two]=2 [Three]=3 [Four]=4 [Five]=5 [Six]=6 [Seven]=7 [Eight]=8 [Nine]=9 [hundreds]=00 [hundred]=00 )

ARRAY=()

printf "In digits: "

IFS=' '

read -a strarr <<< "$num"


for val in "${strarr[@]}";
do

 if ((${#strarr[@]}==4));then
   printf "${array2[$val]}"
   ARRAY+=("${array2[$val]}")

 elif ((${#strarr[@]}==2));then
   printf "${array4[$val]}"
   ARRAY+=("${array4[$val]}")

 

 else
   printf "${array3[$val]}"
   ARRAY+=("${array3[$val]}")
 fi

done

sum=$(IFS=+; echo "$((${ARRAY[*]}))")
printf "\nSum of the digits= $sum\n\n"
