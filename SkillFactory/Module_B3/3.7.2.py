n = int(input('Введите число: '))


def check_h(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3 + 1) / 2
        if n == 1:
            return True
    return False


print(check_h(n))
