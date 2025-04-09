class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        else:
            if self.front == -1: 
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print("Pushed", item)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear: 
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def traverse(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("The items are: ", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()


s = int(input("Enter the Queue size: "))
obj = CircularQueue(s)

obj.enqueue(4)
obj.enqueue(6)
obj.enqueue(8)
obj.traverse()

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Traverse\n4.Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = int(input("Enter the item: "))
        obj.enqueue(item)
    elif choice == "2":
        item = obj.dequeue()
        if item is not None:
            print("Dequeued", item)
    elif choice == "3":
        obj.traverse()
    elif choice == "4":
        break
