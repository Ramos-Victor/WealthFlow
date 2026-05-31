from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.categoria_repository import CategoriaRepository

from app.services.categoria_service import CategoriaService

from app.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse
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