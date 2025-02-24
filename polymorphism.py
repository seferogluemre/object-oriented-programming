class Employee:

    def raise (self):
        raise_rate = 0.1
        return 100+100*raise_rate


class CompEng(Employee):
    def raise (self):
        raise_rate = 0.2
        return 100+100*raise_rate


class EEE(Employee):
    def raise (self):
        raise_rate = 0.3
        return 100+100*raise_rate


eee=EEE()
ce=CompEng()
employee=Employee()