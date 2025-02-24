class BankAccount(object):
     
    def __init__(self,name,money,address):
        self.name=name
        self.__money=money
        self.address=address
        
    # get and set blocks
    def getMoney(self):
        return self.__money
        
    def setMoney(self,amount):
        self.__money=amount
        
        
        

p1=BankAccount("Ahmet mehmetoglu", 12000, "İstanbul")
p2=BankAccount("Osman osmanoglu", 7300, "Paris")

print(p1.getMoney())
p1.setMoney(1000)
print(p1.getMoney())