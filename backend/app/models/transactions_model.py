from typing import Optional 

from decimal import Decimal
from datetime import date, datetime
from enum import StrEnum
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func

class typeTransaction(StrEnum):
    RECEITA = "receita",
    DESPESA = "despesa"

class Transaction(SQLModel, table=True):

    __tablename__ = "transactions"

    id: Optional[int] = Field(default=None, primary_key=True)

    description: str = Field(max_length=255)

    amount: Decimal = Field(default=0, max_digits=12, decimal_places=2)

    transaction_date: date

    type: typeTransaction

    created_at: datetime = Field(sa_column=Column(DateTime, nullable=False, server_default=func.now()))

    user_id: int = Field(foreign_key="users.id")

    account_id: int = Field(foreign_key="account.id")

    categoria_id: int = Field(foreign_key="categorias.id")