def Armstrong():
    n=int(input("Enter the value of N:"))
    cpy=n
    a=0
    sum=0
    while n>0:
        a=n%10
        sum=sum+(a*a*a)
        n=n//10
    if cpy ==sum:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

def main():
    Armstrong()

if __name__ == "__main__":
    main()
    

