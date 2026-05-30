from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.user_repository import UserRepository

from app.services.user_service import UserService

from app.schemas.user_schema import (
    UserCreate,
    UserResponse
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_user(
    data: UserCreate,
    session: Session = Depends(get_session)
):

    repository = UserRepository(session)

    service = UserService(repository)

    return service.create_user(data)