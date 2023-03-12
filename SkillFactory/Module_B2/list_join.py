list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print('---')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for i in list2:
    list1.append(i)
print(list1)
print('---')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [True, False, True]
list1.extend(list2)
list1.extend(list3)
print(list1)
