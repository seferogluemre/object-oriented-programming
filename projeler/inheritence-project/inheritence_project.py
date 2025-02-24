class WebSite:
    
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        
    def login_info(self):
        print(self.name+" "+self.surname)
        
    




p1=WebSite("Ahmet", "Mehmetoglu")
p1.login_info()





