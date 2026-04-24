from utils import books

def show():
    print("\nAvailable Books:")

    for book in books:
        if books[book]["available"]:
            print(book)