from sqlalchemy.orm import Session
from models.author import Author
from models.publisher import Publisher
from models.book import Book
from models.borrower import Borrower

class LibraryController:
    def __init__(self, session: Session):
        self.session = session

    # CREATE
    def add_author(self, name: str) -> Author:
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()
        return author

    def add_publisher(self, name: str) -> Publisher:
        publisher = Publisher(name=name)
        self.session.add(publisher)
        self.session.commit()
        return publisher

    def add_book(self, title: str, author_id: int, publisher_id: int) -> Book:
        book = Book(title=title, author_id=author_id, publisher_id=publisher_id)
        self.session.add(book)
        self.session.commit()
        return book

    def add_borrower(self, name: str) -> Borrower:
        borrower = Borrower(name=name)
        self.session.add(borrower)
        self.session.commit()
        return borrower

    def loan_book(self, borrower_id: int, book_id: int) -> None:
        borrower = self.session.query(Borrower).get(borrower_id)
        book = self.session.query(Book).get(book_id)
        borrower.books.append(book)
        self.session.commit()

    # READ
    def list_authors(self): return self.session.query(Author).all()
    def list_publishers(self): return self.session.query(Publisher).all()
    def list_books(self): return self.session.query(Book).all()
    def list_borrowers(self): return self.session.query(Borrower).all()

 # UPDATE
    def update_author(self, author_id: int, new_name: str) -> None:
        author = self.session.query(Author).get(author_id)
        author.name = new_name
        self.session.commit()

    def update_publisher(self, publisher_id: int, new_name: str) -> None:
        publisher = self.session.query(Publisher).get(publisher_id)
        publisher.name = new_name
        self.session.commit()

    def update_book(self, book_id: int, new_title: str) -> None:
        book = self.session.query(Book).get(book_id)
        book.title = new_title
        self.session.commit()

    def update_borrower(self, borrower_id: int, new_name: str) -> None:
        borrower = self.session.query(Borrower).get(borrower_id)
        borrower.name = new_name
        self.session.commit()

    # DELETE
    def delete_author(self, author_id: int) -> None:
        self.session.query(Author).filter_by(id=author_id).delete()
        self.session.commit()

    def delete_publisher(self, publisher_id: int) -> None:
        self.session.query(Publisher).filter_by(id=publisher_id).delete()
        self.session.commit()

    def delete_book(self, book_id: int) -> None:
        self.session.query(Book).filter_by(id=book_id).delete()
        self.session.commit()

    def delete_borrower(self, borrower_id: int) -> None:
        self.session.query(Borrower).filter_by(id=borrower_id).delete()
        self.session.commit()