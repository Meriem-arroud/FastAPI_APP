from pydantic import BaseModel, HttpUrl
from typing import Optional

class ProductCreate(BaseModel):
    title: str
    imgUrl: HttpUrl
    price: float
    category_id: int


class ProductUpdate(BaseModel):
    title: Optional[str] = None
    imgUrl: Optional[str] = None
    stars: Optional[float] = 0
    reviews: Optional[int] = 0
    price: Optional[float] = 0
    category_id: Optional[int] = None
    isBestSeller: Optional[bool] = False    

class ProductOut(ProductCreate):
    id: str
    stars: float
    reviews: int
    isBestSeller: bool

