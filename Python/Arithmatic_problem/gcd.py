a=int(input("Input a number:"))
b=int(input("Input a number:"))
if(a<b):
    small=a
else:
    small=b
while(small>0):
    if(a%small==0 and b%small==0):
        break
    else:
        small-=1
print("G.C.D of",a,"and",b,"is",small)
