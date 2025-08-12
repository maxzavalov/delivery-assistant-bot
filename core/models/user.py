from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from core.database import Base


# Роли пользователей (можно вынести в отдельный файл enums.py)
class UserRole(PyEnum):
    CLIENT = "client"
    COURIER = "courier"
    MANAGER = "manager"
    ADMIN = "admin"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(200), nullable=True)

    hashed_password = Column(String(256), nullable=True)
    is_active = Column(Boolean, default=True)

    # Ролевая система
    role = Column(Enum(UserRole), default=UserRole.CLIENT, nullable=False)

    # Временные метки
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))

    # Связи
    orders = relationship("Order", back_populates="user")  # Заказы пользователя
    courier_orders = relationship("Order", back_populates="courier")  # Если это курьер