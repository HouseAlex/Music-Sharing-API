from dataclasses import dataclass
import datetime
from pydantic import BaseModel


class Account(BaseModel):
    accountName: str
    createdOn: datetime.datetime
    id: str

class AddAccount(BaseModel):
    accountName: str
