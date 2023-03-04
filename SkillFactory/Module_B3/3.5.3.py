def get_wind_class(speed):
    if speed in [1, 2, 3, 4]:
        return 'weak [1]'
    elif speed in [5, 6, 7, 8, 9, 10]:
        return 'moderate [2]'
    elif speed in [11, 12, 13, 14, 15, 16, 17, 18]:
        return 'strong [3]'
    else:
        return 'hurricane [4]'


print(get_wind_class(3))
print(get_wind_class(8))
print(get_wind_class(14))
print(get_wind_class(25))
