from sys import argv

if len(argv) == 11:
    number = []
    n = 1
    for i in argv:
        if n > 1:
            number.append(i)
        n = n + 1

    sorted_list = []
    for i in number:
        if i not in sorted_list:
            sorted_list.append(i)

    sum = 0
    mul = 1
    sum_list = []
    mul_list = []
    for i in sorted_list:
        if int(i) % 2 == 0:
            sum = int(i) + sum
            sum_list.append(i)
        else:
            mul = int(i) * mul
            mul_list.append(i)

    def sum_str(sum_list):
        str1 = " + "
        return (str1.join(sum_list))

    def mul_str(mul_list):
        str2 = " * "
        return (str2.join(mul_list))

    print('Output:')
    print("Addition : {0} = {1}".format(sum_str(sum_list),sum))
    print("Multiplication : {0} = {1} ".format(mul_str(mul_list),mul))


else:
    print('You must pass 10 arguments...')