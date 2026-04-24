import random
from utils import balance

def play_game():
    user = int(input("Enter a number (1-6): "))
    computer = random.randint(1, 6)

    print("Computer rolled:", computer)

    if user == computer:
        print("🎉 You WIN!")
        balance["wins"] += 1
    else:
        print("😢 You lose!")
        balance["losses"] += 1