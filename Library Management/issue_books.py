from utils import books, issued_books

def issue():
    book = input("Enter book name: ").upper()

    if book in books and books[book]["available"]:
        name = input("Enter student name: ")
        days = int(input("Enter number of days: "))

        books[book]["available"] = False

        issued_books[book] = {
            "name": name,
            "days": days
        }

        print("Book issued successfully")

    else:
        print("Book not available")