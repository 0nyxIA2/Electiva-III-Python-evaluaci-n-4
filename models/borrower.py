from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .book import loan_table

class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', secondary=loan_table, back_populates='borrowers')

    def __repr__(self):
        return f"<Borrower(id={self.id}, name='{self.name}')>"

