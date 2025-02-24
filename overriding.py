class Animal:
    
    def toString(self):
        print("Animal")
        
    
    
class Monkey(Animal):
    
    def toString(self):
        print("Monkey")
        

a1=Animal()
a1.toString()

m1=Monkey()
m1.toString()