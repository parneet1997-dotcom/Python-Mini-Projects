from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_book

while True:
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        show()

    elif choice == 3:
        issue()

    elif choice == 4:
        return_book()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
