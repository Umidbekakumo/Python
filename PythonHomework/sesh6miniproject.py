#MINI project Password checker

#first i will make varibale for true or false for the password
# missing_criteria = []  # List to store missing criteria
#re.search() is a function provided by the re module in Python 
# that allows you to search for a specific pattern 
# within a given string.
missing_criteria = []
A33 = 0 
password = input('Enter your password: ')
import re
if not re.search('[a-z]', password):
    A33 = 1
    missing_criteria.append("at least one lowercase letter")
if not re.search('[0-9]', password):
    A33 = 1
    missing_criteria.append("at least one digit")
if not re.search('[A-Z]', password):
    A33 = 1
    missing_criteria.append("at least one uppercase letter")
if not re.search('[@#$!]', password):
    A33 = 1
    missing_criteria.append("at least one special character")
if len(password)<8:
    A33 = 1 
    missing_criteria.append("at least 8 characters long")
if A33 == 0:
    print('password accepted')
else:
    print('Password is not accepted. Missing criteria:',','.join(missing_criteria))


