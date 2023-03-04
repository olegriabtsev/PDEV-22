def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


# вызовем два раза одну и ту же функцию
incorrect_func()
print('-----')
incorrect_func()
