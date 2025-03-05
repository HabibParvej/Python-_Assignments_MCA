# Create an ADT for Queue using OOPs concept(Imagine Python list do not
# support append and pop).
# Define a class with the name Queue and with the following members
# Data member List l
# Data member Size of the array max
# Data member front and rear
# Define a member function(constructor) __init__ () which define a list l with the
# entries zeros of size max and initialize front and rear with the value −1.
# Define member function Insertion(), to insert new element at the top of the
# rear.
# Define member function Traverse() to display all the values of the queue
# Define member function Deletion() to remove an element from front of the
# queue.

class kyun:
    def _init_(self, size):
        self.size = size
        self.l = []
        self.rear = -1
        self.front = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.l.append(item)
            print("Pushed", item)
        if self.front == -1:
            self.front = 0
    def traverse(self):
        print("The items are: ", end=' ')
        for i in range(self.front, self.rear + 1, 1):
            print(self.l[i], end=" ")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            item = self.l[self.front]
            self.front = self.front + 1
            return item

size = input("Enter the Queue size: ")
obj = kyun(int(size))
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Traverse\n4.Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        obj.enqueue(item)
    elif choice == "2":
        item = obj.dequeue()
        print("Popped", item)
    elif choice == "3":
        obj.traverse()
    elif choice == "4":
        break