from utils import balance, transactions

def withdraw():
    amt = int(input("Enter amount to withdraw: "))

    if amt <= balance["amount"]:
        balance["amount"] -= amt
        transactions.append(f"Withdrawn: {amt}")
        print("Please collect your cash")
    else:
        print("Insufficient balance")