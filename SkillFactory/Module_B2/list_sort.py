this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)
print('---')

this_list = [100, 50, 65, 82, 23]
this_list.sort()
print(this_list)
print('---')

this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse=True)
print(this_list)
print('---')


def myfunc(n):
    return abs(n - 50)


this_list = [100, 50, 65, 82, 23]
this_list.sort(key=myfunc)
print(this_list)
