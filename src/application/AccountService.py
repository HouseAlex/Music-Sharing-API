from dataclasses import dataclass

from src.domain.Account import Account
from src.domain.repositories.IAccount import IAccount

@dataclass
class AccountService:
    IAccount: IAccount

    def addEntry(self, content: str) -> str:
        #placeholder
        entry = Account.AddAccount(content=content)
        return 
    