a=int(input("Input coefficient of X^2:"))
b=int(input("Input coefficient of X^1:"))
c=int(input("Input coefficient of X^0:"))
d=(b**2)-(4*a*c)
if(d<0):
    print("Equatio has complex roots")
else:
    import math
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("Roots of the quadratic equation",a,"X^2+",b,"X+",c,"are",x1,"and",x2)
