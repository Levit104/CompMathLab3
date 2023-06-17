from functions import functions
from methods import methods


def get_data():
    print('\nЧтобы выйти из программы введите exit на любом этапе')

    n_default = 4

    print_dictionary('Подынтегральные функции', functions)
    function_id = int(get_value('Выберите функцию', min_value=1, max_value=len(functions), strict=False))
    function = functions[function_id]

    a = get_value('Введите нижний предел интегрирования')
    b = get_value('Введите верхний предел интегрирования', min_value=a,
                  invalid_message='Верхняя граница должна быть больше нижней')

    eps = get_value('Введите точность')

    print_dictionary('Методы', methods)
    method_id = int(get_value('Выберите метод', min_value=1, max_value=len(methods), strict=False))
    method = methods[method_id]

    return method, function, a, b, n_default, eps


def print_results(integral_value, n, eps):
    try:
        # 0.0001
        round_to = len(str(eps).split('.')[1])
    except IndexError:
        # 1e-05
        round_to = int(str(eps).split('-')[1])

    print(f'\nЗначение интеграла: {round(integral_value, round_to)}'
          f'\nТребуемое число разбиений: {n}')


def valid_value(value, min_value, max_value, strict):
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        if strict:
            return min_value < float(value) < max_value
        else:
            return min_value <= float(value) <= max_value
    except ValueError:
        return False


def get_value(description='Введите значение',
              min_value=float('-inf'), max_value=float('inf'), strict=True,
              invalid_message='Невалидное значение'):
    value = input(f'\n{description}: ').strip().replace(',', '.')

    while not valid_value(value, min_value, max_value, strict):
        print(invalid_message)
        value = input('Повторите ввод: ').strip().replace(',', '.')

    return float(value)


def print_dictionary(name, dictionary):
    print(f'\n{name}:', end='')
    for key, value in dictionary.items():
        print(f'\n\t{key}. {value}', end='')
    print()
