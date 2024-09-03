class Programmer:
    Company = "Google"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        print(f"Name = {self.name} & Salary = {self.salary}")


hansil = Programmer("Hansil", 1000000)
print(hansil.Company)
hansil.getInfo()