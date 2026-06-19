from book import Book
from library import Library
from user import User

lib = Library()

user1 = User("Kamal")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book ("The A1chemist", "Pualo Coelho")

lib.add_book(book1)
lib.add_book(book2)

user1.borrow_book(book1)

lib.show_books()
user1.show_user_books()