class Employee:
    salary = 100000
    increment = 2.5

    @property
    def salaryIncreament(self):
        return self.salary*self.increment
    
    @salaryIncreament.setter
    def salaryIncreament(self,salaryIncreament):
        self.increment = salaryIncreament/self.salary

e = Employee()
print(e.salaryIncreament)
print(e.increment)
    
    