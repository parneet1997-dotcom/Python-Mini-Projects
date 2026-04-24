from game import play_game
from utils import balance

while True:
    print("\n===== DICE GAME =====")
    print("1. Play Game")
    print("2. Show Score")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        play_game()

    elif choice == 2:
        print("Wins:", balance["wins"])
        print("Losses:", balance["losses"])

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")