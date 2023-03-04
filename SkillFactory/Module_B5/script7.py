def linear_solve(a, b):
    if a:
        return b / a
    elif not a and not b:
        return 'Бесконечное количество корней'
    else:
        return 'Нет корней'


print(linear_solve(2, 9))
