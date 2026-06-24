from book import Book
from library import Library
from user import User
from borrow import Borrow

library = Library()
library.load_books()
user1 = User("Kamal")

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Show books")
    print("3. Borrow Book")
    print("4. Show user books")
    print("5. Exit")

    try:
      choice = int(input("Enter choice: "))
    except ValueError:
         print("Invalid input, Please enter a number .")
         continue

    #1. ADD BOOK
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        book = Book(title, author)
        library.add_book(book)
        print("Book added successfully!")
        library.save_books()

    # 2.SHOW BOOKS
    elif choice == 2:
     library.show_books()

    # 3.BORROW BOOK
    elif choice == 3:
       title = input ("Enter book title to borrow: ")
       for book in library.books:
          if book.title == title:
             borrow = Borrow(user1, book)
             user1.borrow_book(book)
             print("Book Borrowed!")
             break
          else:
             print("Book not found!")

    # 4. SHOW USER BOOKS
    elif choice == 4:
       user1.show_user_books()

    # 5. EXIT
    elif choice == 5:
     print("Exiting system...")
     break

    else:
     print("Invalid choice!")
          