number = int(input("Введи 5-тизначне число "))
if number<10000 or number>99999:
    print("Бачу, що вводиш не ті цифри")
else:
    a=number%10
    b=number//10%10
    c=number//100%10
    d=number//1000%10
    e=number//10000
    number2=a*10000+b*1000+c*100+d*10+e*1
    print(number2)