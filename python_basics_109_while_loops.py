# While loops

# Syntax
# while <condition>:
    # block of code
    # block of code
    # <conditon>
        # breakpoint

# num = 0
# while num < 10:
#     print('still less than 10')
#     num += 1


wish_list = ['rc car', 'cheese', 'cheerleaders', 'white shirts', 'sugar laces', 'reeses pieces', 'pastel de nata']

# Using to substitute the for loop
# print(len(wish_list))
# index_length = len(wish_list)-1
# counter = 0
#
# while counter <= index_length:
#     print(wish_list[counter])
#     counter += 1

while True:
    # Generate random number
    num = 14
    # Ask for user input
    user_guess = int(input('What number do you think I am thinking of? Exit using 0 '))
    # Evaluate input and respond appropriately
    if num == user_guess:
        print('Holy Cow! You guessed it!')
    elif user_guess > num:
        print('Lower.. bit lower')
    elif user_guess == 0:
        break
    elif user_guess < num:
        print('Higher.. bit higher')



