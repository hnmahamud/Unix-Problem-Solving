list = [6, 7, 3, 1, 5, 8, 4, 9, 2, 16]

print('After removing all odd numbers the list is:')
formatted_list = []
for i in list:
    if i % 2 == 0:
        formatted_list.append(i)
print(formatted_list)