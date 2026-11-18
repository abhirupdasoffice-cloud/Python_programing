n=int(input("Input a number:"))
s=0
for i in range(1,int((n+2)/2)):
    if(n%i==0):
        s+=i
if(s==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect nmber")
