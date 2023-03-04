a = input('Введите две последовательности целых чисел: ').split()
b = input('Введите две последовательности целых чисел: ').split()

set_a, b_set = set(a), set(b)
a_and_b = set_a.difference(b_set)
print(a_and_b)