'''Write a program Python to calculate l.c.m using while loop.'''
def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if((greater%a==0) and (greater%b==0)):
            lcm=greater
            break
        greater+=1
    return lcm

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("LCM of",a,"and",b,"is",lcm(a,b))