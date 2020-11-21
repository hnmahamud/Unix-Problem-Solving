list = [7, 3, 5, 8, 7]

print('After removing the duplicate numbers the list is:')
formatted_list = []
for i in list:
    if i not in formatted_list:
        formatted_list.append(i)
print(formatted_list)