# Strings!

## Define strings - using '' and ""
my_string = "I'm an amazing string"
my_string2 = 'I am'
my_name = 'Shireen the Great'

print(my_string)
print(type(my_string2))

# Concatenation - Joining of two strings
print ('this is an example of concatenation ' + my_string)
print('these are examples of strings', my_string2, my_string)

concatenate = my_string2 + ' ' + my_name
print(concatenate)


# Interpolation
age = 21
name = 'Julia'

# This is where we need to interpolate
print ('Welcome <person>, you are <age_years> old')
print ('Welcome <person>, you were born on the year <date_birth>')

# This is us actually interpolating values
print (f'Welcome {name}, you are {age} old')
print (f'Welcome {name}, you were born on the year {2019 - age}')


## Useful methods for strings
example_string = " HELLoo "
print(example_string)
print(example_string.strip()) # Remove trailing white spaces
print(example_string.count('L')) # Count number of characters in the string
print(example_string.lower())
print(example_string.upper())
print(example_string.strip().capitalize()) # Chaining methods

# Learning and using .split()
text_to_split = 'this is some example text in our file'
results_split = text_to_split.split(' ')
print(results_split)

# Standard builtin function len()
print(len(example_string))


# Casting int
str_string = '1990'
print(type(str_string))

## str --> int
int_number = int(str_string)
print(type(int_number))

## int --> str
new_str = str(int_number)
print (type(new_str))