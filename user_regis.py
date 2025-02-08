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

def email_validation(email):
    pattern=r'^[A-Za-z].*[a-zA-Z0-9].*@[a-zA-Z].*\.[a-zA-Z].*[a-zA-Z]$'
    if re.findall(pattern,email):
        print("The email is valid.")
    else:
        print("The email is not valid.")

first_name=input("Enter the First Name: ")
last_name=input("Enter the Last Name: ")
email=input("Enter the email: ")
first_name_validation(first_name)
last_name_validation(last_name)
email_validation(email)