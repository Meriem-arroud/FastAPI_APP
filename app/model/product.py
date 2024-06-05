import uuid
import shortuuid
from app.model.base import Base
from typing import Annotated, Union
from sqlalchemy import ForeignKey, String, Float, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.category import Category


def generate_product_id():
    return str(shortuuid.encode(uuid.uuid4()))


id_key = Annotated[
    str, mapped_column(primary_key=True, index=True, autoincrement=False, insert_default=generate_product_id, sort_order=-999)
]

class Product(Base):
    """Product SQLAlchemy Model"""

    __tablename__ = 'products'

    id: Mapped[id_key] = mapped_column(init=False, comment='Product ID from Amazon') 
    title: Mapped[str] = mapped_column(String(500))
    imgUrl: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float())
    stars: Mapped[float] = mapped_column(Float(), default=0)
    reviews: Mapped[int] = mapped_column(Integer(), default=0)
    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id', ondelete='SET NULL'), default=None)
    isBestSeller: Mapped[bool] = mapped_column(Boolean(), default=False)
   #category: Mapped[Union['Category', None]] = relationship(init=False, backref='products', default=None)


    



