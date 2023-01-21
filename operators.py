# Day3 py
age = 24
height = 5.7
complex_number = 23.5
base = int(input("Enter base :"))
height2 = int(input("Enter height :"))
area_of_triangle = 0.5 * base * height
print(area_of_triangle)


a = int(input("Enter side a :"))
b = int(input("Enter side b :"))
c = int(input("Enter side c :"))
perimeter_of_triangle = a + b + c
print(perimeter_of_triangle)

length = int(input("Enter the length of the rectange: "))
width = int(input("Enter the width of the rectangle: "))
area_of_rectangle = 2*(length + width)
print(area_of_rectangle)

radius = int(input("Enter the radius: "))
area_of_circ = 3.14 * radius * radius
circum = 2 * 3.14 * radius
print(area_of_circ)
print(circum)

x = int(input("Enter the x intercept: "))
y = (2*x) - 2
print(y)

print(len('python') != len('dragon'))
print("on" in "python" and "dragon")
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'python' )
length_of_word = len('python')
print(float(length_of_word))
print(str(length_of_word))

num = int(input())
if num % 2 == 0:
    print("Even")

print((7/3) == int(2.7))

print(type(10) == 'type of 10')
print(int(9.8) == 10)

hours = int(input("Enter the hours: "))
rate = int(input("Enter the rate: "))
weekly_earning = hours * rate
print('Your weekly earning is:', weekly_earning)

years = int(input("Enter number of years you have lived: "))
print(years * 365 * 24 * 60 * 60 * 60)

for i in range(1, 6):
    print(i, i ** 0, i**1, i **2,i**3)