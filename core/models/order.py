from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String, default='new')
    date = Column(DateTime)
