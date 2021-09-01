from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.session import get_db_session
from db.crud.users import create_new_user


router = APIRouter()


@router.post('/')
def create_user(user: UserCreate, session: Session = Depends(get_db_session)):
    """User creation endpoint"""
    user = create_new_user(user, session)
    return user
