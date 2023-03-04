list_ = [-5, 2, 4, 8, 12, -7, 5]

for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
    print("Индекс элемента: ", i)
    print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")

list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")