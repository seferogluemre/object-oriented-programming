from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    def toString(self): pass


class Square(Shape):

    def __init__(self, edge):
        self.__edge = edge

    def area(self):
        result = self.__edge**2
        print("Square area "+result)
        
    def perimeter(self):
        result=self.__edge*4
        print("Square perimeter "+result)
        
    def toString(self):
        print("Square edge"+self.__edge)
        
    

def Circle(Shape):
    def __init__(self,radius):
        self.__radius=radius
        
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass
        
        
        
        
        
        
        
        
        
        
        