from functools import wraps
from typing import Callable


def deco(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_count = getattr(func, 'call_count', 0)

        if call_count == 0:
            function_result = func(*args, **kwargs)
            setattr(func, 'call_count', call_count + 1)
            return function_result
        elif call_count == 1:
            raise ValueError(f'Функция {func.__name__} уже была вызвана 1 раз.')

    return wrapper


@deco
def func1(name: str) -> int:
    print(f'hello {name}')
    return 23


@deco
def func2():
    print('hello everyone')
    return [1, 2, 3]


def main():
    func1('Oleg')
    func2()


if __name__ == '__main__':
    main()
