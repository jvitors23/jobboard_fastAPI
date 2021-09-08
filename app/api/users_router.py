from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.users import UserCreate, UserResponse
from db.session import get_db_session
from db.crud.users import create_new_user, retrieve_user_by_id


router = APIRouter()


@router.post('/', response_model=UserResponse,
             status_code=status.HTTP_201_CREATED,
             response_description='User created!')
def create_user(user: UserCreate, session: Session = Depends(get_db_session)):
    """User creation endpoint"""
    user = create_new_user(user, session)
    return user


@router.get('/{user_id}', response_model=UserResponse,
            status_code=status.HTTP_200_OK,
            responses={
                 status.HTTP_404_NOT_FOUND: {'description': 'User not found!'},
             })
def retrieve_user(user_id: int, session: Session = Depends(get_db_session)):
    user = retrieve_user_by_id(user_id=user_id, session=session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
