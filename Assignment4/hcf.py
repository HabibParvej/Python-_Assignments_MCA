'''Write a program in Python to calculate H.C.F using while loop.'''
def hcf():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    while(a%b!=0):
        rem=a%b
        a=b
        b=rem
    return b

print(hcf())