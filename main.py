from ledger import Ledger
from scripts.add import add_transaction_cli


if __name__ == "__main__":
    ledger = Ledger()
    command = input(">>> ")
    while(command!="exit"):
        if command == "add":
            add_transaction_cli()
        command = input(">>> ")
        


    