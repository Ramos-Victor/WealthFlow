from pydantic import BaseModel
from enum import Enum
from decimal import Decimal
from datetime import date, datetime


class typeTransaction(str, Enum):
    RECEITA = "receita",
    DESPESA = "despesa"

class TransactionCreate(BaseModel):

    description: str
    amount: Decimal
    transaction_date: date
    type: typeTransaction
    user_id: int
    account_id: int
    categoria_id: int

class TransactionResponse(BaseModel):

    description: str
    amount: Decimal
    transaction_date: date
    created_at: datetime
    type: typeTransaction
    user_id: int
    account_id: int
    categoria_id: int

