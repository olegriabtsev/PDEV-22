a = int(input('Введите целое число: '))
if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print(f'Число {a} удовлетворяет условиям')
