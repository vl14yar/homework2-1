print("Hello and welcome to my first calculator")
action = input('''
It has four operations presently: + - * /
Choose one: ''')
if action == '+':
    first_value = input("Enter first value: ")
    if first_value.isdigit():
        second_value = input("Enter second value: ")
        if second_value.isdigit():
            print(f"{first_value} + {second_value} = {int(first_value) + int(second_value)}")
        else:
            print("Please, enter digit!")
    else:
            print("Please, enter digit!")
elif action == '-':
    first_value = input("Enter first value: ")
    if first_value.isdigit():
        second_value = input("Enter second value: ")
        if second_value.isdigit():
            print(f"{first_value} - {second_value} = {int(first_value) - int(second_value)}")
        else:
            print("Please, enter digit!")
    else:
         print("Please, enter digit!")
elif action == '*':
    first_value = input("Enter first value: ")
    if first_value.isdigit():
        second_value = input("Enter second value: ")
        if second_value.isdigit():
            print(f"{first_value} * {second_value} = {int(first_value) * int(second_value)}")
        else:
            print("Please, enter digit!")
    else:
        print("Please, enter digit!")
elif action == '/':
    first_value = input("Enter first value: ")
    if first_value.isdigit():
        second_value = input("Enter second value: ")
        if second_value.isdigit():
            print(f"{first_value} / {second_value} = {int(first_value) / int(second_value)}")
        else:
            print("Please, enter digit!")
    else:
         print("Please, enter digit!")
else:
    print("Choose correct operation pls")