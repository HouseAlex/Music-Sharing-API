from dependency_injector import providers, containers

from src.application.AccountService import AccountService
from src.infrastructure.database.AccountRepository import AccountRepository

class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    accountRepository = providers.Singleton(
        AccountRepository, storage_dir=configuration.storage_dir
    )

    accountService = providers.Factory(AccountService, accountRepository)