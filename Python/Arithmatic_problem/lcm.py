a=int(input("Input a number:"))
b=int(input("Input a number:"))
if(a>b):
    big=a
else:
    big=b
while(big>0):
    if(big%a==0 and big%b==0):
        break
    else:
        big+=1
print("LCM of",a,"and",b,"is",big)
