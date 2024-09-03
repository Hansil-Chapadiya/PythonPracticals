class Programmer:
    Company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"Name = {self.name} & Product = {self.product}")
hansil = Programmer("Hansil", "Skype")
hansil.getInfo()