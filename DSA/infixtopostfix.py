class Infixtopostfix:
    def __init__(self,lst):
        self.infix = lst
        self.postfix = []
        self.stack = [0] * 20
        self.top = -1
        


    def postfixconversion(self):
        for i in self.infix:
            if i.isalnum():  
                self.postfix.append(i)
            if i == '(': 
                self.top += 1
                self.stack[self.top]=1
            if i == ')':
                pass
            if i in ['+','-','*','/','^']:
                self.top+=1
                self.stack[self.top]=i

    

            
    def Display(self):
        print(self.infix)
        print(self.postfix)
        print(self.stack)
        






ob = Infixtopostfix(['A', '+', 'B', '*', '(', 'C', '-', 'D', ')', '-', 'E', '/', 'F'])
ob.Display()