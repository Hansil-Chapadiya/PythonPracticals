class Addition():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        

    def __add__(self):
         return self.num1 + self.num2

A = Addition(int(input("Enter Number:: ")),int(input("Enter second Number :: ")))
print(A.__add__())