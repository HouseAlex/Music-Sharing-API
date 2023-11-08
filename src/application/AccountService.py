from dataclasses import dataclass

from src.domain.Account import Account
from src.domain.repositories.IAccount import IAccount

@dataclass
class AccountService:
    account: IAccount

    def AddEntry(self, content: str) -> str:
        #placeholder
        entry = Account.AddAccount(content)
        self.account.add(entry)
        return entry.id
    
    def get(self, id: str) -> Account:
        return self.account.get(id)
    