from fastapi import HTTPException

from app.models.account_model import Account

from app.repositories.account_repository import AccountRepository

from app.schemas.account_schema import (
    AccountCreate,
    AccountUpdate
)


class AccountService:

    def __init__(
        self,
        repository: AccountRepository
    ):
        self.repository = repository


    def create_account(
        self,
        data: AccountCreate
    ):
        account = Account(
            name = data.name,
            balance = data.balance,
            user_id = data.user_id
        )

        return self.repository.create_account(account)
    
    def get_all_accounts(
        self,
        user_id: int
    ):
        accounts = self.repository.get_all_account(user_id)

        if not accounts:
            raise HTTPException(
                status_code=404,
                detail="Não foi encontrada nenhuma conta"
            )
        
        return accounts
    
    def update_account(
        self,
        data: AccountUpdate,
        account_id = int
    ):
        
        account = self.repository.get_by_id(account_id)

        if not account:
            raise ValueError("Conta não encontrada")
        
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(account, field, value)

        return self.repository.update_account(account)
    
    def delete_account(self, account_id):

        account = self.repository.get_by_id(account_id)

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Conta não encontrada"
            )
        
        self.repository.delete_account(account)

        return{
            "message": "Conta deletada com sucesso!"
        }