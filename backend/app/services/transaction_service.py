from fastapi import HTTPException, status
from sqlmodel import Session

from app.models.transactions_model import Transaction

from app.repositories.transactions_repository import TransactionRepository
from app.repositories.account_repository import AccountRepository

from app.schemas.transaction_schema import(
    TransactionCreate
)

class TransactionService:

    def __init__(
        self,
        session: Session,
        repository: TransactionRepository,
        account_repository: AccountRepository
    ):
        self.session = session
        self.repository = repository
        self.account_repository = account_repository

    def create_transaction(
        self,
        data: TransactionCreate
    ):
        account = self.account_repository.get_by_id_for_update(data.account_id)

        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conta não encontrada"
            )
        
        if data.type == "despesa":
            if account.balance < data.amount:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                detail="Saldo insuficiente para realizar esta transação!"
                )
            
            account.balance -= data.amount
        else:
            account.balance += data.amount

        self.session.add(account)
        
        transaction = Transaction(
            description= data.description,
            amount = data.amount,
            transaction_date= data.transaction_date,
            type = data.type,
            user_id = data.user_id,
            account_id = data.account_id,
            categoria_id = data.categoria_id
        )

        return self.repository.create_transaction(transaction)