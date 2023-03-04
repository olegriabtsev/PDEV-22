a = None # пустая строка
b = a or 1
print(b)
print(type(b))

print('---')
print(42 and 0 and '' and False)
print('---')
print(1 and "hello" and [False])
print('---')
print([] or 3.14 or False)
print('---')
print(0 or '' or False)
