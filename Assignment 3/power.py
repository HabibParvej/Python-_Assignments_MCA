def findpower():
    count=0
    res=0
    n1=int(input("Enter the base Number:"))
    n2=int(input("Enter the power:"))
    while n2>1:
        count+=1
        res=res+n1*n1
        n2-=1
    print("Result is:",res)
def main():
 findpower()

if __name__ == "__main__":
   main()


