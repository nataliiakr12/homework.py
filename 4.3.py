import random
numbers = [random.randint(1, 100) for _ in range(random.randint(3, 100))]
new_numbers = numbers[0], numbers[2], numbers[-2]

print('Рандомний список: ', numbers)
print( 'Перший, третій номер і другий номер з кінця: ', new_numbers)
