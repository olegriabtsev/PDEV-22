#  range_1 = range(-10, -1)
#  range_2 = range(2, 15)
A = float(input('Введите число: '))
if not (-10 <= A <= -1 or 2 <= A <= 15):
    print(f'Число {A} не принадлежит данному интервалу')
else:
    print(f'Число {A} принадлежит данному интервалу')


A = int(input('Введите число\n'))

if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")