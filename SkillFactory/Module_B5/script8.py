PI = 3.14


def area_circle(r):
    global PI
    print('Число глобальное из локальной видимости до изменения', PI)
    print('---')

    PI = 3.1415
    print('Число из локальной видимости после изменения', PI)
    print('---')
    return PI * (r ** 2)


print('Число из глобальной видимости до вызова функции', PI)
print('---')
print(area_circle(10))
print('Число из глобальной видимости после вызова функции', PI)
print('---')

L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))
