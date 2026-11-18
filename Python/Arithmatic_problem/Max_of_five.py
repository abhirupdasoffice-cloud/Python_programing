num1=int(input("Input a number:"))
num2=int(input("Input a number:"))
num3=int(input("Input a number:"))
num4=int(input("Input a number:"))
num5=int(input("Input a number:"))
if(num1>num2 and num1>num3 and num1>num4 and num1>num5):
    print(num1,"is maximum")
elif(num2>num3 and num2>num4 and num2>num5):
    print(num2,"is maximum")
elif(num3>num4 and num3>num5):
    print(num3,"is maximum")
elif(num4>num5):
    print(num4,"is maximum")
else:
    print(num5,"is maximum")
