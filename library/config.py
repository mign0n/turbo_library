import argparse
import logging

from model import Status
import services

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
    add_parser.set_defaults(func=services.add)

    delete_parser = subparsers.add_parser(
        'delete',
        help='Удаляет книгу из библиотеки',
    )
    delete_parser.add_argument('id', help='Идентификатор книги')
    delete_parser.set_defaults(func=services.delete)

    search_parser = subparsers.add_parser(
        'search',
        help='Осуществляет поиск книг в библиотеке',
    )
    search_parser.add_argument('-t', '--title', help='Поиск по названию')
    search_parser.add_argument('-a', '--author', help='Поиск по автору')
    search_parser.add_argument('-y', '--year', help='Поиск по году издания')
    search_parser.set_defaults(func=services.search)

    list_parser = subparsers.add_parser(
        'list',
        help='Выводит список книг в библиотеке',
    )
    list_parser.set_defaults(func=services.show_all)

    set_status_parser = subparsers.add_parser(
        'set-status',
        help='Устанавливает новый статус книги.',
    )
    set_status_parser.add_argument('id', help='Идентификатор книги')
    set_status_parser.add_argument(
        'status',
        choices=Status._value2member_map_,
        help='Желаемый статус книги',
    )
    set_status_parser.set_defaults(func=services.set_status)

    return parser


def configure_logging():
    """Конфигурирует логгер."""
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
    )
