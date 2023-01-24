""" 
Part 3: camelCase
Thurman
Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 
Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?
Test your program with different example inputs, and comment your code.  
"""

def banner():
    """ Display program name, using stars """
    message = 'Awesome camel case program'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    """ Display instructions on how to use program """
    print('Enter a sentence and this program will convert it to camelcase.')
# Print the welcoming banner    
banner()
instructions()

# Ask the user for a sentence
userString = input('Enter a sentence: ')
print(userString)

# Convert the sentence to title case
userSentenceTitleCase = userString.title()
print(userSentenceTitleCase)

# Take out the spaces
userSentenceNoSpaces = userSentenceTitleCase.replace(' ', '')
print(userSentenceNoSpaces)

# Take the first character of the string and convert it to lowercase
lowercaseFirstCharacter = userSentenceNoSpaces[0].lower()

# Append the rest of the string to the lowercase character
userSentenceCamelCase = ''.join([lowercaseFirstCharacter, userSentenceNoSpaces[1:]])
print(userSentenceCamelCase)
