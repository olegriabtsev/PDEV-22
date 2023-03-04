L = [3.3, 4.4, 5.5, 6.6]

# к каждому элементу применяем функцию округления
print(map(round, L)) # <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L))) # [3, 4, 6, 7]

string = input('Введите числа через пробел:')
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

