from solver import solve_integral
from util import get_function, get_limits, get_precision, get_steps, get_method, \
    print_functions, print_methods, print_results

if __name__ == '__main__':
    while True:
        try:
            print('\nЧтобы выйти из программы введите exit на любом этапе')

            print_functions()
            function, function_string = get_function()

            lower_limit, upper_limit = get_limits()
            precision = get_precision()
            # steps_default = get_steps()
            steps_default = 4

            print_methods()
            method, method_string = get_method()

            integral_value, steps = solve_integral(method, method_string,
                                                   function, lower_limit, upper_limit,
                                                   steps_default, precision)

            print_results(integral_value, steps, precision)
        except (EOFError, KeyboardInterrupt):
            print("\nВыход из программы")
            break
