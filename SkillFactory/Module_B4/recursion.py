def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))


def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)


print(rec_fibb(10))  # 55
