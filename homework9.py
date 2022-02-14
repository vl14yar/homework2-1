import random

dict_comp = {random.randint(0, 100) for index, value in enumerate (range(20))}
print(dict_comp)

'''2 створіть словник family в якому по іменах будуть доступні словники для кожного члена сім'ї/родини
(по одному словнику на кожну людину чи домашнього улюбленця)'''

family_dict = {
    'Vova': {
        'age': 13,
        'sex': 'male',
        'hobby': 'programming'
    },
    'Volodymyr': {
        'age': 38,
        'sex': 'male',
        'hobby': 'driving a car'
    },

    'Snizhana': {
        'age': 38,
        'sex': 'female',
        'hobby': 'reading'
    },

    'Volodymyr': {
        'age': 65,
        'sex': 'male',
        'hobby': 'cartography'
    },

    'Natalia': {
        'age': 65,
        'sex': 'female',
        'hobby': 'watching documentary films'
    }
}

'''3 з вашого словника family виведіть тільки імена з усіх записів'''
for name in family_dict:
    print(name)

'''4 Напишіть скрипт, з допомогою якого користувач може перевірити чи значення(ключ або значення),
є у вашому словнику family і якщо воно є то виведіть словник, в якому це значення зустрічається'''

print(family_dict, 'Grandmother', 'age')
element_to_find = 'reading'
for family, family_info in family_dict.items():
    family_info_list = list(family_info.items())
    for info_element in family_info_list:
        if element_to_find in info_element:
            print(f"{element_to_find} was found in \n{family}:{family_info}")
