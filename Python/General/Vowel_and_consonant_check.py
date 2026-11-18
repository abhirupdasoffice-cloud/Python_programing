a=input("Input an alphabet:")
if((a>='A' and a<='Z') or (a>='a' and a<='z')):
    if(a=='A' or a=='E' or a=='I' or a=='O' or a=='U' or a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
        print(a,"is vowel")
    else:
        print(a,"is a consonant")
else:
    print("You didn't enter an alphabet")
