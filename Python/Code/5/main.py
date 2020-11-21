# Dictionary of 10 elements
std_dic = {
    'sayeed': 75,
    'sakib': 70,
    'shaon': 90,
    'pranto': 38,
    'hasib': 79,
    'anik': 80,
    'evan': 35,
    'rafi': 82,
    'pial': 83,
    'masud': 40
}


# Extract the value of key contains from std_dic and append to num_list
# Then sort the num_list with Ascending Order
num_list = []
for key in std_dic:
    num_list.append(std_dic[key])
num_list.sort()


print('Output:')


# Reverse the num_list for get the largest value from 0 position
# Then we find the highest mark with name from std_dic
num_list.reverse()
for i in std_dic:
    if std_dic[i] == num_list[0]:
        print('Highest Mark:',i,'(',std_dic[i],')')


# Again reverse the num_list for get the lowest value from 0 position
# Then we find the lowest mark with name from std_dic
num_list.reverse()
for j in std_dic:
    if std_dic[j] == num_list[0]:
        print('Lowest Mark:',j,'(',std_dic[j],')')


# Percentage Calculation
n = 0
m = 0
for i in std_dic:
    if std_dic[i] >= 80:
        n = n + 1
    if std_dic[i] < 40:
        m = m + 1
plus_cal = int((100 * n) / 10)
fail_cal = int((100 * m) / 10)
print(str(plus_cal) + '%' + ' students achieved 80 or more')
print(str(fail_cal) + '%' + ' students are failed')