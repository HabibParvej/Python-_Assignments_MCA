sum=0
for i in range(1,8):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum+=i/fact
print(sum)
