a = 42
b = 42

print(a == b)
print(a is b)
print('---')

c = 123456789
d = 123456789
print(c == d)
print(c is d)
print('---')

L = ['Hello', 'world']
M = L

print(L)
print(M is L)
M.append('!')
print(L)
print('---')

M = L.copy()
print(M is L)
