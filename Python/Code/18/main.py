def find_country(country_code):
    country_switch = {
        "88": "Bangladesh",
        "44": "United Kingdom",
        "86": "China",
    }
    return country_switch.get(country_code, "Unknown Country")


def read_number(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    for line in Lines:
         country_code = line[1:3]
         print("Phone Number:" + line + " Country:" + find_country(country_code))
         print()



print("Output:")
read_number("test.txt")