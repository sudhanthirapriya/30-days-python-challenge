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