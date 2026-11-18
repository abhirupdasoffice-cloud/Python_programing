p=float(input("Input the principle amount:"))
r=float(input("Input rate of interest:"))
t=float(input("Input time in year:"))
import math
print("Total amount with interest is",p*pow((1+r/100),t))
print("Compound interest=",(p*pow((1+r/100),t))-p)
