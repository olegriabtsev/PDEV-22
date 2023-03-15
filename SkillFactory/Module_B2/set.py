a = {'a', 'b', 'c', 'd'}  # используя синтаксис { }
print(a)
print(type(a))
print('---')
L = [1, 1, 2, 3, 2]
print(L)
print('---')
b = set(L)
print(b)
print(type(b))

b_list = list(b)
print(b_list)  # [1,2,3]

c = list(set(L))
print(c)

abons = {"Иванов", "Петров", "Васильев", "Антонов"}
debtors = {"Петров", "Антонов"}
non_debtors = abons.difference(debtors)
print(non_debtors)  # {'Васильев', 'Иванов'}
