n=int(input("Input an integer number:"))
m=0
s=1
k=n
while(n>0):
    r=n%10
    n=int(n/10)
    for i in range(1,r+1):
        s*=i
    m+=s
    s=1
if(m==k):
    print(k,"is a krishnamurti number")
else:
    print(k,"is not an krishnamurti number")
