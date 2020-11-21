class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def result(self):
        txt = open('test.txt')
        readOne = txt.readline()
        readAll = txt.readlines()
        allData = []
        for i in readAll:
            finalSplit = i.split()
            allData.append(finalSplit)

        counter = 1
        for i in allData:
            if self.id == i[0]:
                print('Name: ', self.name)
                print('ID: ', i[0])
                print('Result: ', i[1])
                break
            else:
                if len(allData) == counter:
                    print('ID not found!')

            counter = counter + 1

        txt.close()

id = input('Enter student ID: ')
name = input('Enter student Name: ')

print()

test = Student(id, name)
test.result()