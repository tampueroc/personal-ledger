from dataclasses import dataclass


@dataclass
class Transaction:
    date: str
    desc: str
    account_a: str
    value_a: str
    account_b: str
    value_b: str

    def __str__(self) -> str:
        """
        Returns Transaction as .ledger parsed entry
        """
        s = f"{self.date} {self.desc}\n"+ f"\t{self.account_a} {self.value_a}\n" + f"\t{self.account_b} {self.value_b}"
        return s