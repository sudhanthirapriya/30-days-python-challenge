#day 3 excercise
age= 25
height=146.9
j=1+1j

#area of triangle
base=int(input("Enter the base : "))
height_triangle=int(input("Enter the height : "))
area=0.5*base*height_triangle
print("Area of triangle is :",area)

#perimeter of triangle
side_a=int(input("Enter the side a : "))
side_b=int(input("Enter the side b : "))
side_c=int(input("Enter the side c : "))
perimeter=side_a+side_b+side_c
print("perimeter of triangle is :", perimeter)

#area and permimeter of rectangle
length=int(input("Enter the length of rectangle : "))
breadth=int(input("Enter the breadth of rectangle : "))
area_rectangle = length*breadth
permimeter_rectangle = 2*(length+breadth)
print("Area of rectangle is :", area_rectangle)
print("Perimeter of rectangle is :", permimeter_rectangle)

#area and circumference of circle
radius=int(input("Enter the radius of circle : "))
area_circle = 3.14*radius*radius
circumference_circle = 2*3.14*radius
print("Area of circle is : ",area_circle)
print("Circumference of circle is : ", circumference_circle)

#slope of a line
x1=int(input("Enter the x1 : "))
y1=int(input("Enter the y1 : "))
x2=int(input("Enter the x2 : "))
y2=int(input("Enter the y2 : "))
slope = (y2-y1)/(x2-x1)
print("Slope of the line is : ", slope)

#slope of a line 

# Equation: y = 2x - 2

# 1. Slope
slope = 2

# 2. X-intercept: set y = 0
x_intercept = 2 / 2

# 3. Y-intercept: set x = 0
y_intercept = 2 * 0 - 2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

#euclidean distance and slope finding 

import math

# Given points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate slope
slope = (y2 - y1) / (x2 - x1)

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope)
print("Euclidean distance:", distance)

#slope comparison of the previous two tasks
slope_1=2
slope_2=0
if slope_1 > slope_2:
    print("Slope of the first line is greater than the second line.")
elif slope_1 < slope_2:
    print("Slope of the first line is less than the second line.")
else:
    print("Both lines have the same slope.")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int(input("Enter the value of x: "))
y = x**2 + 6*x + 9
print("The value of y is:", y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len("python")
dragon_length = len("dragon")
if python_length < dragon_length:
    print("The length of 'python' is less than 'dragon'.")
elif python_length > dragon_length:
    print("The length of 'python' is greater than 'dragon'.")
else:
    print("The lengths of 'python' and 'dragon' are equal.")

# Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "on" in "dragon":
    print("'on' is found in both 'python' and 'dragon' .")
elif "on" in "python" or "on" in "dragon":
    print("'on' is found in either 'python' or 'dragon' ,but noth both.")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
    print("yes,'jargon' is in the senetnce")
else:
    print("no, 'jargon' is not in the sentence")

#There is no 'on' in both dragon and python
if "on" not in "dragon" and "on" not in "python":
    print("There is no 'on' in both 'dragon' and 'python'.")

#Find the length of the text _python_ and convert the value to float and convert it to string
python_length = len("python")
python_lenth_float=float(python_length)
python_length_str=str(python_lenth_float)
print("Length of 'python' as float:", python_lenth_float)
print("Length of 'python' as string:", python_length_str)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x=int(input("Enter a value for x: "))
if x / 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7. with variable
x=2.7
converted_int=int(x)
if 7 // 3 == converted_int:
    print("The floor division of 7 by 3 is equal to the integer value of x.")   
else:
    print("The floor division of 7 by 3 is not equal to the integer value of x.")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.without variable
if 7 // 3 == int(2.7):
    print("The floor division of 7 by 3 is equal to the integer value of 2.7.")
else:
    print("The floor division of 7 by 3 is not equal to the integer value of 2.7.")
#Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("The type of '10' is equal to the type of 10.")
else:
    print("The type of '10' is not equal to the type of 10.")

#Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print("int('9.8') is equal to 10.")
else:
    print("int('9.8') is not equal to 10.")
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=int(input("Enter hours worked: "))
rate_per_hour=float(input("Enter rate per hour: "))
pay=hours*rate_per_hour
print("The pay of the person is:", pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
x= int(input("Enter a number: "))
living_sec=x*365*24*60*60
print("The number of seconds a person can live is:", living_sec)

#prints the table 
for i in range(1,6):
    print(i,1,i,i**2,i**3)
#print the 8 th table
x=8
for i in range(1,20):
    print(i,x,i*x)
