class Employee:
    def __init__(self,name,company):
        self.name = name
        self.company = company

class Programmer(Employee):
    def __init__(self,surname,name,company):
        super().__init__(name, company)
        self.surname = surname


#e = Employee()
#print(e.company)
p = Programmer("Chapadiya", "Hansil", "Google")
print(f"{p.name}  {p.surname} And Company = {p.company}")
