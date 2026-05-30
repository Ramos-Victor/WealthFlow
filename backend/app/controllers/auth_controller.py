from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session

from app.repositories.user_repository import UserRepository

from app.services.auth_service import AuthService

from app.schemas.auth_schema import (
    LoginRequest,
    TokenResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: LoginRequest,
    session: Session = Depends(get_session)
):

    repository = UserRepository(session)

    service = AuthService(repository)

    return service.login(
        data.email,
        data.password
    )