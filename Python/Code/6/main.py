class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def result(self):
        if self.id == '011147477':
            print('Student ID: ',self.id)
            print('Student Name: ',self.name)
            print('CGPA: 3.02')
        elif self.id == '011113437':
            print('Student ID: ', self.id)
            print('Student Name: ', self.name)
            print('CGPA: 3.56')
        elif self.id == '011112323':
            print('Student ID: ', self.id)
            print('Student Name: ', self.name)
            print('CGPA: 3.98')
        else:
            print('ID is not found!')

id = input('Enter your ID: ')
name = input('Enter your Name: ')

print()

p = Student(id, name)
p.result()
