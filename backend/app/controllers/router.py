from fastapi import APIRouter

from app.controllers.user_controller import router as user_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.account_controller import router as account_router

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(user_router)
api_router.include_router(auth_router)
api_router.include_router(categoria_router)
api_router.include_router(account_router)