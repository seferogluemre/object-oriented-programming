from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):pass
    
    @abstractmethod
    def perimeter(self):pass
    
    def toString(self):pass
    
    