import re
import logging


def main():
    """
    Description: Driver Code
    
    Parameter: None
        
    Return: Calls the other Functions
    """

    first_name=input("Enter the First Name: ")
    last_name=input("Enter the Last Name: ")
    email=input("Enter the email: ")       
    mobile_num=input("Enter the mobile number: ")
    password=input("Enter the password: ")
    first_name_validation(first_name)
    last_name_validation(last_name)
    email_validation(email)
    mobile_num_validation(mobile_num)
    password_rule(password)

logging.basicConfig(filename="user_registration.log", format='%(asctime)s %(levelname)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def first_name_validation(first_name):
    """
    Description: This function validates the first name using regex
    
    Parameter: first_name: first name is user-inputted
    
    Return: Prints the first name is valid if true else prints not valid
    """
    
    try:
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string.")
        
        pattern = r'^[A-Z][a-zA-Z]{2,}'
        if re.findall(pattern, first_name):
            print("The First Name is Valid.")
            logger.info("The First Name is Valid.")
        else:
            logger.error("The First Name is not valid.")
            print("The First Name is not valid.")
    
    except TypeError as te:
        logger.error(f"Type Error: {te}")
        print(f"Error: {te}")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def last_name_validation(last_name):
    """
    Description: This function validates the last name using regex
       
    Parameter: last_name: last name is user-inputted
    
    Return: Prints the last name is valid if true else prints not valid
    """

    try:
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string.")
        
        pattern=r'^[A-Z][a-z]{2,}'
        if re.findall(pattern,last_name):
            logger.info("The Last Name is Valid.")
            print("The Last Name is Valid.")
        else:
            logger.error("The Last Name is not valid.")
            print("The Last Name is not valid.")
    
    except TypeError as te:
        logger.error(f"Type Error: {te}")
        print(f"Error: {te}")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def email_validation(email):
    """
    Description: This function validates the email using regex
       
    Parameter: email: Email is user-inputted
       
    Return: Prints the email is valid if true else prints not valid
    """

    try:
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")
        
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        if re.findall(pattern,email):
            logger.info("The email is valid.")
            print("The email is valid.")
        else:
            logger.error("The email is not valid.")
            print("The email is not valid.")

    except TypeError as te:
        logger.error(f"Type Error: {te}")
        print(f"Error: {te}")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def mobile_num_validation(mobile_num):
    """
    Description: This function validates the mobile number using regex
    
    Parameter: mobile_num: mobile number is user-inputted
       
    Return: Prints the mobile number is valid if true else prints not valid
    """

    try:
        if not isinstance(mobile_num, str):
            raise TypeError("Mobile Number must be a string.")

        pattern=r'^\d{2} \d{10}$'
        if re.match(pattern,mobile_num):
            logger.info("The Mobile Number is valid")
            print("The Mobile Number is valid")
        else:
            logger.error("The Mobile Number is not valid")
            print("The Mobile Number is not valid")

    except TypeError as te:
        logger.error(f"Type Error: {te}")
        print(f"Error: {te}")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def password_rule(password):
    """
    Description: This function validates the password using regex
       
    Parameter: password: password is user-inputted
       
    Return: Prints the password is valid if true else prints not valid"""

    try:
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")
    
        pattern=r'(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])[a-zA-Z0-9@#$%^&*]{8,}'
        counter=0
        special_char=["@","#","$","%","^","&"]
        counter=sum((1 for i in password if str(i) in special_char))
        if counter==1 and re.match(pattern,password):
            logger.info("The password is valid.")
            print("The Password is valid")
        else:
            logger.error("The password is not valid")
            print("The password is not valid")

    except TypeError as te:
        logger.error(f"Type Error: {te}")
        print(f"Error: {te}")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__=="__main__":
    main()