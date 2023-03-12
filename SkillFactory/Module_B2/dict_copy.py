car_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'color': 'red',
    'transmission': 'manual'
}
car_dict2 = car_dict
print(car_dict)
print(car_dict2)
print('---')
car_dict['brand'] = 'Chevrolet'
print(car_dict)
print(car_dict2)
print('---')
new_car_dict = car_dict.copy()
print(new_car_dict)
print('---')
my_dict = dict(car_dict)
print(my_dict)
