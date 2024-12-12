n=int(input("Enter a decimal number to convert to octal: "))
octal=0
i=0
while n>0:
    r=n%8
    octal=octal+r*(10**i)
    n=n//8
    i+=1
print("Octal number is: ",octal)