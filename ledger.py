from ledger_models import Transaction


class Ledger:
    def __init__(self) -> None:
        """
        Initialize ledger file record
        """
        self._ledger = open("ledger_book.ledger", "a")

    def add_transaction(self, transaction_data: Transaction):
        # Write into .ledger
        self._ledger.write(transaction_data.__str__())
        