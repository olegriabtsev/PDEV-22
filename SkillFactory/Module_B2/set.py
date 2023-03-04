a = {'a', 'b', 'c', 'd'} # используя синтаксис { }
print(a)

L = [1,1,2,3,2]
b = set(L)
print(b) # {1,2,3}

b_list = list(b)
print(b_list) # [1,2,3]

c = list(set(L))
print(c)

abons = {"Иванов", "Петров", "Васильев", "Антонов"}
debtors = {"Петров", "Антонов"}
non_debtors = abons.difference(debtors)
print(non_debtors) # {'Васильев', 'Иванов'}