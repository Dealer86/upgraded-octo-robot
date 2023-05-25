from fastapi import APIRouter

from API_which_can_save_users.api.models import UserInfo, UserAdd, UserUpdate
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


@users_router.get("{user_id}", response_model= UserInfo)
def get_by_id(user_id: int):
    return repo.get_by_id(user_id)

@users_router.put("{user_id}", response_model=UserInfo)
def update(user_id: int, user: UserUpdate):
    repo.update(user_id, user.name)
    return repo.get_by_id(user_id)

@users_router.delete("")
def delete_user(id: int):
    repo.delete(id)
