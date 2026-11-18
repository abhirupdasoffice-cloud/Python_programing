a=float(input("Input the length of first side:"))
b=float(input("Input the length of second side:"))
c=float(input("Input the length of third side:"))
s=(a+b+c)/2
from math import sqrt
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is",area)
