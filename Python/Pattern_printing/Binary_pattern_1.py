a=int(input("Input number of lines:"))
k=1
l=0
for i in range(1,a+1):
    for j in range(1,i+1):
        if(i%2==0 and j%2==0):
            print(k,end="\t")
        elif(i%2!=0 and j%2!=0):
            print(k,end="\t")
        else:
            print(l,end="\t")
    print()
