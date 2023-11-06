from dataclasses import dataclass
from datetime import datetime

@dataclass
class Account:
    accountName: str
    createdOn: datetime
    id: str

    