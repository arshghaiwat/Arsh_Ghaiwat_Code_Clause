class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nAvailability: {availability}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book is None:
            return "Book not found."
        if not book.available:
            return "Book is already borrowed."
        book.available = False
        return "Book borrowed successfully."

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            return "Book not found."
        if book.available:
            return "Book is already returned."
        book.available = True
        return "Book returned successfully."


def display_menu():
    print("\n========= Library Management System =========")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")


library = Library()

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        book = Book(title, author)
        library.add_book(book)
        print("Book added successfully.")

    elif choice == '2':
        title = input("Enter the book title to borrow: ")
        result = library.borrow_book(title)
        print(result)

    elif choice == '3':
        title = input("Enter the book title to return: ")
        result = library.return_book(title)
        print(result)

    elif choice == '4':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")