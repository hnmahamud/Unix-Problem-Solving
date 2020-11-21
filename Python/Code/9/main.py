import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

password = input("Enter your password: ")
result = re.findall(pattern, password)

if (result):
    print("The password is valid!")
else:
    print("Invalid password!")