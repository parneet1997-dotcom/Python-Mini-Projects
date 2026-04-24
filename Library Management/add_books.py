from utils import books

def add():
    book = input("Enter book name to add: ").upper()
    books[book] = {"available": True}
    print("Book added successfully")