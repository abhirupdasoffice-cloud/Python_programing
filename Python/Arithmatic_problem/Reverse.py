n=int(input("Input an integer number:"))
s=0
m=n
while(n>0):
    r=n%10
    n=int(n/10)
    s=s*10+r
print("Reverse of",m,"is",s)
