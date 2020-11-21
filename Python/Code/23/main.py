from sys import argv
script, str1, str2 = argv

def findCommon():
    length = 0
    print('Common Characters command-line arguments string:')
    for i in finalStr1:
        if i in finalStr2:
            if i != ' ':
                print(i, end='')
                length = length + 1

    print()
    print()

    msg = 'Enter a string  of the length of ' + str(length) + ': '
    finalstr3 = input(msg).lower()

    if len(finalstr3) == length:
        print('After replace the common characters from the second string by the input value:')
        for i in finalStr2:
            if i not in finalstr3:
                print(i, end='')
    else:
        print('Please enter correct length of string..')


finalStr1 = str1.lower()
finalStr2 = str2.lower()
findCommon()