# Write a program that takes a string input from the user and reverses it.

# using the input function and the value of the users input is set as a variable as the_input

the_input = input("Enter a word or a sentence: ")

#the second line were using slicing, where we use [::-1] to reverse the variable the_input which is the variable we set in the line above

#This slicing notation means to start at the end (-1 index) and move towards the beginning, effectively reversing the order of 

#characters in the string. The reversed copy is then assigned to the variable reversed.

reversed = the_input[::-1]

#this last line prints the variable reversed 
print(reversed)