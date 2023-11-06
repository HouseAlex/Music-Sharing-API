from dataclasses import dataclass
from datetime import datetime

@dataclass
class Account:
    accountName: str
    createdOn: datetime
    id: str

    @classmethod
    def AddAccount(cls, content: str) -> "Account":
        return cls(id=str(uuid.uuid4()), createdOn=datetime.utcnow(), AccountName= content)
    