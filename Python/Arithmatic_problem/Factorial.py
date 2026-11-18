n=int(input("Input a positive integer number:"))
f=1
i=1
if(n<0):
    print("You have entered a negative number")
elif(n==0):
    print("Factorial=",f)
else:
    while(i<=n):
        f*=i
        i+=1
    print("Factorial=",f)
