from fastapi import APIRouter
from api import users_router


api_router = APIRouter()

api_router.include_router(users_router.router, prefix='/user', tags=['users'])
