while True:
    num1 = float(input ('Ведіть перше число: '))
    num2 = float(input ('Введіть друге число: '))
    a = input (' +,-,/,*: ').strip()
    if a == '+': result = num1 + num2
    if a == "-": result = num1 - num2
    if a == "*": result = num1 * num2
    if a == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = ('На 0 ділити не можна')
    print('Результат: ', result)
    cont = input('Хочете продовжити? y/n: ').strip().lower()
    if cont != 'y':
        print('Бувай')
        break


