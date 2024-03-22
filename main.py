from src.auth.config import auth_backend, fastapi_users
from src.schemas.user import UserCreate, UserRead
from fastapi import FastAPI
from src.endpoints.wishes import router as wish_router

app = FastAPI(title="Wisher Grant")


app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"])
app.include_router(wish_router)
