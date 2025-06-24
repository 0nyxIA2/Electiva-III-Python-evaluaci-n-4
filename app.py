import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from controllers.library_controller import LibraryController
from views.console_view import show_menu

def main():
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    controller = LibraryController(session)

    while True:
        show_menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            name = input("Nombre del autor: ")
            print(controller.add_author(name))
        elif choice == '2':
            name = input("Nombre de la editorial: ")
            print(controller.add_publisher(name))
        elif choice == '3':
            title = input("Título del libro: ")
            author_id = int(input("ID autor: "))
            publisher_id = int(input("ID editorial: "))
            print(controller.add_book(title, author_id, publisher_id))
        elif choice == '4':
            name = input("Nombre del prestatario: ")
            print(controller.add_borrower(name))
        elif choice == '5':
            borrower_id = int(input("ID prestatario: "))
            book_id = int(input("ID libro: "))
            controller.loan_book(borrower_id, book_id)
            print("Préstamo registrado.")
        elif choice == '6':
            for a in controller.list_authors(): print(a)
        elif choice == '7':
            for p in controller.list_publishers(): print(p)
        elif choice == '8':
            for b in controller.list_books(): print(b)
        elif choice == '9':
            for br in controller.list_borrowers(): print(br)
        elif choice == '10':
            entity = input("Entidad (author/publisher/book/borrower): ")
            id_ = int(input("ID: "))
            new = input("Nuevo nombre/título: ")
            func = getattr(controller, f"update_{entity}")
            func(id_, new)
            print("Actualizado.")
        elif choice == '11':
            entity = input("Entidad (author/publisher/book/borrower): ")
            id_ = int(input("ID: "))
            func = getattr(controller, f"delete_{entity}")
            func(id_)
            print("Eliminado.")
        elif choice == '0':
            break
        else:
            print("Opción no válida.")


if __name__ == '__main__':
    main()        
