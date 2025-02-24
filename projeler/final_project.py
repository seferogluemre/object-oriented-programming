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
