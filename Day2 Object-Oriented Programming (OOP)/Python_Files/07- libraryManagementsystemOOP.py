class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book}" has been added to the library.')

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You have borrowed "{book}".')
        else:
            print(f'Sorry, "{book}" is not available.')

    def return_book(self, book):
        self.books.append(book)
        print(f'Thank you for returning "{book}".')

# Simulation
my_library = Library("City Library")

# Adding books
my_library.add_book("Python Programming")
my_library.add_book("Artificial Intelligence")

# Borrowing a book
my_library.borrow_book("Python Programming")

# Trying to borrow a book that's not available
my_library.borrow_book("Data Science")

# Returning a book
my_library.return_book("Python Programming")