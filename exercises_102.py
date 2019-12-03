# Lists!

# Define a list with cool things inside!
    # Examples: Christmas list, things you would buy with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????
christmas_list = ['New Phone', 'Christmas jumper', 'Fluffy socks', 'Black jeans', 'Perfume']

# Print the lists and check it's type
print(christmas_list)
print(type(christmas_list))

# Print the list's first object
print(christmas_list[0])

# Print the list's second object
print(christmas_list[1])

# Print the list's last object
print(christmas_list[-1])

# Re-define the first item on the list and
christmas_list[0] = 'i-Phone 11 Pro'

# Re-define another item on the list and print all the list
christmas_list[4] = 'Candles'
print(christmas_list)

# Add an item to the list and print the list
christmas_list.append('New Trainer')
print(christmas_list)

# Remove an item from the list and print the list
christmas_list.pop(3)
print(christmas_list)

# Add two items to list and print the list
christmas_list.extend(['White rug', 'White dressing table'])
print(christmas_list)
