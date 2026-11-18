a=int(input("Input number of lines:"))
for i in range(1,a+1):
    for j in range(a,i-1,-1):
        print("*",end=" ")
    print()
