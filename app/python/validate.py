import json, traceback, logging


class Validate(RuntimeError):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, args, kwargs)


class ValidateException(Exception):
    def __init__(self, message, args):
        print(f'An error was occurred: {message}')
        for error in args:
            print(error)


# class ValidationException(Exception):
#     def __init__(self, message, args):
#         logging.error(message, traceback.format_exc())


def to_list(value: str, sep: str = ',', callback=None):
    values = str.split(value, sep=sep)

    return values if callback is None else callback(values)


def to_int(values: list) -> list:
    int_values = []
    try:
        for value in values:
            int_values.append(int(value))
        return int_values
    except ValueError as ex:
        raise ValidateException('ValueError', ex.args)


def to_printer(message, func):
    func(f'Agora vai {message}')


def printer(message):
    print(f'Print Function', end='\n')
    print(message)


def main():
    lista = '4132, 41324132, 413413, afa, 343214'
    to_list(lista, ',', to_int)
    to_printer(lista, printer)


if __name__ == '__main__':
    main()
