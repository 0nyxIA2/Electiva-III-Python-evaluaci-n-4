from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

# Tabla intermedia para préstamo (M:N)
loan_table = Table(
    'loan', Base.metadata,
    Column('borrower_id', Integer, ForeignKey('borrowers.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship('Author', back_populates='books')
    publisher = relationship('Publisher', back_populates='books')
    borrowers = relationship('Borrower', secondary=loan_table, back_populates='books')  # M:N

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"

