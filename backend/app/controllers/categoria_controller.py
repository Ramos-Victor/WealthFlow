from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.categoria_repository import CategoriaRepository

from app.services.categoria_service import CategoriaService

from app.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse,
    CategoriaUpdate
)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

@router.post(
    "/",
    response_model= CategoriaResponse,
    status_code=201
)
def create_categoria(
    data: CategoriaCreate,
    session: Session = Depends(get_session)
):
    
    repository = CategoriaRepository(session)

    service = CategoriaService(repository)

    return service.create_categoria(data)

@router.get(
    "/{user_id}",
    response_model=list[CategoriaResponse]
)
def get_all_by_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    repository = CategoriaRepository(session)

    service = CategoriaService(repository)

    return service.get_all_by_user(user_id)

@router.put("/{categoria_id}")
def categoria_update(
    categoria_id: int,
    data: CategoriaUpdate,
    session: Session = Depends(get_session)
):
    
    repository = CategoriaRepository(session)

    service = CategoriaService(repository)

    return service.update_categoria(data, categoria_id)

@router.delete("/{categoria_id}")
def categoria_delete(
    categoria_id: int,
    session: Session = Depends(get_session)
):
    
    repository = CategoriaRepository(session)

    service = CategoriaService(repository)

    return service.delete_categoria(categoria_id)