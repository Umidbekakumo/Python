
#Integers
variable1 = 123 
print(variable1)

#Float
variable2 = 12.3 
print(variable2)
# python3 test.py to run 


#Octal numbers starts with 0o or 0O -  represents the numbers (0 - 7) it cant be 0o189 
Print(0o123) 

var = 83
print(oct(var3))

#Hexidecimal Number 
0x or )x 
16 elements (0-9 , a - f ) 

print(hex(57))

# Mathematical Operations in Python 
# -Divison -Mulitply -Addition -Substract -Integer division -Modules -Power 

#additon and subtraction
print(5 + 4) print(5 - 4) 

#multiply 
print(5 * 3)

#division is always a float
 print(6 / 2)

 #Integer Divison - round down to the lowest number 
print(19 // 5)

# Modules - takes the remainder of a divided number - 5x3 = 15 , 19-15 = 4 This is the module 
print(19 % 5)

#Power is a double ** 2 to the power of 3 
print(2 ** 3) 
2 * 2 * 2 

# Boolean data type and strings 
# can only be 2 statements ( true or false ) 
a = 1 
b = 2
Print(a is b)
false 
if 
is, and, or 

#Strings 
#any kind of numbers or letters - it starts with ' ' or " " 
string1 = 'Hello World'
print(string1) 

multiline_string = '''this is a multi line string'''
print(multiline_string)

#Input functions - 
# similar to read -s in bash 
# Input function will always output string 
inp = input('please provide your name: ')
print('hello', inp) 

num1 = input('please provide your first number: ')
num2 = input('Please provide your second number: ')
ans = num1 + num2 
print (ans)


# Len function 
str1 = 'hello world'
print(len(str1))
#answer is 11

# String concantenation
str1 = 'hello'
str2 = 'World'
print(str1 + str2)

name = input('Please provide your name')
print('Hello ' + name) 

# String Slicing - going to slice a string " always starts with zero and counts the letters inside the numbers"
str1 = 'hello world, some random thing'
print(str1[6:11]) # prints world
print(str1[6:])  = # prints out everything after world 
print(str1[:11]) #prints everything before character 11


#Print() and string keyword arguements 
print('umut')
name = input('Please provide your name: ')
age = input('please provide your age')
print('My name is ', name, 'My age is', age, set='||', end='. Welcome!')
# sep, end 

name = input('Please provide your name: ')
age = input('Please provide your age')
print('My name is', name, 'My age is', age, sep='||', end='. Welcome!')
print(' lastname')






