from typing import Optional

from enum import StrEnum
from sqlmodel import SQLModel, Field

class typeCategoria(StrEnum):
    RECEITAS = "receitas",
    DESPESAS = "despesas"

class Categoria(SQLModel, table=True):

    __tablename__ = "categorias"

    id: Optional[int] = Field(default=None,primary_key=True)

    name: str

    type: typeCategoria

    color: str

    user_id: int = Field(foreign_key="users.id")