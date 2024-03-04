from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import Model


class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    manufacturer: Mapped[str] = mapped_column(String(64))
    year: Mapped[int]
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[int] = mapped_column(String(32))

    def __repr__(self) -> str:
        return f'Product({self.id}, "{self.name}")'
