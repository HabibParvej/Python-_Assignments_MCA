x1,y1=map(int,input("Enter plot 1(x1 y1):").split())
x2,y2=map(int,input("Enter plot 2(x2 y2):").split())
x3,y3=map(int,input("Enter plot 3(x3 y3):").split())
if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
    print("Points are on Straight line")
else:
    print("Points are not on Staright line")