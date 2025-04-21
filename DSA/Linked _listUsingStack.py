class node:
    def __init__(self, item):
        self.info = item
        self.link = None

class stack:
    def __init__(self):
        self.start = None
        self.top = None

    def push(self, item):
        nd = node(item)
        if self.start == None:
            self.start = nd
            self.top = nd
        else:
            self.top.link = nd
            self.top = nd

    def pop(self):
        if self.start == None:
            print("Stack is empty")
            return
        elif self.start == self.top:
            item = self.start.info
            del self.start
            self.top = self.start = None
            return item
        else:
            temp = self.start
            while temp.link != self.top:
                prev = temp
                temp = temp.link
            item = self.top.info
            self.top = prev
            self.top.link = None
            del temp
            return item

    def display(self):
        temp = self.start
        while temp != None:
            print(temp.info, end=' -> ')
            temp = temp.link
        print('None')

    def traverse(self):
        temp = self.start
        while temp != None:
            print(temp.info, end=" -> ")
            temp = temp.link

ob = stack() 
ob.push(10)
ob.push(20)
ob.push(30)
ob.push(40)
ob.push(50)

print("Traverse stack:")
ob.traverse()
