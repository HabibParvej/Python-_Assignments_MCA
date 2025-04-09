class node:
    def __init__(self, data):
        self.info = data  
        self.link = None

class linkedlist:
    def __init__(self):
        self.start = None

    def insert_at_end(self, item):
        nd = node(item)
        if self.start is None:
            self.start = nd
            return
        temp = self.start
        while temp.link is not None:
            temp = temp.link
        temp.link = nd

    def display(self):  
        temp = self.start
        while temp:
            print(temp.info, end=' -> ')
            temp = temp.link
        print('None')
    def traverse(self):
        temp = self.start
        while temp != None:
            print(temp.info)
            temp = temp.link
    def insert_at_beginning(self, item):
        nd = node(item)
        if self.start == None:
            self.start = nd
            return
        nd.link = self.start
        self.start = nd
        return
    def reverse_print(self,temp):
        if temp != None:
            self.reverse_print(temp.link)
            print(temp.info,end="->")
    


ob = linkedlist()
ob.insert_at_end(10)
ob.insert_at_end(40)
ob.insert_at_end(20)
ob.insert_at_beginning(43)
ob.display()
# ob.traverse()
ob.reverse_print(ob.start)