input_of_numbers = list(map(float, input('Введиде числа через пробел: ').split()))
input_of_numbers[0], input_of_numbers[-1] = input_of_numbers[-1], input_of_numbers[0]
input_of_numbers.append(sum(input_of_numbers))
print(input_of_numbers)