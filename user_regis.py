import re
import logging

def main():
    
    logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def first_name_validation(first_name):
        pattern=r'^[A-Z][a-zA-Z]{2,}'
        if re.findall(pattern,first_name):
            print("The First Name is Valid.")
            logger.info("The First Name is Valid.")
        else:
            logger.info("The First Name is not valid.")
            print("The First Name is not valid.")

    def last_name_validation(last_name):
        pattern=r'^[A-Z][a-z]{2,}'
        if re.findall(pattern,last_name):
            logger.info("The Last Name is Valid.")
            print("The Last Name is Valid.")
        else:
            logger.info("The Last Name is not valid.")
            print("The Last Name is not valid.")

    def email_validation(email):
        pattern=r'^[A-Za-z].*[a-zA-Z0-9].*@[a-zA-Z].*\.[a-zA-Z].*[a-zA-Z]$'
        if re.findall(pattern,email):
            logger.info("The email is valid.")
            print("The email is valid.")
        else:
            logger.info("The email is not valid.")
            print("The email is not valid.")

    def mobile_num_validation(mobile_num):
        pattern=r'^\d{2} \d{10}$'
        if re.match(pattern,mobile_num):
            logger.info("The Mobile Number is valid")
            print("The Mobile Number is valid")
        else:
            logger.info("The Mobile Number is not valid")
            print("The Mobile Number is not valid")

    def password_rule(password):
        pattern=r'[a-zA-Z0-9]{8,}'
        if re.match(pattern,password):
            logger.info("The password is valid.")
            print("The Password is valid")
        else:
            logger.info("The password is not valid")
            print("The password is not valid")
    
    first_name=input("Enter the First Name: ")
    last_name=input("Enter the Last Name: ")
    email=input("Enter the email: ")       
    mobile_num=input("Enter the mobile number: ")
    first_name_validation(first_name)
    last_name_validation(last_name)
    email_validation(email)
    mobile_num_validation(mobile_num)
    password=input("Enter the password: ")
    password_rule(password)

if __name__=="__main__":
    main()