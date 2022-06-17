from ledger import Ledger
from scripts.add import add_transaction_cli


if __name__ == "__main__":
    ledger = Ledger().valid_account_config()
    command = input(">>> ")
    while(command!="exit"):
        if command == "addt":
            add_transaction_cli()
        else:
            print("Unknown command")
        command = input(">>> ")
        


    