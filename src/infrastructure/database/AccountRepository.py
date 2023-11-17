from dataclasses import dataclass
from pathlib import Path
import pickle

from domain.Account import Account
from domain.repositories.IAccount import IAccount


class AccountNotFound(Exception):
    pass

@dataclass
class AccountRepository(IAccount):
    
    def get(self, id: str) -> Account:
        """
        try:
            entry: Account
            with open(Path(self.storageDir) / id, mode="rb") as entryFile:
                entry = pickle.load(entryFile)
            return entry
        except Exception:
            raise AccountNotFound()
        """
        raise AccountNotFound()

    def add(self, entry: Account) -> None:
        """
        
        with open(Path(self.storageDir) / id, mode="rb") as entryFile:
            pickle.dump(entry, entryFile)
        """