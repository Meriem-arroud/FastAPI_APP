from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class PaginationResponseSchema(BaseModel, Generic[T]):
    items: list[T]
    total: int
    offset: int
    limit: int
    is_last_page: Optional[bool] = None

    def model_post_init(self, __context: Any) -> None:
        self.is_last_page = self.total <= self.offset + self.limit