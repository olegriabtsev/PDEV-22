a = int(input('Введите целое число: '))
if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print(f'Число {a} удовлетворяет условиям')
else:
    print(f'Число {a} не удовлетворяет условиям')
    