""" 
January 10th, 2023, Python Lab 1, Capstone Class

Part 1: Hello, birthday month

Write a program that asks for your name and the month you were born in.
Then, your program should print
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in the current month
Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.
"""

# Ask the user for their name
userName = input('Enter your name: ')

# Calculate the length of the useer's name
userNameLength = len(userName)

# Print the greeting with the length of their name
print(f'Hello {userName}! There are {userNameLength} letters in your name.')

# Ask for their birth month
userBirthMonthInput = input('What month were you born in: ')

# Convert the user input to lowercase
userBirthMonth = userBirthMonthInput.lower()

# Check to see if they were born this month
if userBirthMonth == 'january':
    print('Happy birthday month!')


