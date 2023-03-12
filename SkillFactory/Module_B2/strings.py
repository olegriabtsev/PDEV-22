s = "Hello!"
#print(s[0]) # H
#print(s[4]) # o
#print(len(s))
#print(s.upper())
#print(s.lower())

mystr = 'Hello World!'
#print(mystr[::2])
#print(mystr[-1])
#print(mystr[:-2])
#print(mystr[::-1])

_str = 'Hello World!'
print(_str.find('l'))
print(_str.count('l'))
print('---')
print(_str.index(' '))
print('.'.join(_str))
# print('\n'.join(_str))
print('---')
colors = 'white yellow green blue'
print(colors)
colors_split = colors.split()
print(colors_split)
colors_joined = ' - '.join(colors_split)
print(colors_joined)
