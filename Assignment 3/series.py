'''Write a program to add first seven terms of the following series using a for loop: 1
 1!/1! + 2!/2! + 3!/3! + 4!/4! + 5!/5! + 6!/6! + 7!/7!'''

for i in range(1,8):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact,end=" ")