n = '123456789'
print(list(str(n)))
list_digit = list(map(int, list(str(n))))
print(3 and 7 in list_digit)

N = '123456789'
print('3' in str(N) and '7' in str(N))