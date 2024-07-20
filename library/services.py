import logging

from model import Library


def add(library: Library, args) -> None:
    """Добавляет книгу в библиотеку."""
    book = library.add(args.title, args.author, args.year)
    logging.info(f'Added {book}')


def delete(library: Library) -> None:
    """Удаляет книгу из библиотеки."""
    logging.info('Deleted')


def search(library: Library) -> None:
    """Ищет книгу по заданному аргументу."""
    logging.info('Finded')


def show_all(library: Library, *args, **kwargs) -> None:
    """Выводит все книги."""
    for book in library.books:
        print(book)
    logging.info('Listed')


def set_status(library: Library) -> None:
    """Устанавливает статус книги."""
    logging.info('Status is set')
