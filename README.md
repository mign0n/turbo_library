# Система управления библиотекой

## Описание

Консольное приложение для управления библиотекой книг. Позволяет добавлять,
удалять, искать и отображать книги.

## Технологии

- Python 3.12

## Использование

При запуске приложения создается файл для хранения данных о книгах.

По умолчанию - в корне проекта с именем `library.json`

### Справка

Встроенная справка об использовании приложения вызывается командой:

```shell
python library --help
```

В приложении доступны команды:

- `add` - Добавляет книгу в библиотеку
- `delete` - Удаляет книгу из библиотеки
- `search` - Осуществляет поиск книг в библиотеке
- `list` - Выводит список книг в библиотеке
- `set-status` - Устанавливает новый статус книги

По каждой команде можно получить справку с помощью флага `--help` (или `-h`).

```shell
python library add -h
```

Если в передаваемых аргументах присутствуют символы пробела, эти аргументы
необходимо заключать к кавычки, как показано в примерах ниже.

### Примеры команд

#### Команда `python library add <title> <author> <year>`

```shell
python library add 'Test-Driven Development with Python' 'Harry J.W. Persival' 2018
```

#### Команда `python library delete <id>`

```shell
python library delete 1
```

#### Команда `python library search [-t TITLE] [-a AUTHOR] [-y YEAR]`

Поиск производится по одному параметру (названию или автору или году).

```shell
python library search --title 'Test-Driven Development with Python'
```

```shell
python library search --author 'Harry J.W. Persival'
```

```shell
python library search --author 2018
```

#### Команда `python library list`

```shell
python library list
```

#### Команда `python library set-status <id> <status>`

Книга имеет какой-либо один из возможных статусов: "в наличии" или "выдана"

```shell
python library set-status 1 выдана
```

```shell
python library set-status 1 'в наличии'
```

## Установка

- Склонируйте репозиторий и перейдите в директорию проекта

```shell
git clone https://github.com/mign0n/turbo_library.git && cd turbo_library
```

- Установите и активируйте виртуальное окружение

```shell
python -m venv venv && source venv/bin/activate
```

- Можно пользоваться

```shell
python library -h
```

## Авторы

- [Олег Сапожников](https://github.com/mign0n)
