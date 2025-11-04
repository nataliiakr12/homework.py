num1 = float(input ('Ведіть перше число: '))
num2 = float(input ('Введіть друге число: '))
a = input (' +,-,/,*: ')
if a == '+':
    result = num1 + num2
if a == "-":
    result = num1 - num2
if a == "*":
    result = num1 * num2
if a == "/":
    if num2 != 0:
        result = num1 / num2
    else:
     result = ('На 0 ділити не можна')
print('Результат: ', result)
