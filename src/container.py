from dependency_injector import providers, containers

from application.AccountService import AccountService
from infrastructure.database.AccountRepository import AccountRepository

class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    accountRepository = providers.Singleton(
        AccountRepository
    )

    accountService = providers.Factory(AccountService, accountRepository)