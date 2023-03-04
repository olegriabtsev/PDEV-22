def my_fun(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


my_fun()


def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_


print(adder())
print(adder(1))
print(adder(1, 2))
print(adder(1, 2, 3))
print('---')
