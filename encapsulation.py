class BankAccount(object):
     
    def __init__(self,name,money,address):
        self.name=name
        self.__money=money
        self.address=address
        
        
        
p1=BankAccount("Ahmet mehmetoglu", 12000, "İstanbul")
p2=BankAccount("Osman osmanoglu", 7300, "Paris")

print(p1.money)

p1.money+=p2.money
print(p1.money)


