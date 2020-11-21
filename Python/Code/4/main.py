str1 = 'Good boy'
str2 = 'Bad girl'

finalStr1 = str1.lower()
finalStr2 = str2.lower()

print('Common Characters:')
for i in finalStr1:
    if i in finalStr2:
        if i != ' ':
            print(i)