from fastapi import HTTPException

from app.models.categoria_model import Categoria

from app.repositories.categoria_repository import CategoriaRepository

from app.schemas.categoria_schema import (
    CategoriaCreate
)


class CategoriaService:

    def __init__(
        self,
        repository: CategoriaRepository
    ):
        
        self.repository = repository

    def create_categoria(
        self,
        data: CategoriaCreate
    ):
        categoria = Categoria(
            name = data.name,
            type = data.type,
            color = data.color,
            user_id = data.user_id
        )
        
        return self.repository.create(categoria)