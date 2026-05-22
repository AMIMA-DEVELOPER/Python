class Book:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True

            print("You have borrowed a book")

        else:
            print("Sorry you have not borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed= False

            print("Thank you for returning")

        else:
            print("The book is in the library")

Book1 = Book("THE car","Enid blyton")
Book2 = Book("The Hen","HENRY")
Book3 = Book("The castle","EMMA")

Book1.borrow()
Book2.borrow()
Book3.borrow()


Book1.return_book()
Book2.return_book()
Book3.return_book()


print("Book 1 return:",Book1.return_book())

print("Book 2 borrowed:",Book2.borrow())

print("Book 3 return:",Book3.return_book())




        





