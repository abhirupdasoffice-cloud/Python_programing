num=int(input("Input a number:"))
sum=0
num_1=num
while(num>0):
    r=num%10
    num=int(num/10)
    sum+=r
print("Sum of digits of",num_1,"is",sum)
