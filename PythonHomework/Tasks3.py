#Write a program that accepts user input of two variables, chars, and word. The program should then perform the following tasks:

#program asks the user to enter four characters and a word. 
#It then combines them into a new string called "result" using string concatenation. 
#The "result" string includes the first half of the characters, 
#followed by the word, and then the second half of the characters. Finally, it prints the resulting string.

# Accept user input of two variables
chars = input("Enter four characters: ")
word = input("Enter a word: ")

# Create the resulting string using string concatenation
result = chars[:2] + word + chars[2:]

# Print the resulting string
print("Result:", result)
