a=float(input("Input mark of 1st subject:"))
b=float(input("Input mark of 2nd subject:"))
c=float(input("Input mark of 3rd subject:"))
d=float(input("Input mark of 4th subject:"))
e=float(input("Input mark of 5th subject:"))
ave=((a+b+c+d+e)/500)*100
if(ave<=100 and ave>=90):
    print("Grade O")
elif(ave<90 and ave>=80):
    print("Grade A")
elif(ave<80 and ave>=70):
    print("Grade B")
elif(ave<70 and ave>=60):
    print("Grade C")
elif(ave<70 and ave>=50):
    print("Grade D")
else:
    print("Grade F")
