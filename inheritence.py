class Animal:
    def __init__(self):
        print("Animal is created")
        
        
    def toString(self):
        print("Animal")
        
    def walk(self):
        print("Animal walk")
        
        

class Monkey(Animal):
    def __init__(self):
        super().__init__() # Referans alınan nesnenin initilaze fonksiyonunu kullanabiliyor artık
        print("Monkey created")
        
    def toString(self):
        print("Monkey")
        
    def climb(self):
        print("Monkey can climb")
        

m1=Monkey() 
m1.toString()
m1.walk()