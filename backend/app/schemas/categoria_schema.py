from pydantic import BaseModel
from enum import Enum

class typeCategoria(str, Enum):
    RECEITAS = "receitas",
    DESPESAS = "despesas"

class CategoriaCreate(BaseModel):

    name: str
    type: typeCategoria
    color: str
    user_id: int

class CategoriaResponse(BaseModel):

    id: int
    name: str
    type: typeCategoria
    color: str
    user_id: int