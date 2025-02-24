class Employee:

    def raise (self):
        raise_rate = 0.1
        result = 100+100*raise_rate
        print("Employee: "+result)


class CompEng(Employee):
    def raise (self):
        raise_rate = 0.2
        result = 100+100*raise_rate
        print("Comp Eng: "+result)


class EEE(Employee):
    def raise (self):
        raise_rate = 0.3
        result = 100+100*raise_rate
        print("EEE: "+result)


eee = EEE()
ce = CompEng()
employee = Employee()

for employee in employee_list:
    employee.raise()