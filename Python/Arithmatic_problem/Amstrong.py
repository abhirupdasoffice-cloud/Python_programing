n=int(input("Input a number:"))
m=n
s=0
p=1
j=1
i=0
while(n>0):
    n=n//10
    i+=1
k=m
while(m>0):
    r=m%10
    while(j<=i):
        p=p*r
        j+=1
    s=s+p
    p=1
    j=1
    m=m//10
if(s==k):
    print(k,"is an amstrong number.")
else:
    print(k,"is not an amstrong number.")
