# Exercise#2
given_string = '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
x=given_string.upper()
print(x)

x=given_string.strip(" ")
print(x)

x=given_string.lower()
print(x)

x=given_string.isalpha()
print(x)

x=given_string.count("a")
print(x)

x=given_string.replace("super power", "tasty breakfast")
print(x)

x=given_string.replace("i", "1",)
y=given_string.replace(" ", "-")
print(x, y)

# Exercise #3

first_name = input("Enter your first name: ")
last_name = input(f"Enter your last name, {first_name}: ")
patronymic = input(f"Enter your patronymic, {first_name} {last_name}: ")
date_of_birth = input(f"Enter your date of birth, {first_name} {patronymic} {last_name}: ")
first = last_name[0]
second = first_name[0]
third = patronymic[0]
fio = (f"{first}{second}{third}")
print(f"ПІП: {fio}")
print(f"{first_name}\n{last_name}\n{patronymic}\n{date_of_birth}")

# Exercise #1
x=10
y=5
z=20
comparison = x == y == z
print(comparison)

comparison = x != y != z
print(comparison)

comparison = x > y < z
print(comparison)

comparison = x < y > z
print(comparison)

comparison = x >= y <= z
print(comparison)

comparison = x <= y >= z
print(comparison)
