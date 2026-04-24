from utils import books, issued_books

def return_book():
    book = input("Enter book name: ").upper()

    if book in issued_books:
        actual_days = int(input("Enter days taken: "))
        allowed_days = issued_books[book]["days"]

        extra_days = actual_days - allowed_days
        fine = 0

        if extra_days > 0:
            if extra_days <= 7:
                fine = extra_days * 10
            elif extra_days <= 14:
                fine = extra_days * 20
            else:
                fine = extra_days * 60

        print("Fine:", fine)

        books[book]["available"] = True
        del issued_books[book]

        print("Book returned successfully")

    else:
        print("This book was not issued")