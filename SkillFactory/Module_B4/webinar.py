a = 10
while a > 0:
    print(a)
    a -= 1
print('---')

for i in range(10):
    print(i)

print('---')

a = {'Hello': 1,
     'World': 2}

for i in a.items():
    print(i)

print('---')

a = [(1, 2), (3, 4)]

for i, x in a:
    print(i)
    print(x)

print('---')

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in a:
    print(i)

print('---')

a = [str(i) for i in range(10)]
print(a)

print('---')

for i in range(1, 4):
    for j in range(3):
        print(i + j, end='')
    print('')

print('---')

my_array = [i ** 2 for i in range(1, 11)]
print(my_array)

print('---')

my_array = []
for i in range(1, 11):
    my_array.append(i ** 2)
print(my_array)
