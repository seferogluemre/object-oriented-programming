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