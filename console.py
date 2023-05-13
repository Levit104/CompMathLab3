from validation import valid_value


def get_value(description, *valid_params, add_validation=lambda x: True, add_message=''):
    value = input(f'\n{description}: ').strip()

    while not (valid_value(value, *valid_params) and add_validation(value)):
        print(f'Невалидное значение{add_message}')
        value = input('Повторите ввод: ').strip()

    return value


def print_dictionary(name, dictionary, value_is_tuple=True, value_tuple_index=1):
    print(f'\n{name}:', end='')
    for key, value in dictionary.items():
        print(f'\n\t{key}. {value[value_tuple_index] if value_is_tuple else value}', end='')
    print()
