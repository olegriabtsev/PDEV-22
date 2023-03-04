def multi_plyer(*nums):
    var = 1
    for n in nums:
        var = var * n  # or var *= n

    return var


print(multi_plyer(1))
print(multi_plyer(1, 2))
print(multi_plyer(1, 2, 3))
