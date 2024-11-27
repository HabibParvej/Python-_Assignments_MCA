
def worker():
    wh=40
    for i in range(1,11):
        n=int(input(f"Enter The Working Hours Of Employe{i}::"))
        if n>wh:
            print("You Have worked For Extra",(n-wh),"hours And you get extra Rs:",((n-wh)*12))
        else:
            print("No Overtime")

def main():
    worker()

if __name__ =='__main__':
    main() 
            
              
    
    


