num=int(input("Input an integer number:"))
flag=0
for i in range(2,int((num+2)/2)):
    if(num%i==0):
        flag=1
        break
if(flag==1):
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
