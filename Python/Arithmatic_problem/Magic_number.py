n=int(input("Input a number:"))
s=0
m=n
while(n>=10):
    while(n>0):
        r=n%10
        n=int(n/10)
        s+=r
    n=s
    s=0
if(n==1):
    print(m,"is a magic number")
else:
    print(m,"is not a magic number")
