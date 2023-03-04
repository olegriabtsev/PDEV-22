def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(1, 2, 3)
print('---')
fun(3, 2, 1)
print('---')
fun(a=1, b=2, c=3)
print('---')
fun(c=3, b=2, a=1)
print('---')
print(1)
print(1, 2)
print(1, 2, 3)
print('---')
a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
print('---')
a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
