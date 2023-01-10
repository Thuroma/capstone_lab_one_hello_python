""" 
Part 2: List of classes

Write a program that asks for the names of all of the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line. 
"""

# Start a list of classes
listOfClasses = []

# Use a while loop to ask the user for the classes they are taking
while True:
    # Ask them what classes thay are taking
    userClass = input('Enter a class that you are currently taking. Press (q) to quit: ')

    # Set up an escape for the user
    if userClass.lower() == 'q':
        break

    # Add their class to the list of classes
    listOfClasses.append(userClass)

    # Let the user know their class was added
    print(userClass + ' added.')

# Print the user's classes from the list, one by one
for i in range(len(listOfClasses)):
    print(listOfClasses[i])