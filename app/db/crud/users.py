from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, session: Session) -> User:
    user = User(username=user.username, email=user.email,
                password=Hasher.get_password_hash(user.password),
                is_active=True, is_superuser=False)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
