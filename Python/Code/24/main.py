std_dic = {
    'sayeed': 75000,
    'sakib': 70000,
    'shaon': 90000,
    'pranto': 38000,
    'hasib': 79000,
    'anik': 80000,
    'evan': 35000,
    'rafi': 82000,
    'pial': 83000,
    'masud': 40000
}


num_list = []
for key in std_dic:
    num_list.append(std_dic[key])
num_list.sort()


print('Output:')


num_list.reverse()
for i in std_dic:
    if std_dic[i] == num_list[0]:
        print('Highest Balance:',i,'(',std_dic[i],')')


num_list.reverse()
for j in std_dic:
    if std_dic[j] == num_list[0]:
        print('Lowest Balance:',j,'(',std_dic[j],')')