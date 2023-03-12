car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
}
if 'model' in car:
    print('Yes, this key exist in dictionary')
else:
    print('No, there is no such a key exist!')

print(car)
print(car.values())
print(len(car))
print('---')
x = car['model']
print(x)
print('---')
x = car.get('model')
print(x)
print('---')
x = car.keys()
print(x)
print('---')
car['color'] = 'red'
print(car)
x = car.keys()
print(x)
y = car.values()
print(y)
car['year'] = 2020
print(car)
y = car.items()
print(y)
