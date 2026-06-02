from sqlmodel import Session, select

from app.models.account_model import Account


class AccountRepository:

    def __init__(self, session: Session):

        self.session = session

    def create_account(self, account: Account):

        self.session.add(account)

        self.session.commit()

        self.session.refresh(account)

        return account
    
    def get_by_id(self, account_id : int):

        stmt = select(Account).where(
            Account.id == account_id
        )

        return self.session.exec(stmt).first()
    
    def get_all_account(self, user_id : int):

        stmt = select(Account).where(
            Account.user_id == user_id
        )

        return self.session.exec(stmt).all()
    
    def get_by_id_for_update(self, account_id : int):
        stmt = select(Account).where(Account.id == account_id).with_for_update()

        return self.session.exec(stmt).first()
    
    def update_account(self, account: Account):

        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)

        return account
    
    def delete_account(self, account: Account):

        self.session.delete(account)

        self.session.commit()