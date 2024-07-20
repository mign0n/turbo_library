import argparse
import logging

from services import show_all
from services import add

PARSER_DESCRIPTION = (
    'Управляет библиотекой книг. '
    'Позволяет добавлять, удалять, искать и отображать книги.'
)
SUBPARSER_TITLE = 'Команды'
SUBPARSER_DESCRIPTION = 'Описание доступных команд'
SUBPARSER_HELP = (
    'Операции добавления, удаления, поиска, отображения, '
    'установки статуса книг'
)

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


def configure_argument_parser() -> argparse.ArgumentParser:
    """Конфигурирует парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(description=PARSER_DESCRIPTION)
    subparsers = parser.add_subparsers(
        title=SUBPARSER_TITLE,
        description=SUBPARSER_DESCRIPTION,
        help=SUBPARSER_HELP,
        required=True,
    )
    add_parser = subparsers.add_parser(
        'add',
        help='Добавляет книгу в библиотеку',
    )
    add_parser.add_argument('title', help='Название книги')
    add_parser.add_argument('author', help='Автор книги')
    add_parser.add_argument('year', help='Год издания книги')
    add_parser.set_defaults(func=add)

    list_parser = subparsers.add_parser(
        'list',
        help='Выводит список книг в библиотеке',
    )
    list_parser.set_defaults(func=show_all)
    return parser


def configure_logging():
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
    )
