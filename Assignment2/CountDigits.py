n=int(input('Enter a number to check :')) #525
count=0
while n!=0:
    b=n%10 #5
    if b%3==0:
       count+=1
    n=n//10 #

print('Number divisible by 3 is :',count)

