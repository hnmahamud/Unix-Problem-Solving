#!/bin/bash

echo -n "Text1- "
read text1

echo -n "Text2- "
read text2

printf "\n"

IFS=', '

read -a arr1 <<< "$text1"
read -a arr2 <<< "$text2"

for i in "${arr1[@]}"
do
  for j in "${arr2[@]}"
  do
    if [ $i == $j ]
    then
      arr3=("${arr3[@]}" "$i")
    fi
  done
done

echo -n "Common words: "
sed -E "s/([[:alnum:]]+)/'&'/g;s/ /,/g" <<< ${arr3[@]}