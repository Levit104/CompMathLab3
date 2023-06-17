from util import get_data, print_results

if __name__ == '__main__':
    while True:
        try:
            method, function, a, b, n_default, eps = get_data()
            integral_value, n = method(function, a, b, n_default, eps)
            print_results(integral_value, n, eps)
        except (EOFError, KeyboardInterrupt):
            print("\nВыход из программы")
            break
