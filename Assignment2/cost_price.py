cp=int(input("Enter the cost price of the item"))
sp=int(input("Enter the seling price of the item"))
pf=sp-cp
loss=cp-sp
if pf>0:
    print('your profit of ',pf)
else:
    print('You made loss of:',loss)