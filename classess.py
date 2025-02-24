employee1_name = "Emre"
employee1_age = 17
employee1_address = "Rize"


class Employee(object):

    pass


employee_one = Employee()


class Footballer:

    age = 30
    football_club="Barcelona"
    
    
f1=Footballer()

print(f1)

print("Futbolcunun Yaşı"+str(f1.age)+" ve kulübü"+f1.football_club)

f1.football_club="Real Madrid"

print("Futbolcunun yeni kulübü :"+f1.football_club)

#-----------Methods

class Square(object):
    
    edge=5 # Meter
    
    def area1(self):
        area = self.edge*self.edge
        print("Area:",area)

s1=Square()


print(s1)
print(s1.edge)

s1.edge=7
s1.area1()



class Emp(object):
    
    age = 25
    salary=1000
    
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("FUNCTİON",a)



def ageSalaryRatio(age,salary):
    print(age / salary)



emp1=Emp()

emp1.ageSalaryRatio()

ageSalaryRatio(emp1.age, emp1.salary)





def find_area(a,b):
    area=a*b**2
    return area



pi=3.14
r=5


result1 = find_area(pi,r)
print(result1)

result2 = find_area(pi,10)
print(result2)

print("Alan",result1+result2)





class Animal(object):
   
    
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    
    
    def getAnimal(self):
        return {self.age,self.name}

    


a1=Animal("Brid",0.8)
print(a1.getAnimal())




