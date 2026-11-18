num=int(input("Input a number:"))
num1=num
s=0
while(num>0):
    r=num%10
    num=int(num/10)
    s=s*10+r
if(s==num1):
    print(num1,"is a palindrom number")
else:
    print(num1,"is not a palindrom number")
