num = input('Enter a number: ')

list = []
for i in num:
    if i not in list:
        list.append(i)

timesCounter = 0
print('Output:')
for i in list:
    for j in num:
        if j == i:
            timesCounter = timesCounter + 1

    print(str(i) + ':' + str(timesCounter) + 'times')
    timesCounter = 0

print()

evenCounter = 0
for i in list:
    if int(i) % 2 == 0:
        evenCounter = evenCounter + 1

print(evenCounter, 'even digits exist in the input!')