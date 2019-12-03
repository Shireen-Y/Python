# If functions
# Control flow
# While loops also part of control flow

# Syntax
# if <condition>:
    # block of code
# elif <condition>:
    # block of code
# else:
    # block of code

age = int(input('What is your age? '))
if age < 21 and age > 18:
    print('You can vote, but unfortunately cannot drink')
elif age >= 18:
    print('You can vote, please register :)')
elif age > 16:
    print('You can drive in the US')
else:
    print('You are a child')


# Most specific condition has to be ontop
# Conditions are built with operators and logical operators
# Once something is True, the block runs and the program exists the function

