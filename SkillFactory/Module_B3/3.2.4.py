def is_leap_year(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print('True')
        return f'Год {x} високосный'
    else:
        print('False')
        return f'Год {x} невисокосный'


print(is_leap_year(1998))
print(is_leap_year(2000))
