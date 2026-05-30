from typing import Optional

from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func


class User(SQLModel, table=True):

    __tablename__ = "users"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    name: str

    email: str = Field(
        unique=True,
        index=True
    )

    password: str

    created_at: datetime = Field(sa_column=Column(DateTime, nullable=False, server_default=func.now()))