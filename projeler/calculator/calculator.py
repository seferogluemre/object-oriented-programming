# Calculator Project

class Calc(object):
    
    def __init__(self,a,b):
        self.value1=a
        self.value2=b
    
        

    def add(self):
        return self.value1+self.value2        
    
    
    def multiply(self):
        return self.value1*self.value2
         



v1=5
v2=4

c1=Calc(v1, v2)
add_result=c1.add()
multiply_result=c1.multiply()

print("Add: {}, Multiply: {}".format(add_result, multiply_result))











