from fastapi import APIRouter
from api import users_router
from api import jobs_router


api_router = APIRouter()

api_router.include_router(users_router.router, prefix='/user', tags=['users'])
api_router.include_router(jobs_router.router, prefix='/job', tags=['jobs'])
