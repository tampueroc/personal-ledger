from dateutil.parser import parse, ParserError
from pydantic import BaseModel, validator

class Transaction(BaseModel):
    date: str
    desc: str
    account_a: str
    value_a: str
    account_b: str
    value_b: str

    @validator("date")
    def valid_date(cls, v:str):
        try:
            parsed_date = parse(v, dayfirst=True)
            return parsed_date
        except ParserError as e:
            print(e)

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
    root:str = ""
    deep:int = 0
    account_name:str
    
    # @validator(account_name)
    # def parse_account_name(cls, v):
    #     cls.account_name = v.split(":")
    #     cls.root = cls.account_name[0]
    #     cls.deep = len(cls.account_name)
