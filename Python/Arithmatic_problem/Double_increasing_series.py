n=int(input("Input an integer number:"))
s=0
while(n>0):
    for i in range(1,n+1):
        s+=i
    n-=1
print("Sum of the given series=",s)
