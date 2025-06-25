class Book():
    def __init__(self, name, author, price, id, charge):
        self.name = name
        self.author = author
        self.__price = price
        self.id = id
        self.charge = charge

    def get_price(self):
        return self.__price
class Library():
    def __init__(self):
        self.bookShelf = []

    def add_book(self, book, copies):
        for i, (b, available) in enumerate(self.bookShelf):
            if b.name == book.name:
                self.bookShelf[i][1] += copies
                return
        self.bookShelf.append([book, copies])
        print(f"{copies} copies of {book.name} added to the library")

    def remove_book(self, book, copies):
        for i, (book1, available) in enumerate(self.bookShelf):
            if book1.name == book:
                if copies <= 0:
                    print("Invalid number of copies")
                elif copies > available:
                    print(f"Not enough copies of {book} available")
                else:
                    self.bookShelf[i][1] -= copies
                    print(f"{copies} copies of {book} removed from the library")
                return
        print(f"{book} not found in the library")

    # Admin & User Shared Function
    def view_available_books(self, password=""):
        if not self.bookShelf:
            print("No books available")
        else:
            for book, copies in self.bookShelf:
                print(f"{book.name} by {book.author} | Copies: {copies}")

    def borrow_book(self, book_name, copies):
        for i, (book, available) in enumerate(self.bookShelf):
            if book.name == book_name:
                if available >= copies:
                    self.bookShelf[i][1] -= copies
                    print(f"You have borrowed {copies} copies of {book_name}")
                else:
                    print("Not enough copies available")
                return
        print("Book not found in the library")

    def return_book(self, book_name, copies):
        for i, (book, available) in enumerate(self.bookShelf):
            if book.name == book_name:
                self.bookShelf[i][1] += copies
                print(f"You have returned {copies} copies of {book_name}")
                return
        print("This book is not in the library")


def main():
    Library1 = Library()
    Money = 0
    User = input("Choose the Option:\n1.Admin\n2.User: ")
    if User == "1":
        original = "Vijay@2654"
        password = input("Enter the Admin Password: ")
        if password == original:
            choice = 1
            while choice != 0:
                print("1.Add Book\n2.Remove Book\n3.View Available Books\n4.View Cost of a specific Book\n5.Change the System for User\n0.Exit")
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        book1 = Book(input("Enter Book Name: "), input("Enter Author Name: "),
                                     float(input("Enter Price: ")), int(input("Enter ID: ")),
                                     float(input("Enter Charge: ")))
                        copiee = int(input("Enter Number of Copies: "))
                        Library1.add_book(book1, copiee)
                    case 2:
                        code = input("Enter Book Name: ")
                        copiee = int(input("Enter Number of Copies: "))
                        Library1.remove_book(code, copiee)
                    case 3:
                        Library1.view_available_books(password)
                    case 4:
                        book_name = input("Enter Book Name to view cost: ")
                        for book, _ in Library1.bookShelf:
                            if book.name == book_name:
                                print(f"Price of {book_name} is {book.get_price()}")
                                break
                        else:
                            print("Book not found")
                    case 5:
                        print("Changing the system to User mode")
                        User = "2"
                        break
                    case 0:
                        print("Thank you for using the Library Management System")
                if choice == 0:
                    break
        else:
            print("Incorrect password")

    elif User == "2":
        name = input("Enter your name: ")
        print(f"Welcome {name} to the Library Management System")
        print("1.Borrow Book\n2.Return Book\n3.View Available Books\n4.Changing the System for Admin\n0.Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                name = input("Enter Book Name to borrow: ")
                copies = int(input("Enter Number of Copies to borrow: "))
                Library1.borrow_book(name, copies)
            case 2:
                name = input("Enter Book Name to return: ")
                copies = int(input("Enter Number of Copies to return: "))
                for book, _ in Library1.bookShelf:
                    if book.name == name:
                        Money += copies * book.charge
                        break
                print(f"You have to pay {Money} for borrowing {copies} copies of {name}")
                Library1.return_book(name, copies)
            case 3:
                Library1.view_available_books("")
            case 4:
                print("Changing the system to Admin mode")
                User = "1"
                main()  # Restart the main function for Admin mode
            case 0:
                print("Thank you for using the Library Management System")
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
