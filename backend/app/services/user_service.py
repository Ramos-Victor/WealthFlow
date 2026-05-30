from fastapi import HTTPException

from app.models.user_model import User

from app.repositories.user_repository import UserRepository

from app.schemas.user_schema import (
    UserCreate,
    )

from app.core.security import hash_password


class UserService:

    def __init__(
        self,
        repository: UserRepository
    ):

        self.repository = repository


    def create_user(
        self,
        data: UserCreate
    ):

        user_exists = self.repository.get_by_email(
            data.email
        )

        if user_exists:

            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        hashed_password = hash_password(
            data.password
        )

        user = User(
            name=data.name,
            email=data.email,
            password=hashed_password
        )

        return self.repository.create(user)
    
    def get_by_email(
            self,
            email: str
    ):
        user = self.repository.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Não foi encontrado nenhum perfil com este email"
            )
        
        return user