import logging

from config import configure_argument_parser, configure_logging
from model import Library


def main() -> None:
    """Основная функция."""
    configure_logging()
    logging.info('Library is running...')
    args = configure_argument_parser().parse_args()
    args.func(Library(), args)
    logging.info('Library is stopped.')


if __name__ == '__main__':
    main()
