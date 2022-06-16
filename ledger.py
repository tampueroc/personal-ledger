from ledger_models import Transaction


class Ledger:
    def __init__(self) -> None:
        """
        Initialize ledger file record
        """
        self._ledger = open("ledger_book.ledger", "w")

    def add_transaction(self, date, desc=None, account_a=None, value_a=None, account_b=None, value_b=None):
        # Create Transaction Dataclass
        data  = Transaction(date=date, desc=desc, account_a=account_a, value_a=value_a, account_b=account_b, value_b=value_b)

        # Write into .ledger
        self._ledger.write(data.__str__())
        