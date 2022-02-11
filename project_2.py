
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print('Books in library are:')
        for i in self.books:
            print(" * " + i)

    def borrowBook(self, bookname):
        if bookname in self.books:
            self.books.remove(bookname)
            print("Thank you for borrowing", bookname, 'book')
        else:
            print("Sorry this book is not available in library")

    def returnBook(self, bookname):
        if bookname in self.books:
            self.books.append(bookname)
            print("Thank you for returning", bookname, "book")
        else:
            self.books.append(bookname)
            print("Thank you for adding new book into library")

class Student:
    def requestBook(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book

    def returnBook(self):
        bookname = input("Enter the book you want to return: \n ")
        return bookname


availableBooks = Library(['Hindi', 'Eng', 'Maths', 'Science'])
student = Student()
while(True):
    welcomeMsg = '''=====Welcome to Smart Square Library=====
    1. To See Available Books
    2. To Borrow Books
    3. To Return Books
    4. To Exit
    '''
    print(welcomeMsg)
    userInput = int(input("Enter a Choice: "))
    if userInput == 1:
        availableBooks.displayAvailableBooks()
    elif userInput == 2:
        availableBooks.borrowBook(student.requestBook())
    elif userInput == 3:
        availableBooks.returnBook(student.returnBook())
    elif userInput == 4:
        print("Thanks for using Smart Square Library")
        exit()
    else:
        print("Invalid Choice!!")
