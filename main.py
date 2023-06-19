from io_handler import get_data

if __name__ == '__main__':
    while True:
        try:
            float_format = '.5f'
            n_default: int = 4

            method, function, a, b, eps = get_data()
            integral_value, n = method(function, a, b, n_default, eps, float_format=float_format, print_info=True)

            print(f'\nЗначение интеграла: {integral_value:{float_format}}'
                  f'\nТребуемое число разбиений: {n}')
        except (EOFError, KeyboardInterrupt):
            print("\nВыход из программы")
            break
