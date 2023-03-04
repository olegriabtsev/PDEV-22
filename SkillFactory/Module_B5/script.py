L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
print(L)


a = 5
b = 3+2
a_id = id(a)
b_id = id(b)
print(a_id-b_id)

print(id(a))
print(id(b))
