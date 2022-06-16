import datetime

from ledger import Ledger


def add_transaction_cli():
    print("$ Add Transaction record")
    date = input("$ date (dd-mm-yyyy)\n") 
    date = datetime.date.today().strftime("%d-%m-%Y") if date=="" else date

    desc = input("$ description\n")

    account_a, value_a = input("$ entry a (<account> <value>)\n").split()
    account_b, value_b = input("$ entry b (<account> <value>)\n").split()

    Ledger().add_transaction(date=date, desc=desc, account_a=account_a, value_a=value_a, account_b=account_b, value_b=value_b)