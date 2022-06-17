from pydantic import BaseModel, validator

class Transaction(BaseModel):
    date: str
    desc: str
    account_a: str
    value_a: str
    account_b: str
    value_b: str

    @validator("value_a", "value_b")
    def is_value_numeric(cls, v:str):
        if not v.isnumeric():
            raise ValueError(f"{v} not numeric value")
        return v

    def __str__(self) -> str:
        """
        Returns Transaction as .ledger parsed entry
        """
        s = f"\n{self.date} {self.desc}\n"+ f"\t{self.account_a} {self.value_a}\n" + f"\t{self.account_b} {self.value_b}"
        return s


class Account(BaseModel):
    parent:str
    account_name:str


    @validator(parent)
    def valid_parent(cls, v):
        if v not in ["Expenses", "Assets", "Income", "Liabilities", "Equitiy"] 