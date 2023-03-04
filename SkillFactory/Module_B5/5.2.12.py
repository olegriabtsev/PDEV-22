a = input('Введите две последовательности целых чисел: ')
b = input('Введите две последовательности целых чисел: ')

set_a, b_set = set(list(map(int, a.split()))), set(list(map(int, b.split())))
a_and_b = set_a.symmetric_difference(b_set)
print(a_and_b)
