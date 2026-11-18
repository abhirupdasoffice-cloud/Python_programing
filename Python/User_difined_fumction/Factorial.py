def fact():
    n=int(input("Input an integer number:"))
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print("Factorial is",fact())
