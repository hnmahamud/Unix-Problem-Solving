class Student:
    def __init__(self, studentName, courseCode, marks):
        self.studentName = studentName
        self.courseCode = courseCode
        self.marks = int(marks)

    def grade(self):
        print('Name: ', self.studentName)
        print('Course Code: ', self.courseCode)

        if self.marks >= 80:
            print('Grade: A+')
        elif self.marks >= 70:
            print('Grade: A')
        elif self.marks >= 60:
            print('Grade: B+')
        elif self.marks >= 50:
            print('Grade: B')
        elif self.marks >= 40:
            print('Grade: C')
        else:
            print('Grade: F')

student_name = input('Enter Your Name: ')
course_code = input('Enter Course Code: ')
marks = input('Enter Marks: ')

print()

test = Student(student_name, course_code, marks)
test.grade()