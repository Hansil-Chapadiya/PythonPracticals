class Libary:
    def __init__(self,listBook):
        self.book = listBook
    def availablebook(self):
        print("Book present in the Libaray : ") 
        for book in self.book:
            print("-->" + book)

    def borrowbook(self,bookname):
        if bookname in self.book:
            print(f"Done you will get {bookname}. plz keep it safe")
            self.book.remove(bookname)
        else:
            print("Sorry, book is not available ")
        
    def returnBook(self,bookname):
        if bookname in self.book:
            print("Thanks for returning book")
            self.book.append(bookname)
            

class student():
    def requestbook(self):
        self.book = input("Which book is do you want :: ")
        return self.book
    
    def reBook(self):
        self.book = input("Which book is do you return :: ")
        return self.book

if __name__ == "__main__":
    l = Libary(["sherlok holmes", "loluton waves","Python","Text book","C Text book"])
    l.availablebook()
    stu = student()
    while True:
        msg =''' ---------Welcome to the central libarary----------
        Please choose option::
        1. List all the books
        2. Request a book
        3. Return book
        4. Exit from the libary
        '''
        
        print(msg)
        a = int(input("Enter Your Choice :  "))

        if a == 1 :
            l.availablebook()
        elif a == 2:
            l.borrowbook(stu.requestbook())
        elif a == 3:
            l.returnBook(stu.reBook())
        elif a == 4:
            exit()
        else:
            print("Invalid choice ::")
