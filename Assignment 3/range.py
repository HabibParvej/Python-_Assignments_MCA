'''Write a program to find the range of a set of numbers. Range is the difference between the 
smallest and biggest number in the list. '''
n=int(input("Enter a range: "))
l=[0]*n
for i in range(n):
    l[i]=int(input("Enter a number: "))
print(l)

m=max(l)
n=min(l)
print("Range is: ",m-n)