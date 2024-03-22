from pydantic import BaseModel
from typing import Optional


class CreateWish(BaseModel):
    title: str
    description: Optional[str] = None
