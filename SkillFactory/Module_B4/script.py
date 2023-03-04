x = 3


def func():
    global x
    print(x)
    x = 5
    x += 5
    return x


func()
print(x)
