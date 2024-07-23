import logging

from model import Library


def add(library: Library, args) -> None:
    """Добавляет книгу в библиотеку."""
    book = library.add(args.title, args.author, args.year)
    logging.info(f'Added {book}')


def delete(library: Library, args) -> None:
    """Удаляет книгу из библиотеки."""
    try:
        book = library.delete(int(args.id))
        logging.info(f'Deleted {book}')
    except ValueError:
        logging.info('Значение id должно являться целым числом.')


def search(library: Library) -> None:
    """Ищет книгу по заданному аргументу."""
    logging.info('Finded')


def show_all(library: Library, *args, **kwargs) -> None:
    """Выводит все книги."""
    for book in library.books:
        print(book.as_dict)
    logging.info('Listed')


def set_status(library: Library) -> None:
    """Устанавливает статус книги."""
    logging.info('Status is set')
