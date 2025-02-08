import re

def first_name_validation(first_name):
    pattern=r'^[A-Z][a-z].{1,}'
    if re.findall(pattern,first_name):
        print("The First Name is Valid.")
    else:
        print("The First Name is not valid.")


first_name=input("Enter the First Name: ")
first_name_validation(first_name)