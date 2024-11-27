def fact():
    f=1
    n=int(input("Enter the value that you want to factorial of:"))
    while n>0:
        f=f*n
        n-=1
    print("The factorial is:",f)
def main():
    fact()

if __name__=='__main__':
    main()