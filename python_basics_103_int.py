# Numerical types
# Numerical types are: intergers, floats, composites
    # Big int and complex numbers

# Declaring an int

num1 = 20
print(type(num1))

num2 = 20.0
print(type(num2))

# Operators # +, -, *, /, % --> These take priority over logical operators, however.. use brackets to be sure

result1 = 10 + 12 # Adding
result2 = 10 - 2 # Subtracting
result3 = 10 * 30 # Multiplying
result4 = 20 % 2 # Finding the remainder
result5 = 20 / 2 # dividing

print(result1, result2, result3, result4, result5)


# Logical Operators -->
# One = is assignment
num_a = 10
num_b = 10
num_c = 13

# Bigger than --> returns a boolean (bool)
print(num_b > num_c)
print(num_c > num_a)
# Smaller than
print(num_b < num_c)

# Bigger/Smaller or equal
print(num_a >= num_b)
print(num_a <= num_b)
print(num_b <= num_c)

# Check if the same
## Data type matters
print('10' == 10)
print(num_b == num_a)
print(num_a == num_c)

# Boolean
    # True or False
print(type(True))
print(type(False))

bool_true = True
bool_false = False

print(bool_true == bool_false)
print(bool_true != bool_false)

# Logical AND
# Syntax
# (<condition> and <condition>) --> outputs a bool
    # Requires the two sides to be true to return true

print(True and True) # The two sides and true
print(True and False) # Only one side is true --> becomes false

# Logical <OR>
# Syntax
# (<condition> and <condition>) --> outputs a bool
    # Requires only one side to be true to result in true

print(True or True) # The two sides and true
print(True or False) # Only one side is true --> results in true