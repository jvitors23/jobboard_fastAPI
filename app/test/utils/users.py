from sqlalchemy.orm import Session
import random
import string
from schemas.users import UserCreate
from db.crud.users import create_new_user


def random_lowercase_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_owner(session: Session):
    email = f'{random_lowercase_string()}@{random_lowercase_string()}.com'
    password = random_lowercase_string()
    user_schema = UserCreate(email=email, username=email, password=password)
    user = create_new_user(user=user_schema, session=session)
    return user
