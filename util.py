from console import get_value, print_dictionary
from functions import functions
from methods import methods

"""Функции-обёртки, можно обойтись и без них, сделаны для удобства"""

valid_steps_params = (1, float('inf'), True)
valid_precision_params = (0, 1, True)
valid_interval_params = (float('-inf'), float('inf'), True)
valid_function_id_params = (1, len(functions), False)
valid_method_id_params = (1, len(methods), False)


def get_steps():
    return int(get_value('Введите кол-во шагов разбиения',
                         *valid_steps_params,
                         add_validation=lambda n: int(n) % 2 == 0,
                         add_message='\nКол-во шагов должно быть чётным'))


def get_precision():
    return float(get_value('Введите точность', *valid_precision_params))


def get_limits():
    lower_limit = get_value('Введите нижний предел интегрирования',
                            *valid_interval_params)
    upper_limit = get_value('Введите верхний предел интегрирования',
                            *valid_interval_params,
                            add_validation=lambda l: l > lower_limit,
                            add_message='\nВерхняя граница должна быть больше нижней')
    return float(lower_limit), float(upper_limit)


def get_function():
    function_id = int(get_value('Выберите функцию', *valid_function_id_params))
    return functions[function_id]


def get_method():
    method_id = int(get_value('Выберите метод', *valid_method_id_params))
    return methods[method_id]


def print_functions():
    print_dictionary('Подынтегральные функции', functions)


def print_methods():
    print_dictionary('Методы', methods)


def print_results(integral_value, steps, precision):
    try:
        # 0.0001
        round_to = len(str(precision).split('.')[1])
    except IndexError:
        # 1e-05
        round_to = int(str(precision).split('-')[1])

    print(f'\nЗначение интеграла: {round(integral_value, round_to)}'
          f'\nТребуемое число шагов: {steps}')
