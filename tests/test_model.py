import json
import os
import unittest


from library.model import FILE_PATH, Book, Library, Status


class LibraryTestCase(unittest.TestCase):
    """Тесты модели Library."""

    @classmethod
    def setUpClass(cls):
        """Создает тестовый объект библиотеки."""
        cls.library = Library(FILE_PATH)

    @classmethod
    def tearDownClass(cls):
        """Удаляет тестовый файл с данными библиотеки."""
        os.remove(FILE_PATH)

    def test_01_create_new_book(self) -> None:
        """Тест добавления книги в библиотеку."""
        self.library.add('test title', 'test author', '1970')
        self.assertEqual(
            self.library.books,
            [Book(1, 'test title', 'test author', 1970, Status.AVAILABLE)],
        )
        self.assertIn(1, self.library._books_ids)

    def test_02_new_book_in_file(self) -> None:
        """Тест записи книги в файл с данными библиотеки."""
        with self.library.file_path.open(
            encoding=self.library.encoding
        ) as file:
            self.assertEqual(
                [
                    {
                        'id': 1,
                        'title': 'test title',
                        'author': 'test author',
                        'year': 1970,
                        'status': Status.AVAILABLE.value,
                    }
                ],
                json.load(file),
            )

    def test_03_create_another_book(self) -> None:
        """Тест добавления другой книги в библиотеку."""
        self.library.add('test title 2', 'test author 2', '1980')
        self.assertEqual(
            self.library.books,
            [
                Book(1, 'test title', 'test author', 1970, Status.AVAILABLE),
                Book(
                    2,
                    'test title 2',
                    'test author 2',
                    1980,
                    Status.AVAILABLE,
                ),
            ],
        )
        self.assertEqual({1, 2}, self.library._books_ids)

    def test_04_all_books_in_file(self) -> None:
        """Тест записи другой книги в файл с данными библиотеки."""
        with self.library.file_path.open(
            encoding=self.library.encoding
        ) as file:
            self.assertEqual(
                [
                    {
                        'id': 1,
                        'title': 'test title',
                        'author': 'test author',
                        'year': 1970,
                        'status': Status.AVAILABLE.value,
                    },
                    {
                        'id': 2,
                        'title': 'test title 2',
                        'author': 'test author 2',
                        'year': 1980,
                        'status': Status.AVAILABLE.value,
                    },
                ],
                json.load(file),
            )
