a=int(input("Input number of lines in upper triangle:"))
for i in range(1,a+1):
    for j in range(1,a-i+2):
        print(" ",end=" ")
    print("*",end=" ")
    if(i>1):
        for j in range(1,2*i-2):
            print(" ",end=" ")
        print("*",end=" ")
    print()
for i in range(a-1,0,-1):
    for j in range(1,a-i+2):
        print(" ",end=" ")
    print("*",end=" ")
    if(i>1):
        for j in range(1,2*i-2):
            print(" ",end=" ")
        print("*",end=" ")
    print()
