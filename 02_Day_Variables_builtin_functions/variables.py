#day2 : 30days of learning python programming
#level 1
first_name="priya"
last_name="sundaram"
fullname=first_name+" "+last_name
country="india"
age=25
city="coimbatore"
year=2026
is_married=False
is_true=True
is_light_on=True
x,y,z,s = 1,2,3,"str"

#level 2
print(type(first_name))
print(type(last_name))
print(type(fullname))
print(type(country))
print(type(age))
print(type(city))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))
print(type(s))
print(len(first_name))
print(len(last_name))
a=len(first_name)
b=len(last_name)
if a>b:
    print("first name is greater than last name")
elif a<b:
    print("last name is greater than first name")
else:
    print("both are same length")

num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
exp=num_one**num_two
floor_division=num_one//num_two

r=30
area_of_circle=3.14*r*r
print("area of circle is:",area_of_circle)

r=30
area_of_circle=3.14*r**2
print("area of circle is:",area_of_circle)

circum_of_circle=2*3.14*r
print("circumference of circle is:",circum_of_circle)

def circles_calculations(radius):
    area=3.14*radius**2
    circumference=2*3.14*radius
    return area,circumference
area,circumference=circles_calculations(30)
print("area of circle is:",area)
print("circumference of circle is:",circumference)

help('keywords')

