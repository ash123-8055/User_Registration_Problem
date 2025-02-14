import re

def first_name_validation(first_name):
    pattern=r'^[A-Z][a-zA-Z]{2,}'
    return bool(re.findall(pattern,first_name))

def last_name_validation(last_name):
    pattern=r'^[A-Z][a-z]{2,}'
    return bool(re.findall(pattern,last_name))

def email_validation(email):
    #version2
    # pattern=r'^[A-Za-z]*[\+\-\.]*[A-Za-z0-9]+@[A-Za-z0-9\.]*[a-zA-Z]$'
    #version3
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.findall(pattern,email))

def mobile_num_validation(mobile_num):
    pattern=r'^\d{2} \d{10}$'
    return bool(re.match(pattern,mobile_num))

def password_rule(password):
    pattern=r'(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])[a-zA-Z0-9@#$%^&*]{8,}'
    counter=0
    special_char=["@","#","$","%","^","&"]
    counter=sum((1 for i in password if str(i) in special_char))
    return bool(counter==1 and re.match(pattern,password))