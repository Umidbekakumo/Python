# Class Task
# “The cat is black, and it likes to sleep on the mat. Its name is Max.”
#  1. check if string is not more than 100 letters --> if the check failed then print (‘Your string has more than 100 letters’)
#  2. If the check passed, then grab the first word, save it in a variable
#  3. with the grabbed word, check if that word has less than 5 characters and not more than 2  --> if the check failed then print (‘Your does not meet the requirement’)
#  4. print ‘Success’ (edited)

string = 'The cat is black, and it likes to sleep on the mat. Its name is Max'
if len(string) > 100:
    print('Your string has more than 100 letters')
else:
     print('String length is within the limit')

first_word = string.split()[0]
if len(first_word) < 5 and len(first_word) <= 2:
    print('success')
else:
    print('Your does not meet the requirement')
