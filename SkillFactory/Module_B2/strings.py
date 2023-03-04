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

colors = 'red blue green'
print(colors.split())

path = '/home/user/documents/file.txt'
print(path.split('/'))

colors = 'red blue green'
colors_split = colors.split()

colors_joined = 'and'.join(colors_split)
print(colors_joined)