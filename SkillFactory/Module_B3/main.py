a = [1, 2, 3]
print(id(a))  # id возвращает идентификатор объекта
# 140039772293512

b = a
print(id(b))
# 140039772293512

print(a is b)  # а и b являются один и тем же объектом
# True


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)  # True
print(a is b)  # False

# Хорошо
a is None

# Плохо
a == None