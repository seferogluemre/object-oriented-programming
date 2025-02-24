class WebSite:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def login_info(self):
        print(self.name+" "+self.surname)


class WebSite1(WebSite):
    def __init__(self, name, surname,ids):
        WebSite.__init__(self, name, surname)
        self.ids=ids
        
    def login(self):
        print(self.name+" "+self.surname+" "+self.ids)




class WebSite2(WebSite):
    def __init__(self,name,surname,email):
        WebSite.__init__(self,name,surname)
        self.email=email
        
        
    def login(self):
        
        print(self.name+" "+self.surname+" "+self.email)
        
        
        
        
        
        


p1 = WebSite("Ahmet", "Mehmetoglu")
p1.login_info()

p2 = WebSite1("Ahmet", "Mehmetoglu","123")
print(p2)
p3 = WebSite2("Osman", "osmanoglu","1223233")
print(p3.login)




