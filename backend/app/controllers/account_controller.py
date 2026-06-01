from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.account_repository import AccountRepository

from app.services.account_service import AccountService

from app.schemas.account_schema import (
    AccountCreate,
    AccountResponse,
    AccountUpdate
)

router = APIRouter(
    prefix="/account",
    tags=["Account"]
)

@router.post(
    "/",
    response_model= AccountResponse,
    status_code=201
)
def create_account(
    data: AccountCreate,
    session: Session = Depends(get_session)
):
    
    repository = AccountRepository(session)

    service = AccountService(repository)

    return service.create_account(data)

@router.get(
    "/{user_id}",
    response_model=list[AccountResponse]    
)
def get_all_account(
    user_id: int,
    session: Session = Depends(get_session)
):
    repository = AccountRepository(session)

    service = AccountService(repository)

    return service.get_all_accounts(user_id)

@router.put("/{account_id}")
def account_update(
    account_id: int,
    data: AccountUpdate,
    session: Session = Depends(get_session)
):
    
    repository = AccountRepository(session)

    service = AccountService(repository)

    return service.update_account(data, account_id)

@router.delete("/{account_id}")
def account_delete(
    account_id: int,
    session: Session = Depends(get_session)
):
    
    repository = AccountRepository(session)

    service = AccountService(repository)

    return service.delete_account(account_id)