a=int(input("Input number of lines:"))
for i in range(1,a+1):
    for j in range(1,a-i+1):
        print(end="\t")
    for j in range(1,i+1):
        print("*",end="\t")
    print()
