import logging

from config import ConfigArgumentParser, configure_logging
from model import Library


def main() -> None:
    """Основная функция."""
    configure_logging()

    args = ConfigArgumentParser().parser.parse_args()
    args.func(Library(), args)


if __name__ == '__main__':
    main()
