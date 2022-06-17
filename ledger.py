import re
from ledger_models import Account, Transaction


class Ledger:
    def __init__(self) -> None:
        """
        Initialize ledger file record
        """
        self._ledger_file = ".ledger"
        try:
            self.valid_account_config()
        except IOError:
            self._ledger = open(self._ledger_file, "w")
            init_config = ";Config\n" + ";;Accounts\n" + "\tExpenses\n" + "\tAssets\n" + "\tIncome\n" + "\tLiabilities\n" + "\tEquity\n" 
            self._ledger.write(init_config)

    def valid_account_config(self):
        with open(self._ledger_file) as ledger_file:
            for line in ledger_file:
                line = re.search(";;Accounts", line)
                if line:
                    return True
            raise IOError("No Account config found")
                
    def add_transaction(self, transaction_data: Transaction):
        self._ledger = open(self._ledger_file, "a")
        # Write into .ledger
        self._ledger.write(transaction_data.__str__())
    

        
        