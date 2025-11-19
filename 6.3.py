def mult_digits(n):
    while n > 9:
        p = 1
        for digit in str(n):
            p *= int(digit)
        n = p
    return n
number = int(input())
print(mult_digits(number))

