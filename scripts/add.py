import datetime
from lib2to3.pgen2.parse import ParseError
from dateutil.parser import ParserError
from ledger import Ledger
from ledger_models import Account, Transaction

# TODO Unknown Parse Error when Entry has one value (or there isn't any whitespace)
def add_transaction_cli():
    try:
        print("$ Add Transaction record")
        cli_input = input("$ date (dd-mm-yyyy)\n") 
        date = datetime.date.today().strftime("%d-%m-%Y") if cli_input == "" else cli_input

        cli_input = input("$ description\n")
        desc = cli_input

        cli_input = input("$ First Entry (<account> <value>)\n")
        account_a, value_a = cli_input.split()
        cli_input = input("$ Second Entry (<account> <value>)\n")
        account_b, value_b = cli_input.split()

        transaction_data = Transaction( date=date, desc=desc, account_a=account_a, value_a=value_a, account_b=account_b, value_b=value_b)
        Ledger().add_transaction( transaction_data=transaction_data)
    except ValueError:
        add_transaction_cli()
    except ParseError:
        add_transaction_cli()

def add_account_cli():
    print("$ Add Account")
    cli_command = input(" entry account (with hierarchy)")
    account_data = Account(account_name=cli_command)
    Ledger().add_account(account_data= account_data)