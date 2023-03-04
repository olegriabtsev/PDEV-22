def num_del(a, n):
    if a % n == 0:
        print(f'Данное число {n} является делителем числа {a}')
    else:
        print(f'Данное число {n} не является делителем числа {a}')


num_del(6, 3)
num_del(7, 3)
