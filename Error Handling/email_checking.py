"""
Created on Thu Aug 22 10:43:57 2019
Simple program with the reg-expression pattern for email

"""

import re
PATTERN = "^[A-Za-z0-9]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"

email = input("Enter an email address: ")

email_match = re.match(PATTERN, email)

if email_match:
    print("This is a valid email format")
else:
    print("This is an invalid email format")