word = 'Java'

file = open('test.txt', 'r')
Lines = file.readlines()

for line in Lines:
    lowLine = line.lower()
    lowWord = word.lower()
    if lowWord in lowLine:
        print(line)