class node:
    def __init__(self, data):
        self.info = data
        self.link = None

class clinkedlist:
    def __init__(self):
        self.start=None
    def start_at_beginning(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            nd.link=self.start
        else:
            temp=self.start
            while temp.link!=self.start:
                temp=temp.link
            nd.link=self.start
            self.start=nd
            temp.link=self.start
    
    def display(self):
        temp=self.start
        while temp.link!=self.start:
            print(temp.info,end="->")
            temp=temp.link
        print(temp.info)


ob = clinkedlist()
ob.start_at_beginning(10)
ob.start_at_beginning(20)
ob.start_at_beginning(30)
ob.display()
