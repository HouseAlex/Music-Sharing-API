from dataclasses import asdict
from dependency_injector.wiring import Provide
from fastapi import APIRouter
from application.AccountService import AccountService
from container import ApplicationContainer
from infrastructure.api.schemas.AccountSchemas import Account, AddAccount

accountService: AccountService = Provide[ApplicationContainer.accountService]

router = APIRouter(
    prefix="/Account",
    tags=["Account"],
    responses={404: {"description": "Not Found"}}
)

async def AddAccount(account: AddAccount) -> str:
    return accountService.AddEntry(account.accountName)

@router.get("/{id}")
async def GetAccount(id: str) -> Account:
    account = accountService.get(id)
    return Account(**asdict(account))

