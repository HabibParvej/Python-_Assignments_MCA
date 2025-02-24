class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def showdata(self):
        print("Name :",self.name)
        print("Roll No :",self.roll)

    def showmarks(self):
        print("Marks :",self.marks)


name = input("Enter Name:")
roll = int(input("Enter The Roll NO:"))
m =[]
for i in range(0,5):
    m.append(int(input("Enter Marks:")))
ob1 = student(name,roll,m)
ob1.showdata()
ob1.showmarks()
