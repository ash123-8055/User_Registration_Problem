import pytest
import re

#Importing all the necessary functions from the test.py
from test import (
    first_name_validation,
    last_name_validation,
    email_validation,
    mobile_num_validation,
    password_rule
)

#checking test case for first name which works
def test_true_first_name():
    assert first_name_validation("John") == True
    assert first_name_validation("Ashwin") == True
    assert first_name_validation("Logan") == True

#checking test case for first name which gives error
def test_false_first_name():
    assert first_name_validation("john") == False
    assert first_name_validation("ashwin") == False
    assert first_name_validation("123John") == False

#checking test case for last name which works
def test_true_last_name():
    assert last_name_validation("Kumar") == True
    assert last_name_validation("Lamar") == True
    assert last_name_validation("Smith") == True

#checking test case for last name which gives error
def test_false_last_name():
    assert last_name_validation("kumar") == False
    assert last_name_validation("lamar") == False
    assert last_name_validation("kumar123") == False

#checking test case for emails which works
def test_true_email_validation():
    assert email_validation("abc@yahoo.com") == True
    assert email_validation("abc-100@yahoo.com") == True
    assert email_validation("abc111@abc.com") == True

#checking test case for emails which gives error
def test_false_email_validation():
    assert email_validation("abc@.com.my") == False
    assert email_validation("abc123@gmail.a") == False
    assert email_validation("abc123@.com") == False

#checking test case for mobile number which works
def test_true_mobile_num_validation():
    assert mobile_num_validation("91 9253716352") == True
    assert mobile_num_validation("91 9261548361") == True
    assert mobile_num_validation("71 7123157214") == True

#checking test case for mobile number which gives error
def test_false_mobile_num_validation():
    assert mobile_num_validation("921 2187401274")== False
    assert mobile_num_validation("9 123812987982")== False
    assert mobile_num_validation("91 213123123")  == False

#checking test case for password_rule which works
def test_true_password_rule():
    assert password_rule("Ashwin1@") == True
    assert password_rule("aShw1@nk") == True
    assert password_rule("Kumar@12") == True

#checking test case for password_rule which gives error
def test_false_password_rule():
    assert password_rule("Ash") == False
    assert password_rule("Ashwin@@1") == False
    assert password_rule("Ashwin@asd") == False
