def fibo(ran):
    t1=0
    t2=1
    t3=0
    sum=t1+t2
    print(t1,"",t2,"",end='')
    for i in range (2,ran,1):
        t1=t2
        t2=t3
        t3=t1+t2
        print(t3," ",end='')
        sum+=t3
    return sum
       
print("Enter the range to calculate fibonacci series sum: ",end='')
ran=int(input())
print("\nThe sum of fibonacci series is: ",fibo(ran))