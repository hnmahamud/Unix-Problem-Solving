#Part A:
list = [3, 5, 8, 10, -7, 0, 6, -15, 1, -4]

primeList = []
notPrimeList = []

for num in list:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                notPrimeList.append(num)
                break
        else:
            primeList.append(num)

    else:
        notPrimeList.append(num)

print('Prime Number List:', primeList)

print()

#Part B:
negList = []
avg = 0

for i in list:
    if i < 0:
        negList.append(i)

for i in negList:
    avg = avg + i

print('Average of all negative number: ', avg)
