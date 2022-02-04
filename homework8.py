import random
import re

# task 1.1
l1 = [random.randint(0, 10) for i in range (10)]
l2 = [random.randint(0, 10) for j in range (10)]
a = set(l1)
b = set (l2)
print(a,b)

# task 1.2
c = []
for i in l1:
    for j in l2:
        if i == j:
            c.append(i)
            break
print(c)

# # task 2.1
l3 = [random.randint(0, 100) for i in range (10)]

index = 0
while index < 10:
    print(l3[index])
    index += 1

# task 2.2
for number in l3:
    print(number)

# task 2.3
l4 = [number for number in l3]
print(l4)

# task 3.2
for number in range(20, 100):
    if number % 2 ==0 and number % 4 == 0:
        print(number)

# task 3.3
list = [print(number) for number in range(20, 100) if number % 2 ==0 and number % 4 == 0]

# task 4
list = [48, 24, 12, 70, 50]
for tuple_1 in enumerate(list):
    print(tuple_1)

# Validator
def validate():
    while True:
        password = input("Введіть пароль: ")
        if len(password) < 8:
            print("Ваш пароль повинен мати щонайменше 8 символів")
        elif re.search('[0-9]',password) is None:
            print("Ваш пароль повинний мати хоча б одну цифру")
        elif re.search('[A-Z]',password) is None:
            print("Ваш пароль має починатися з великої літери")
        else:
            print("Пароль створено. Гарного користування!")
            break