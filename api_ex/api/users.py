
from fastapi import APIRouter

from api_ex.api.models import UserInfo, UserAdd
from api_ex.domain.factory import UserFactory
from api_ex.domain.repo import UserRepo

users_router = APIRouter(prefix="/users")
user_repo = UserRepo()


@users_router.get('', response_model=list[UserInfo])
def get_all_users():
    return user_repo.get_all_users()


@users_router.get("{username}", response_model=UserInfo)
def get_by_username(username: str):
    return user_repo.get_by_username(username)


@users_router.post('', response_model=UserInfo)
def add_user(user: UserAdd):
    new_user = UserFactory.create_user(user.username, user.email)
    print(new_user.email, new_user.username)
    user_repo.add_user(new_user)
    return new_user


@users_router.patch("{username}", response_model=UserInfo)
def update_user(username, new_username: str):
    user_repo.update_user(username, new_username)
    user = user_repo.get_by_username(new_username)
    return user


@users_router.delete("")
def delete_user(username: str):
    try:
        user_repo.delete_user(username)
        return {"status": "ok"}
    except Exception as e:
        return str(e)



