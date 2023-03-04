print(iter('oleg'))
print(iter([1, 2, 3]))
print(iter({'name': 'oleg'}))
print(iter((1, 'oleg')))

for i in range(10):
    pass

str_ = 'my test'
str_iter = iter(str_)
print(type(str_))
print(type(str_iter))
print('---')
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))


# print(next(str_iter))

def count(start, step):
    counter = start
    while True:
        yield counter
        counter += step


my_gen_func = count(100, 10)
for i in range(10):
    print(next(my_gen_func))

print('---')


def last_gen():
    for i in range(10):
        yield i
        if i == 5:
            raise StopIteration


my_last_gen = last_gen()

for i in range(10):
    print(next((my_last_gen)))

