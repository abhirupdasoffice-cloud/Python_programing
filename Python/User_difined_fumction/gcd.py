def gcd(x,y):
    if(x<y):
        small=x
    else:
        small=y
    while(small>0):
        if(x%small==0 and y%small==0):
            break
        else:
            small-=1
    print("G.C.D of",x,"and",y,"is",small)
a=int(input("Input an integer number:"))
b=int(input("Input an integer number:"))
gcd(a,b)
