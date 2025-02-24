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




p1 = WebSite("Ahmet", "Mehmetoglu")
p1.login_info()
