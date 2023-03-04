n = 'aaabbccccdaa'
count = {}
for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i, j in count.items():
    print(i, j, end='')


# 2
text = input('Введите текст в виде строки: ')

last = text[0]
count = 0
result = ''

for i in text:
    if i == last:
        count += 1
    else:
        result += last + str(count)
        last = i
        count = 1
result += last + str(count)
print(result)
