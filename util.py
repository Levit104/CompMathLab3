from typing import Any

from functions import functions, Function
from methods import methods, Method


def get_data() -> tuple[Method, Function, float, float, int, float]:
    print('\nЧтобы выйти из программы введите exit на любом этапе')

    n_default: int = 4

    print_dictionary('Подынтегральные функции', functions)
    function_id: int = int(get_value('Выберите функцию', min_value=1, max_value=len(functions), strict=False))
    function: Function = functions[function_id]

    a: float = get_value('Введите нижний предел интегрирования')
    b: float = get_value('Введите верхний предел интегрирования', min_value=a,
                         invalid_message='Верхняя граница должна быть больше нижней')

    eps: float = get_value('Введите точность')

    print_dictionary('Методы', methods)
    method_id: int = int(get_value('Выберите метод', min_value=1, max_value=len(methods), strict=False))
    method: Method = methods[method_id]

    return method, function, a, b, n_default, eps


def print_results(integral_value: float, n: int, eps: float) -> None:
    try:
        # 0.0001
        round_to: int = len(str(eps).split('.')[1])
    except IndexError:
        # 1e-05
        round_to = int(str(eps).split('-')[1])

    print(f'\nЗначение интеграла: {round(integral_value, round_to)}'
          f'\nТребуемое число разбиений: {n}')


def valid_value(value: str, min_value: float, max_value: float, strict: bool) -> bool:
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        if strict:
            return min_value < float(value) < max_value
        else:
            return min_value <= float(value) <= max_value
    except ValueError:
        return False


def get_value(description: str = 'Введите значение',
              min_value: float = float('-inf'),
              max_value: float = float('inf'),
              strict: bool = True,
              invalid_message: str = 'Невалидное значение') -> float:
    value: str = input(f'\n{description}: ').strip().replace(',', '.')

    while not valid_value(value, min_value, max_value, strict):
        print(invalid_message)
        value = input('Повторите ввод: ').strip().replace(',', '.')

    return float(value)


def print_dictionary(name: str, dictionary: dict[Any, Any]) -> None:
    print(f'\n{name}:', end='')
    for key, value in dictionary.items():
        print(f'\n\t{key}. {value}', end='')
    print()
