from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.transactions_repository import TransactionRepository
from app.repositories.account_repository import AccountRepository

from app.services.transaction_service import TransactionService

from app.schemas.transaction_schema import (
    TransactionCreate,
    TransactionResponse
)

router = APIRouter(
    prefix="/transaction",
    tags=["Transações"]
)

@router.post(
    "/",
    response_model = TransactionResponse,
    status_code=201
)
def create_transaction(
    data: TransactionCreate,
    session: Session = Depends(get_session)
):
    
    repository = TransactionRepository(session)
    account_repository = AccountRepository(session)

    service = TransactionService(session,repository, account_repository)

    return service.create_transaction(data)