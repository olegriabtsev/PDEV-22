def rec_fun(n):
    if n == 1:
        return n
    return n + rec_fun(n - 1)


print(rec_fun(4))
