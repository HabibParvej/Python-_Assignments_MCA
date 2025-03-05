class Stack:
    def _init_(self, size):
        self.size = size
        self.list = []
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack overflow")
        else:
            self.top += 1
            self.list.append(item)

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return 
        item = self.list[self.top]
        self.top -= 1
        return item

    def traverse(self):
        for i in range(0, self.top + 1):
            print(self.list[i])

ob = Stack(5)

while True:
        n = int(input("Print 1 for push and 2 for pop (0 to exit): "))
        if n == 1:
            while True:
                n1 = int(input("Enter the value to push (5 to exit): "))
                if n1 == 5:
                    break
                ob.push(n1)
        elif n == 2:
            while True:
                print(ob.pop())
                if n1 == 5:
                    break
        elif n == 0:
            break
        else:
            print("Invalid option. Please enter 1, 2, or 0.")