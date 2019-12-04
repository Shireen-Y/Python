# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu



# Learn about how to define a function
# remember what is DRY?
# what is separation of concerns?
# Turn this into a functional program

# Definition of done for the project:
# This should be it's own project
# it should have a read me
    # it should outline the project
    # it should have simple instructions on how to run the project
# it should have git and git history
# it should be on git hub




def bizzuu():
    welcome_message = print('Welcome to the BIZZUU Game')
    ask_for_number = int(input('Please choose a number '))
    if ask_for_number % 5 == 0 and ask_for_number % 3 == 0:
        return ('BIZZUUU')
    elif ask_for_number % 3 == 0:
        return ('This is a Bizz Number')
    elif ask_for_number % 5 == 0:
        return (' This is a Zzuu Number')
    else:
        return ('Try Again ')
print(bizzuu())

