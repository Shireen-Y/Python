# Define a function full_name to take in first and last name
def full_name(first_name, last_name):
    full_name = first_name.capitalize() + ' ' + last_name.capitalize()
    return full_name
    print(full_name(first_name, last_name))

# Define a calculator_sum, to add 2 integers
def calculator_sum(num1, num2):
    sum = int(num1) + int(num2)
    return sum
    print(int(calculator_sum(num1, num2)))

# Define a calculator_subtract, to subtract 2 integers
def calculator_subtract(num1, num2):
    subtraction = int(num1) - int(num2)
    return subtraction
    print(int(calculator_subtract(num1, num2)))

# Define a calculator_multiply, to multiply 2 integers
def calculator_multiply(num1, num2):
    multiplcation = int(num1) * int(num2)
    return multiplcation
    print(int(calculator_multiply(num1, num2)))

# Define a area_square, to multiply 2 integers
def area_square(length):
    #
    pass
    area = int(length) * int(length)
    return area
    print(int(area_square(length)))

# Define a area_triangle, to multiply 2 integers
def area_triangle(height, base):
    #
    pass
    area = (int(base)/2) * int(height)
    return area
    print(int(area_triangle(height, base)))


