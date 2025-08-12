from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)
    weight = Column(Integer, nullable=False)
    image_url = Column(String(500), nullable=False)
    stock_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
