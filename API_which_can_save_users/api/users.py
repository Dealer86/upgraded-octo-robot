from fastapi import APIRouter

from API_which_can_save_users.api.models import UserInfo, UserAdd
from API_which_can_save_users.domain.repo import UserRepository
from API_which_can_save_users.domain.user_factory import UserFactory

users_router = APIRouter(prefix="/users")
repo = UserRepository()


@users_router.post("", response_model=UserInfo)
def add_user(user: UserAdd):
    new_user = UserFactory.create(user.name, user.email)
    repo.add(new_user)
    # return UserInfo(name=new_user.name, email=new_user.email)
    return new_user


@users_router.get("", response_model=list[UserInfo])
def get_users():
    users = repo.get_all()
    # return [UserInfo(name=u.name, email=u.email, id=u.id) for u in users]
    return users


@users_router.delete("")
def delete_user(id: int):
    repo.delete(id)
