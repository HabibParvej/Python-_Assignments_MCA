class term:
    def __init__(self,coeff,exp):
        self.coeff=coeff
        self.exp=exp
        self.link = None
class Polynimial:
    def __init__(self):
        self.start = None
    def traverse(self):
        temp=self.start
        while temp!=None:
            print(temp.coeff,' ',temp.exp)
            temp=temp.link
    def insert(self,coeff,exp):
        t = term(coeff,exp)
        if self.start == None:
            self.start = t
            return
        else:
            temp = self.start
            prev = temp
        while temp != None and exp < temp.exp:
            prev = temp
            temp = temp.link
        if temp == prev:
            t.link = temp
            self.start = t
        elif temp != None:
            prev.link = t
            t.link = temp
        else:
            prev.link = t
    

            
            

ob = Polynimial()
ob.insert(2,3)
ob.insert(3,2)
ob.insert(4,1)
ob.insert(5,0)
ob.traverse()

            



