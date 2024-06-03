from datetime import datetime
import zoneinfo
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column
from settings import settings

class DateTimeMixin(MappedAsDataclass):
    """ Mixin """
    created_time: Mapped[datetime] = mapped_column(
        init=False,
        default_factory=datetime.now(zoneinfo.ZoneInfo(settings.DATETIME_TIMEZONE)),
        sort_order=999
    )
    updated_time: Mapped[datetime | None] = mapped_column(
        init=False,
        onupdate=datetime.now(zoneinfo.ZoneInfo(settings.DATETIME_TIMEZONE)),
        sort_order=999
    )


class DataClassBase(MappedAsDataclass, DeclarativeBase):
    """
    DataClassBase
    `MappedAsDataclass <https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#orm-declarative-native-dataclasses>`__
    """  
    __abstract__ = True


class Base(DataClassBase):
    """
     Mixin
    """  
    __abstract__ = True