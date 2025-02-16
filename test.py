import re


def first_name_validation(first_name):
    """Description: 
        This function validates the first name using regex
       Parameter:
        first_name: first name is user-inputted
       Return:
        Prints the first name is valid if true else prints not valid"""

    pattern=r'^[A-Z][a-zA-Z]{2,}'
    return bool(re.findall(pattern,first_name))

def last_name_validation(last_name):
    """Description: 
        This function validates the last name using regex
       Parameter:
        last_name: last name is user-inputted
       Return:
        Prints the last name is valid if true else prints not valid"""

    pattern=r'^[A-Z][a-z]{2,}'
    return bool(re.findall(pattern,last_name))

def email_validation(email):
    """Description: 
        This function validates the email using regex
       Parameter:
        email: Email is user-inputted
       Return:
        Prints the email is valid if true else prints not valid"""

    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.findall(pattern,email))

def mobile_num_validation(mobile_num):
    """Description: 
        This function validates the mobile number using regex
       Parameter:
        mobile_num: first name is user-inputted
       Return:
        Prints the mobile number is valid if true else prints not valid"""

    pattern=r'^\d{2} \d{10}$'
    return bool(re.match(pattern,mobile_num))

def password_rule(password):
    """Description: 
        This function validates the password using regex
       Parameter:
        password: password is user-inputted
       Return:
        Prints the password is valid if true else prints not valid"""
        
    pattern=r'(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])[a-zA-Z0-9@#$%^&*]{8,}'
    counter=0
    special_char=["@","#","$","%","^","&"]
    counter=sum((1 for i in password if str(i) in special_char))
    return bool(counter==1 and re.match(pattern,password))