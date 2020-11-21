#!bin/bash

#Part-1:
echo "Enter a Number:"
read number

echo "Output:"
echo "$number" | awk -vFS="" '{for(i=1;i<=NF;i++){ if($i~/[0-9]/) { w[$i]++ } } }END{for(i in w) if(w[i] > 1){ print i " is " w[i] " times" } } '

#Part-2:
printf "\n"

number2=`grep -o . <<<$number`

n=0
for i in $number2
do
	if [ $((i%2)) -eq 0 ]
	then
		n=$((n+1))
	fi
done

echo "$n even digits exist in the input"