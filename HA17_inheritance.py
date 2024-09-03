class Employee:
    name = input("Enter Your Name ::  ")
    company = "Microsoft"

class Programmer(Employee):
    salary = 100000000

e = Employee()
print(f"Name = {e.name}")
p = Programmer()
print(f"Salary = {p.salary}")
print(f"Comapany = {p.company}")