def lcm(x,y):
    if(x>y):
        big=x
    else:
        big=y
    while(big>0):
        if(big%x==0 and big%y==0):
            break
        else:
            big+=1
    print("L.C.M of",x,"and",y,"is",big)
a=int(input("Input an integer number:"))
b=int(input("Input an integer number:"))
lcm(a,b)
