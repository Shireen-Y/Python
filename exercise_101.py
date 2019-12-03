# declare some strings

# prompt user for his/her name
# Save it to some variables with good names
user_first_name = input('What is your name? ')
print('You have a lovely name ' + user_first_name + '!')

# prompt the user for some random number between 0 - 99
# store it in a variable called: user_chosen_num
user_chosen_num = input('Pick a random number between 0-99: ')

# print a nice welcome message using user name
print('Welcome ' + user_first_name + '! Have a great time!')

# request the users last_name
user_last_name = input('I have your first name, but I would like to know your last name too. So, what is your last name? ')

# Print a nice message welcoming the user using their first and last name
print("That's fantastic! Thank you so much " + user_first_name + ' ' + user_last_name + '!')

# Ask for the users age
user_age = input('What is your age? ')

# print a message of the users age and what year they were born in
print(f'You are {user_age} years old. That means you were born in {2019 - int(user_age)}')

# Compare the users input to the number they chose at the start and compare it

