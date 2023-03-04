def first_fun(m):
    nonlocal_var = m

    def second_fun(n):
        return n * nonlocal_var

    return second_fun


two_fun = first_fun(3)
print(type(two_fun))
print(two_fun(3))
