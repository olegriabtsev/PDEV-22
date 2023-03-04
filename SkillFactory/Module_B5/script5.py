squares = [i ** 2 for i in range(1, 11)]
print(squares)
print('---')

squares = [i ** 2 for i in range(1, 11) if i % 2 == 1]
print(squares)
print('---')

list_tuples = [(i, i ** 2) for i in range(1, 11)]
print(list_tuples)
print('---')

M = [[i + j for j in range(5)] for i in range(5)]
print(M[0])
print(M[1])
print(M[2])
print(M[3])
print(M[4])
print('---')

L = [i for i in range(10)]
M = [i for i in range(10, 0, -1)]
N = []
for i in range(10):
    N.append(L[i] * M[i])
print(N)
print('---')
for i in zip(L, M):
    print(i)
print('---')
for a, b in zip(L, M):
    print('a =', a, 'b =', b)
