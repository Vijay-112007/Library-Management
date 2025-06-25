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

