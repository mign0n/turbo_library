import json
import logging

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

DEFAULT_ENCODING = 'utf-8'
FILE_PATH = Path('library.json')


class Status(Enum):
    AVAILABLE = 'в наличии'
    ISSUED = 'выдана'


@dataclass(frozen=True)
class Book:
    """Объект книги."""

    id: int
    title: str
    author: str
    year: int
    status: Status = Status.AVAILABLE

    @property
    def as_dict(self) -> dict[str, int | str]:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status.value,
        }


class Library:
    """Объект библиотеки."""

    def __init__(
        self,
        file_path=FILE_PATH,
        encoding=DEFAULT_ENCODING,
    ) -> None:
        self.file_path = file_path
        self.encoding = encoding
        self._books = self._read()
        self._books_ids = set(book.id for book in self._books if book)

    @property
    def _next_id(self) -> int:
        if not self._books_ids:
            next_id = 1
        else:
            next_id = max(self._books_ids) + 1
        return next_id

    def _write(self) -> None:
        self.file_path.write_text(
            json.dumps([book.as_dict for book in self._books]),
            encoding=self.encoding,
        )

    def _read(self) -> list[Book]:
        if not self.file_path.exists():
            logging.info('Библиотека пуста.')
            return []
        with self.file_path.open(encoding=self.encoding) as file:
            books = []
            for attrs in json.load(file):
                attrs['status'] = Status(attrs['status'])
                books.append(Book(**attrs))
            return books

    def add(self, title: str, author: str, year: str) -> Book:
        book_id = self._next_id
        book = Book(book_id, title, author, int(year))
        self._books.append(book)
        self._books_ids.add(book_id)
        self._write()
        return book

    @property
    def books(self) -> list[Book]:
        return self._books
