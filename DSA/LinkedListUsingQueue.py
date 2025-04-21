class node:
    def __init__(self, item):
        self.info = item
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def insertion(self, data):
        nd = node(data)
        if self.front is None:
            self.front = self.rear = nd
        else:
            self.rear.link = nd
            self.rear = nd

    def deletion(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front == self.rear:
            item = self.front.info
            del self.front
            self.front = self.rear = None
            return item
        else:
            temp = self.front
            item = temp.info
            self.front = self.front.link
            del temp
            return item

    def traverse(self):
        temp = self.front
        while temp is not None:
            print(temp.info, end=" -> ")
            temp = temp.link
        print("None")

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.info, end=" -> ")
            temp = temp.link
        print("None")

    def reverse_print(self, temp):
        if temp is not None:
            self.reverse_print(temp.link)
            print(temp.info, end=" -> ")
        return


ob = Queue()
ob.insertion(10)
ob.insertion(20)
ob.insertion(30)
ob.insertion(40)
ob.insertion(50)

print("Traverse after insertion:")
ob.traverse()

print("Deleting one element...")
ob.deletion()

print("Traverse after deletion:")
ob.traverse()

print("Reverse print:")
ob.reverse_print(ob.front)
print("None")  
