class Animal:
    def __init__(self):
        print("Animal is created")
        
        
    def toString(self):
        print("Animal")
        
    def walk(self):
        print("Animal walk")
        

class Monkey(Animal()):
    def __init__(self):
        super().__init__() # Referans alınan nesnenin initilaze fonksiyonunu kullanabiliyor artık
             