def positive(x):
    return x % 2 == 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]
print('---')

d = {2: "c", 1: "d", 4: "a", 3: "b"}
# Чтобы отсортировать его по ключам, нужно сделать так
print(dict(sorted(d.items())))
print(sorted(d.items(), key=lambda x: x[1]))
print('---')



