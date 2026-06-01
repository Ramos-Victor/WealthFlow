from fastapi import HTTPException

from app.models.categoria_model import Categoria

from app.repositories.categoria_repository import CategoriaRepository

from app.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaUpdate
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
    
    def get_all_by_user(
        self,
        user_id: int
    ):
        categorias = self.repository.get_all_by_user(user_id)

        if not categorias:
            raise HTTPException(
                status_code=404,
                detail="Não foi encontrada nenhuma categoria"
            )
        
        return categorias
    
    def update_categoria(
        self,
        data: CategoriaUpdate,
        categoria_id = int
    ):
        
        categoria = self.repository.get_by_id(categoria_id)

        if not categoria:
            raise ValueError("Categoria não encontrada")
        
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(categoria, field, value)

        return self.repository.update_categoria(categoria)
    
    def delete_categoria(
        self,
        categoria_id
    ):
        
        categoria = self.repository.get_by_id(categoria_id)

        if not categoria:
            raise HTTPException(
                status_code=404,
                detail="Categoria não encontrada"
            )
        
        self.repository.delete_categoria(categoria)

        return{
            "message": "Categoria deletada com sucesso!"
        }
        
