from typing import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.model.base import Base


id_key = Annotated[
    int, mapped_column(primary_key=True, index=True, autoincrement=True, sort_order=-999)
]


class Category(Base):
    """Category SQLAlchemy Model"""
    
    __tablename__ = 'categories'
    
    id: Mapped[id_key] = mapped_column(init=False)
    category_name: Mapped[str] = mapped_column(String(100), init=False)