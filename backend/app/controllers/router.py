from fastapi import APIRouter

from app.controllers.user_controller import router as user_router

from app.controllers.auth_controller import router as auth_router

from app.controllers.categoria_controller import router as categoria_router

from app.controllers.account_controller import router as account_router

from app.controllers.transaction_controller import router as transaction_router


api_router = APIRouter(
    prefix="/api"
)

routers = [
    user_router,
    auth_router,
    categoria_router,
    account_router,
    transaction_router
]

for router in routers:
    api_router.include_router(router)
