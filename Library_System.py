class Library:

    def __init__(self, listofBooks):
        self.books=listofBooks

    def displayAvailableBooks(self):
     print("These Books are present in Library right Now: ")
     for book in self.books:
        print("\t"+book)
     print("\n")

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f'''    +++++ This Book has been issued - {bookName} +++++    ''')
            print("\n")
            self.books.remove(bookName)
            return True

        else:
            print('''    XXXX Book has already been issued XXXX    ''')
            print("\n")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("    ----- Thank You for returning Book -----    ")
        print("\n")

class Students:

    def requestBook(self):
        self.book= input("Which Book Do You Want to Borrow: ")
        return self.book 

    def returnBook(self):
        self.book= input("Which Book Do You Want to Return: ")
        return self.book 
     


if __name__=="__main__":
    clgLib =Library(["Java", "Let Us C", "Let Us c++","Django"])
    
    students = Students()


    while(True):
        print('''========= Hello, Welcome to the Library ========= 

        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        
        ''')

        a=int(input("Enter your choice : "))
        print("\n ")
        if a==1:
            clgLib.displayAvailableBooks()
        elif a==2:
            clgLib.borrowBook(students.requestBook())
        elif a==3:
            clgLib.returnBook(students.returnBook())
        elif a==4:
            print("Thank You For Choosing Us")
            exit()
        else:
            print("(Please Enter a Number from the Menu)")
            print("\n \n")