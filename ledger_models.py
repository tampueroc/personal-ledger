from dateutil.parser import parse, ParserError
from pydantic import BaseModel, NegativeFloat, PositiveFloat, validator

class Transaction(BaseModel):
    date: str
    desc: str
    account_a: str
    value_a: PositiveFloat
    account_b: str
    value_b: NegativeFloat

    @validator("date")
    def valid_date(cls, v:str):
        parsed_date = parse(v, dayfirst=True)
        return parsed_date

    def __str__(self) -> str:
        """
        Returns Transaction as .ledger parsed entry
        """
        s = f"\n{self.date} {self.desc}\n"+ f"\t{self.account_a} {self.value_a}\n" + f"\t{self.account_b} {self.value_b}"
        return s


class Account(BaseModel):
    root:str = ""
    deep:int = 0
    account_name:str
    
    # @validator(account_name)
    # def parse_account_name(cls, v):
    #     cls.account_name = v.split(":")
    #     cls.root = cls.account_name[0]
    #     cls.deep = len(cls.account_name)
