def get_multipliers(a):
    count = 0
    for n in range(1, a + 1):
        if a % n == 0:
            count += 1
    return count


print(get_multipliers(5))  # 2
print(get_multipliers(4))  # 2
