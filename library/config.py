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

ADD_COMMAND = 'add'
ADD_COMMAND_HELP = 'Добавляет книгу в библиотеку'
ADD_TITLE_ARG = 'title'
ADD_TITLE_ARG_HELP = 'Название книги'
ADD_AUTHOR_ARG = 'author'
ADD_AUTHOR_ARG_HELP = 'Автор книги'
ADD_YEAR_ARG = 'year'
ADD_YEAR_ARG_HELP = 'Год издания книги'

DELETE_COMMAND = 'delete'
DELETE_COMMAND_HELP = 'Удаляет книгу из библиотеки'

ID_ARG = 'id'
ID_ARG_HELP = 'Идентификатор книги'

LIST_COMMAND = 'list'
LIST_COMMAND_HELP = 'Выводит список книг в библиотеке'

SEARCH_COMMAND = 'search'
SEARCH_COMMAND_HELP = 'Осуществляет поиск книг в библиотеке'
SEARCH_TITLE_ARG = ('-t', '--title')
SEARCH_TITLE_ARG_HELP = 'Поиск по названию'
SEARCH_AUTHOR_ARG = ('-a', '--author')
SEARCH_AUTHOR_ARG_HELP = 'Поиск по автору'
SEARCH_YEAR_ARG = ('-y', '--year')
SEARCH_YEAR_ARG_HELP = 'Поиск по году издания'

SET_STATUS_COMMAND = 'set-status'
SET_STATUS_COMMAND_HELP = 'Устанавливает новый статус книги.'
SET_STATUS_ARG = 'status'
SET_STATUS_ARG_HELP = 'Желаемый статус книги'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


class ConfigArgumentParser:
    """Конфигурирует парсер аргументов командной строки."""

    def __init__(self) -> None:
        """Инициализирует парсер аргументов."""
        self.__parser = argparse.ArgumentParser(description=PARSER_DESCRIPTION)
        self.__subparsers = self.__parser.add_subparsers(
            title=SUBPARSER_TITLE,
            description=SUBPARSER_DESCRIPTION,
            help=SUBPARSER_HELP,
            required=True,
        )

    def __add_parser(self) -> None:
        """Конфигурирует вложенный парсер команды добавления книги."""
        add_parser = self.__subparsers.add_parser(
            ADD_COMMAND,
            help=ADD_COMMAND_HELP,
        )
        add_parser.add_argument(ADD_TITLE_ARG, help=ADD_TITLE_ARG_HELP)
        add_parser.add_argument(ADD_AUTHOR_ARG, help=ADD_AUTHOR_ARG_HELP)
        add_parser.add_argument(ADD_YEAR_ARG, help=ADD_YEAR_ARG_HELP)
        add_parser.set_defaults(func=services.add)

    def __delete_parser(self) -> None:
        """Конфигурирует вложенный парсер команды удаления книги."""
        delete_parser = self.__subparsers.add_parser(
            DELETE_COMMAND,
            help=DELETE_COMMAND_HELP,
        )
        delete_parser.add_argument(ID_ARG, help=ID_ARG_HELP)
        delete_parser.set_defaults(func=services.delete)

    def __list_parser(self) -> None:
        """Конфигурирует вложенный парсер команды вывода списка книг."""
        list_parser = self.__subparsers.add_parser(
            LIST_COMMAND,
            help=LIST_COMMAND_HELP,
        )
        list_parser.set_defaults(func=services.show_all)

    def __search_parser(self) -> None:
        """Конфигурирует вложенный парсер команды поиска книг."""
        search_parser = self.__subparsers.add_parser(
            SEARCH_COMMAND,
            help=SEARCH_COMMAND_HELP,
        )
        search_parser.add_argument(
            *SEARCH_TITLE_ARG,
            help=SEARCH_TITLE_ARG_HELP,
        )
        search_parser.add_argument(
            *SEARCH_AUTHOR_ARG,
            help=SEARCH_AUTHOR_ARG_HELP,
        )
        search_parser.add_argument(*SEARCH_YEAR_ARG, help=SEARCH_YEAR_ARG_HELP)
        search_parser.set_defaults(func=services.search)

    def __set_status_parser(self) -> None:
        """Конфигурирует вложенный парсер команды установки статуса книги."""
        set_status_parser = self.__subparsers.add_parser(
            SET_STATUS_COMMAND,
            help=SET_STATUS_COMMAND_HELP,
        )
        set_status_parser.add_argument(ID_ARG, help=ID_ARG_HELP)
        set_status_parser.add_argument(
            SET_STATUS_ARG,
            choices=Status.values(),
            help=SET_STATUS_ARG_HELP,
        )
        set_status_parser.set_defaults(func=services.set_status)

    @property
    def parser(self) -> argparse.ArgumentParser:
        """Собирает конфигурацию парсера воедино."""
        self.__add_parser()
        self.__delete_parser()
        self.__search_parser()
        self.__list_parser()
        self.__set_status_parser()
        return self.__parser


def configure_logging():
    """Конфигурирует логгер."""
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
    )
