car_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'color': 'red',
    'transmission': 'manual'
}
print(car_dict)
print('---')
car_dict.pop('color')
print(car_dict)
print('---')
car_dict.popitem()
print(car_dict)
print('---')
car_dict.clear()
print(car_dict)
