print('Enter a string that defines number in words: ')
str = input('> ')

dic1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
            'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19, 'twenty': 2, 'thirty': 3, 'forty': 4, 'fifty': 5,
            'sixty': 6, 'seventy': 7, 'eighty': 8, 'ninety': 9, 'hundreds': '', 'hundred': ''}

dic2 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
            'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
            'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundreds': '', 'hundred': ''}

dic3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9, 'hundreds': '', 'hundred': ''}

strList = str.lower().split(' ')

list = []

print('In digit:')
for i in strList:
    if len(strList) == 4:
        print(dic1[i], end='')
        list.append(dic1[i])

    elif len(strList) == 2:
        print(dic3[i], end='')
        list.append(dic3[i])

    else:
        print(dic2[i], end='')
        list.append(dic2[i])

print()
print()

counter = 0
for i in list:
    if i != '':
        counter = counter + i

print('Sum of all digit:',counter)