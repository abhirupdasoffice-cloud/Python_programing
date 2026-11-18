ch=input("Input a character:")
if(ch>='A' and ch<='Z'):
    print("Uppercase letter")
elif(ch>='a' and ch<='z'):
    print("Lowercase character")
elif(ch>='0' and ch<='9'):
    print("Digit")
else:
    print("Special character")
