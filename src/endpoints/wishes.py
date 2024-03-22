from fastapi import APIRouter, Depends, HTTPException
from src.schemas.wish import CreateWish
from src.models.models import Wish
from src.database import AsyncSession, get_async_session
from datetime import datetime
from src.database import User
from src.auth.config import current_user
from sqlalchemy.exc import IntegrityError, DBAPIError

router = APIRouter(prefix='/wishes', tags=['Wish'])


@router.post('/add')
async def add_wish(wish: CreateWish, user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    try:
        user_wish = Wish(title=wish.title, description=wish.description,
                         created_at=datetime.utcnow(), status="NOT COMPLETE", user_id=user.id)
        db.add(user_wish)
        await db.commit()
        await db.refresh(user_wish)
        return user_wish
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Не удалось создать желание")
    except DBAPIError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Ошибка соединения с базой данных")

