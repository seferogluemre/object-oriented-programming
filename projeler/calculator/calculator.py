# Calculator Project

class Calc(object):
    
    def __init__(self,a,b):
        self.value1=a
        self.value2=b
    
        

    def add(self):
        return self.value1+self.value2        
    
    
    def multiply(self):
        return self.value1*self.value2
         



print("Choose Add(1), multiply(2)")
selection = input("Select 1 or 2")

v1=input("first value")
v2=input("Second value")

c1=Calc(int(v1), int(v2))
add_result=c1.add()
multiply_result=c1.multiply()

print("Add: {}, Multiply: {}".format(add_result, multiply_result))











