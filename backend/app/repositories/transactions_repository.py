from sqlmodel import Session, select

from app.models.transactions_model import Transaction

class TransactionRepository:

    def __init__(self, session: Session):

        self.session = session

    def create_transaction(self, transaction: Transaction):

        self.session.add(transaction)

        self.session.commit()

        self.session.refresh(transaction)

        return transaction
    
    def get_by_id(self, transaction_id : int):

        stmt = select(Transaction).where(
            Transaction.id == transaction_id
        )

        return self.session.exec(stmt).first()