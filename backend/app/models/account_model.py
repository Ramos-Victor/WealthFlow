from typing import Optional

from decimal import Decimal
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func

class Account(SQLModel, table=True):

    __tablename__ = "account"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    name: str

    balance: Decimal = Field(default=0, max_digits=12, decimal_places=2)

    created_at: datetime = Field(sa_column=Column(DateTime, nullable=False, server_default=func.now()))

    user_id: int = Field(foreign_key="users.id")