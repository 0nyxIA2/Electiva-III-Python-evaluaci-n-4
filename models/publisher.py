from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='publisher')  # 1:N

    def __repr__(self):
        return f"<Publisher(id={self.id}, name='{self.name}')>"

