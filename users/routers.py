from fastapi import APIRouter, HTTPException, status, Response
from users.models import User

router = APIRouter()
users = [
    User(
        id=1,
        email="josemak10@gmail.com"
    )
]


def get_permission(user_id: int):
    if user_id and user_id in [row.id for row in users]:
        return True
    return False


def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return


def get_users():
    return users


@router.post("/users/{user_id}")
def create_user(user_id: int, user: User, response: Response):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    users.append(user)
    response.status_code = status.HTTP_201_CREATED
    return {
        'detail': users
    }


@router.put("/users/{id}/{user_id}")
def update_user(id: int, user: User, user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    for item in users:
        if item.id == id:
            item.email = user.email
    return {
        'detail': users
    }


@router.delete("/users/{id}/{user_id}")
def delete_user(id: int, user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    for item in users:
        if item.id == id and id != 1:
            users.remove(item)
    return {
        'detail': users
    }


@router.get("/users/{user_id}")
def list_users(user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    return {
        'detail': users
    }
