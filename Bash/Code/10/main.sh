#!/bin/bash

#Part A:
echo "Please enter a filename with extension:"
read filename

printf "\n"

word1=`grep -c $1 $filename`
word2=`grep -c $2 $filename`
word3=`grep -c $3 $filename`
total=$(( word1 + word2 + word3 ))
echo "$total times the words $1 $2 $3 is appeared in $filename file."

printf "\n"

echo "Line Numbers:"
line1=`grep -n $1 $filename`
echo "$line1"
line2=`grep -n $2 $filename`
echo "$line2"
line3=`grep -n $3 $filename`
echo "$line3"

#Part B:
s1=$1
s2=$2
s3=$3

i=0
while [ $i -ne ${#s1} ]
do
    c=${s1:$i:1}
    if [[ $result != *$c* && $s2 == *$c* && $s3 == *$c* ]]
    then
      result=$result$c
    fi
    ((i++))
done

printf "\n"

echo "Common characters in three command-line argument:"
echo $result