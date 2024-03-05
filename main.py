from fastapi_users import FastAPIUsers
from src.database import User
from src.auth.manager import get_user_manager
from src.auth.config import auth_backend
from fastapi import FastAPI
from src.schemas.user import UserCreate, UserRead, UserUpdate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager, [auth_backend]
)

app = FastAPI(title="Wisher Grant")
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"])


