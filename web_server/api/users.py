from fastapi import APIRouter

from web_server.api.models import UserAdd, UserInfo
from web_server.domain.repo import UserRepository
from web_server.domain.user import User
from web_server.domain.user_factory import UserFactory

users_router = APIRouter(prefix="/users")
repo = UserRepository()


@users_router.post("", response_model=UserInfo)
def add_user(user: UserAdd):
    new_user = UserFactory.create(user.name, user.email)
    repo.add(new_user)
    return new_user


@users_router.get("", response_model=list[UserInfo])
def get_users():
    # return repo.get_all()
    user_list = repo.get_all()
    return [User(u.name, u.email) for u in user_list]

@users_router.delete("")
def delete_user(name: str):
    repo.delete(name)
