from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users import FastAPIUsers
from src.database import User
from src.auth.manager import get_user_manager
from src.config import SECRET_AUTH


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(SECRET_AUTH, lifetime_seconds=3600)


cookie_transport = CookieTransport(cookie_max_age=3600)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
auth_backend = AuthenticationBackend(name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager, [auth_backend]
)

current_user = fastapi_users.current_user()
