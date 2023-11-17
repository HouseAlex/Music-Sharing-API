from abc import ABC
from domain.Account import Account

class IAccount(ABC):
    def get(self, id: str) -> Account:
        ...
    
    def add(self, entry: Account) -> None:
        ...