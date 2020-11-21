str1 = 'I like python programming'
str2 = 'Python programming is powerful'

finalStr1 = str1.lower()
finalStr2 = str2.lower()

def Convert(string):
    li = list(string.split(' '))
    return li

list1 = Convert(finalStr1)
list2 = Convert(finalStr2)

print('Common words:')
for i in list1:
    for j in list2:
        if i == j:
            print(i)