# Defining variables
age=30


# Printing
print(age)


# Changing the value of the variable
age=45

print(age)



# Variables are usually named with snake_case
friend_age = 44

# If you will not change the value of a variable
# It is better to name it will all in Uppercase
PI=3.14159

# Variable names does not start with numbers
# Variable names can contain numbers, letters, underscores and dollar signs
# Variable names are case sensitive
# Variable names cannot be keywords




# Numbers in Python

# Integer
age=35
# Float
PI=3.1415


# Whenever there is division included in the calculation
# The output will be given as float
math_ope = 1+3*4/2-2
print(math_ope)


# If you want to do integer division
# Use division sign twice
integer_division = 12//4
print(integer_division)

# Using division sign twice will not show you the remainder

int_div = 12//5
print(int_div)
# Output is 2

# To find the remainder use "%" sign

remainder = 37%2
print(remainder)
# Output is 1


# To find odd numbers
# Divide by 2 and check if the remainder is 1
# To find even numbers
# Divide by 2 and check if the remainder is 0



# Strings

my_string = 'Hello World!'
print(my_string)
string_2 = "Hello World!"
print(string_2)
# You can use double quotations marks and signel quoatations marks
# But the start mark and end mark should match

# If you'll use single quotations mark inside the string it is better to use 
# Double quotation marks to specify and vice vers
string_3 = "My name's Anar"
print(string_3)
string_4 ='He said: "What a beautiful day!"'
print(string_4)
# Another version is to put \ to front of " located inside for Python to ignore it
string_5 = "He said: \"What a beautiful day!\""
print(string_5)

# To be able to use strings as multiline we need to use 3 "" marks

multiline_string = """ Hello World!

That's what John said
"""
print(multiline_string)


# You can add strings together
name = "Anar"
surname = "Abdurahmanov"
age = 22
fullname  = name + " " + surname
print(fullname)

# But, you cannot add strings and numbers together
# Pytohn will throw error
# print(fullname + age)

# You first need to convert integer into string
ae_string = str(age)
print(fullname + " "+ ae_string)

# We can use string formatting to easen the work
# To do this we need to use "f" sign
print(f"{fullname} is {age} years old ")

name = "Anar"
greeting = f"Hello, {name}"

print(greeting)

name = "Ali"
print(greeting)

# Changing the variable value after calculating value of greeting
# will not affect greeting

name = "Anar"
greet1 = "Hello, {}!"

final_greeting = greet1.format(name)
print(final_greeting)
name ="Abu"
print(final_greeting)
# same output


# Another version of doing so
name2 = "Jose"
gree4 = "Hello, {name}!"
fin_greet = gree4.format(name = name2)
print(fin_greet)

description = "{} is {} years old."
print(description.format("Bob", 30))