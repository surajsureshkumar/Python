# Day 2: 30 Days of python programming
first_name = 'ABC'
last_name = 'XYZ'
full_name = first_name + last_name
country = 'VVV'
city = 'VVVVV'
age = 2254
year = 1778
is_married = False
is_true = True
is_light_on = False
dad, mom, sister = 'S', 'R', 'V'

# Checking the data types of the declared variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(dad))

print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two  # sum of two numbers
print(total)
diff = num_two - num_one  # difference of two numbers
print(diff)
product = num_one * num_two  # product of two numbers
print(product)
division = num_one / num_two  # division of one number from another
print(division)
remainder = (num_two % num_one)  # difference of two numbers
print(remainder)
exp = num_one ** num_two  # exponent
print(exp)
floor_division = num_one // num_two  # floor division of one number from another
print(floor_division)

# Calculating the area and circumference of the circle
radius = int(input("Enter the radius"))
area_of_circle = 3.14 * (radius ** 2)
print(area_of_circle)
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

# Taking inputs from user
firstname = input('Enter the first name')
lastname = input('Enter the last name')
country = input('Enter the country')
age = input('Enter the age')
