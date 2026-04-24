from deposit import deposit
from withdraw import withdraw
from balance import check_balance
from statement import show_statement

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        show_statement()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")