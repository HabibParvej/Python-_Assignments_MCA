def evodd(num):
    if num%2==0:
        return True
    else:
        return False

num=int(input("Enter number to check even odd: "))
print("the number is ",evodd(num))