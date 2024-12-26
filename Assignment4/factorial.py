'''Write a program in Python to calculate factorial of a natural number using function.'''

def fact(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f    
n=int(input("Enter a number: "))
print("Factorial is: ",fact(n))