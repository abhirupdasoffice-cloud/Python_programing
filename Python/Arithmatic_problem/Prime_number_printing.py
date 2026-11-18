n=int(input("Input an integer number:"))
print("Prime numbers upto",n,":")
for i in range(2,n+1):
    flag=0
    for j in range(2,int((i+2)/2)):
        if(i%j==0):
            flag=1
            break
    if(flag==1):
        continue
    else:
        print(i,end="\t")
