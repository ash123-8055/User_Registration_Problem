import re

def first_name_validation(first_name):
    pattern=r'^[A-Z][a-zA-Z]{2,}'
    if re.findall(pattern,first_name):
        print("The First Name is Valid.")
    else:
        print("The First Name is not valid.")

def last_name_validation(last_name):
    pattern=r'^[A-Z][a-z]{2,}'
    if re.findall(pattern,last_name):
        print("The Last Name is Valid.")
    else:
        print("The Last Name is not valid.")


first_name=input("Enter the First Name: ")
last_name=input("Enter the Last Name: ")
first_name_validation(first_name)
last_name_validation(last_name)