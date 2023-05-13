def solve_integral(method, method_string, f, a, b, n, eps, print_info=True):
    if method_string in ['Метод Симсона']:
        k = 4
    elif method_string in ['Метод трапеций', 'Метод средних прямоугольников']:
        k = 2
    else:
        k = 1

    i0 = method(f, a, b, n)

    while True:
        n *= 2
        i1 = method(f, a, b, n)

        runge_check = abs(i1 - i0) / (2 ** k - 1)

        if print_info:
            print(f'\nN = {int(n / 2)} * 2 = {n}'
                  f'\n|I1 - I0| / (2^k - 1) = |({i1}) - ({i0})| / {2 ** k - 1} = {runge_check}')

        if runge_check <= eps:
            break

        i0 = i1

    return i1, n
