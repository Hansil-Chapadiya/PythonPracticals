class calc:    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2   
    def __add__(self):
        return self.num1 + self.num2

    def __mul__(self):
        return self.num1 * self.num2
    
    def __div__(self):
        return self.num1 / self.num2

    def __modulo__(self):
         return self.num1 % self.num2

    def __Sub__(self):
        return self.num1 - self.num2

if __name__ == "__main__":
    while True:
        O = '''------------>Calculator<--------------
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Modulo
    5.Division 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
        print(O)
        Q = input("Enter Your Choice  or For Quit, Press Q or S:: ")
        if Q == 'Q' or Q == 'S' or Q == 'q' or Q == 's':
            break

        c = calc(int(input("Enter first Number :: ")), int(input(("Enter Second Number :: "))))
        print("Ans =  ")
        if  Q == '1' :
            print(c.__add__())

        elif Q == '2' :
            print(c.__Sub__())

        elif Q == '3':
            print(c.__mul__())

        elif Q == '4':
             print(c.__modulo__())

        elif Q == '5':
            print(c.__div__())
        else :
            print("Invalid Choice")
        print("==============================================================")
        print("==============================================================")
    print("\n")



