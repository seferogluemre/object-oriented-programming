from abc import ABC,abstractmethod


class Animal(ABC):
    
     @abstractmethod
 
     def walk(self): pass   
 
     def run(self):pass   
 

class Bird(Animal):

    def __init__(self):
        print("Bird")


    def walk(self): print("Walk")   

    def run(self):print("Run")   




b1=Bird()
    