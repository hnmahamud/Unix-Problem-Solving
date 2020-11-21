class Product:
    def __init__(self,id):
        self.id = id

    def search_product(self):
        txt = open('test.txt')
        readOne = txt.readline()
        readAll = txt.readlines()

        allData = []
        finalData = []
        split_list = []
        for i in readAll:
            finalSplit = i.split()
            allData.append(finalSplit)

        for i in allData:
            if i[0]:
                finalData.append(i[0])
                del i[0]
            if i[-1]:
                finalData.append(i[-2])
                del i[-2]
            if i[-2]:
                finalData.append(i[-1])
                del i[-1]

        pos = 1
        for i in allData:
            listToStr = ' '.join([str(elem) for elem in i])
            finalData.insert(pos, listToStr)
            pos = pos + 4

        length = int(((len(finalData)) - 4) / 4)
        index = 4
        for i in range(0, length):
            if i < length:
                split_list.append(index)
                index = index + 4

        allInfo = [finalData[i: j] for i, j in zip([0] + split_list, split_list + [None])]

        counter = 1
        value = 4000
        for i in allInfo:
            if self.id == i[0] and i[2] == 'Monitor' and int(i[3]) > value:
                print('Name: ', i[1])
                print('Type: ', i[2])
                print('Price: ', i[3])
                break
            else:
                if len(allData) == counter:
                    print('Product not found!')
                    break

            counter = counter + 1

        txt.close()

id = input('Enter Product ID: ')

print()

test = Product(id)
test.search_product()
