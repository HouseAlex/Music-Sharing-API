import datetime
from pydantic import BaseModel

class Account(BaseModel):
    accountName: str
    createdOn: datetime
    id: str

class AddAccount(BaseModel):
    accountName: str
