import json
import logging

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

DEFAULT_ENCODING = 'utf-8'
FILE_PATH = Path('library.json')


class Status(Enum):
    """Объект статуса книги."""

    AVAILABLE = 'в наличии'
    ISSUED = 'выдана'


@dataclass
class Book:
    """Объект книги."""

    id: int
    title: str
    author: str
    year: int
    status: Status = Status.AVAILABLE

    @property
    def as_dict(self) -> dict[str, int | str]:
        """Возвращает свойства книги в виде словаря."""
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
        """Вычисляет идентификатор следующей книги."""
        if not self._books_ids:
            next_id = 1
        else:
            next_id = max(self._books_ids) + 1
        return next_id

    def _write(self) -> None:
        """Сохраняет книги в файл."""
        self.file_path.write_text(
            json.dumps([book.as_dict for book in self._books]),
            encoding=self.encoding,
        )

    def _read(self) -> list[Book]:
        """Загружает книги из файла."""
        if not self.file_path.exists():
            logging.info('Библиотека пуста.')
            return []
        with self.file_path.open(encoding=self.encoding) as file:
            books = []
            for attrs in json.load(file):
                attrs['status'] = Status(attrs['status'])
                books.append(Book(**attrs))
            return books

    @property
    def books(self) -> list[Book]:
        """Возвращает список книг библиотеки."""
        return self._books

    def add(
        self,
        title: str,
        author: str,
        year: str,
    ) -> Book:
        """Добавляет книгу в библиотеку."""
        book_id = self._next_id
        book = Book(book_id, title, author, int(year))
        self._books.append(book)
        self._books_ids.add(book_id)
        self._write()
        return book

    def delete(self, id: int, commit: bool = True) -> Book | None:
        """Удаляет книгу из библиотеки по id."""
        if id not in self._books_ids:
            logging.info(f'Книги с id = {id} не существует.')
            return None
        for idx in range(len(self._books)):
            if self._books[idx].id == id:
                deleted_book = self._books.pop(idx)
                self._books_ids.remove(id)
                if commit:
                    self._write()
                return deleted_book

    def _search_by_field(self, subj: str | int, field: str) -> list[Book]:
        """Фильтрует книги по значению 'subj' поля 'field'."""
        return [book for book in self._books if getattr(book, field) == subj]

    def search(
        self,
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
    ) -> list[Book]:
        """Осуществляет поиск книг по названию, автору или году издания."""
        if title is not None:
            return self._search_by_field(title, 'title')
        if author is not None:
            return self._search_by_field(author, 'author')
        if year is not None:
            return self._search_by_field(year, 'year')
        logging.info('Ничего не найдено.')
        return []

    def set_status(
        self,
        id: int,
        status: str,
    ) -> Book | None:
        """Устанавливает новый статус книги."""
        book = self.delete(id, commit=False)
        if not book:
            return None
        book.status = Status(status)
        self._books.append(book)
        self._books_ids.add(book.id)
        self._write()
        return book
