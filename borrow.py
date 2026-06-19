class Borrow:
    def __init__(self, user, book):
        self.user = user
        self.book = book

    def show_borrow_info(self):
        print(self.user.name, "borrowed", self.book.book)
