# Dictionary
# AKA --> hash or (confusingly) objects in JavaScript
# It works exactly like a dictionary
# It has key and value pairs
    # The key is the word you look up
    # The value is the meaning / value of the word

# Syntax
# {}
# dict = {'key': 'value'}

# Defining a dictionary
my_dictionary = {
'tissues': 'a disposable piece of absorbent paper, used especially as a handkerchief or for cleaning the skin.',
'baseball_bat': 'It is a bat made of wood to play baseball'}

# Accessing or Re-assigning is with the key inside []
print(my_dictionary['baseball_bat'])

my_dictionary['baseball_bat'] = 'A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher'

print(my_dictionary['baseball_bat'])