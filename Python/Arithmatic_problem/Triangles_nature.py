a=float(input("Input the length of first side:"))
b=float(input("Input the length of second side:"))
c=float(input("Input the length of third side:"))
if(a==b and a==c):
    print("Triangle is equilateral")
elif(a==b or a==c or b==c):
    print("Triangle is isoscales")
else:
    print("Triangle is scalene")
