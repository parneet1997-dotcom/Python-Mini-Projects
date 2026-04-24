from utils import balance, transactions

def deposit():
    amt = int(input("Enter amount to deposit: "))
    balance["amount"] += amt
    transactions.append(f"Deposited: {amt}")
    print("Amount deposited successfully")