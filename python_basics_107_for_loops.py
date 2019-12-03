# For loops!
# For loops will iterate over an iterateable object and run a block of code

# Syntax
# for <placeholder> in <iterateable>:
#       # Doing stuff in this block
#       # More things in a block

# Note: the block of code exist after the : (colon)
# It is the lines of code that ARE INDENTED
# And it STOPS when the indentation stops

# Iterateables are: lists, ranges and dictionaries... and also strings (why?)
import time

wish_list = ['rc car', 'cheese', 'cheerleaders', 'white shirts', 'sugar laces', 'reeses pieces', 'pastel de nata']

# counter = 1
# for item in wish_list:
#     print(counter, '-', item)
#     time.sleep(1.2)
#     counter += 1

list_data = [['rc car', 'cheerleaders', 'white shirts', 'audi r8'],['sugar laces', 'cheese', 'pastel de nata', 'baklava']]

counter = 1
for data in list_data:
    print(data)
    for item in data:
        print(counter, '-', item)
        time.sleep(1.2)
        counter += 1




