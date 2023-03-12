car_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'color': 'red',
    'transmission': 'manual'
}
for i in car_dict:
    print(i)
print('---')
for i in car_dict:
    print(car_dict[i])
print('---')
for i in car_dict.keys():
    print(i)
print('---')
for i in car_dict.values():
    print(i)
print('---')
for i, j in car_dict.items():
    print(i, j)
