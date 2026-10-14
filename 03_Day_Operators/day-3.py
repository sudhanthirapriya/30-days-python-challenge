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
