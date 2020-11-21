class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def result(self):
        if self.id == "011147477":
            print('Name: ', self.name)
            print('ID: ', self.id)
            print('Result: ', 3.02)
        elif self.id == "011113437":
            print('Name: ', self.name)
            print('ID: ', self.id)
            print('Result: ', 3.56)
        elif self.id == "011112323":
            print('Name: ', self.name)
            print('ID: ', self.id)
            print('Result: ', 3.98)
        else:
            print("ID Not Found!")

id = input('Enter student ID: ')
name = input('Enter student Name: ')

print()

test = Student(id, name)
test.result()