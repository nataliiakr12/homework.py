digit = int(input("Введи 4-тизначне число "))
a, digit=divmod(digit,1000)
b, digit=divmod(digit,100)
c, digit=divmod(digit,10)
d = digit

print(a)
print(b)
print(c)
print(d)