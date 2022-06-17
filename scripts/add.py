import datetime
from lib2to3.pgen2.parse import ParseError

from ledger import Ledger
from ledger_models import Transaction
from scripts.errors import DateInputError


def add_transaction_cli():
    try:
        print("$ Add Transaction record")
        cli_input = input("$ date (dd-mm-yyyy)\n") 
        date = datetime.date.today().strftime("%d-%m-%Y") if cli_input == "" else cli_input

        cli_input = input("$ description\n")
        desc = cli_input

        cli_input = input("$ entry a (<account> <value>)\n")
        account_a, value_a = cli_input.split()
        cli_input = input("$ entry a (<account> <value>)\n")
        account_b, value_b = cli_input.split()

        transaction_data = Transaction( date=date, desc=desc, account_a=account_a, value_a=value_a, account_b=account_b, value_b=value_b)
        Ledger().add_transaction( transaction_data=transaction_data)
    except ValueError as e:
        add_transaction_cli()