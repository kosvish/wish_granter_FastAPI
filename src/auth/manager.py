from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.database import User, get_user_db
from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ) -> None:
        print(f"Пользователь {user.email}, зарегестрировался")

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f"Пользователь {user.email}, забыл свой пароль, токен сброса: {token}")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f"Пользователь {user.email}, запросил верефикацию. Токен: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
