from utils import transactions

def show_statement():
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        print("\nTransaction History:")
        for t in transactions:
            print(t)