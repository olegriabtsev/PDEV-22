from geometric_figures import *


def main():
    r = int(input('Введите радиус круга:\n'))

    a = int(input('Введите длину прямоугольника:\n'))
    b = int(input('Введите ширину прямоугольника:\n'))

    if circle_area(r) > rectangle_area(a, b):
        print('Площадь круга больше')
    else:
        print('Площадь прямоугольника больше')


main()
