y=int(input("Enter a year:"))
if (y%4==0 and y%100!=0) or (y%400==0):
   print("LEAP YEAR")
else:
   print("NOT A LEAP YEAR")