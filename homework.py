# Homework
# Слздать программу которая получает на вход данные о треугольниках(катеты)
# Выводит информацию о каждом треугольнике в формате:
# Треугольник с катетами {a} и {b} имеет гипотенузу {c} и площадь {s}


# Первый вариант


import math
from collections import Counter


def triangle_function_first():
    a = input("Enter first leg length. If you enter not only one number use space for divide: ")
    b = input("Enter second leg length. If you enter not only one number use space for divide: ")
    if len(a) == len(b):
        if len(a) > 1:
            a = a.split()
            b = b.split()
            a_leg = [int(i) for i in a]
            b_leg = [int(i) for i in b]
            list_of_legs = list(zip(a_leg, b_leg))
            for i in list_of_legs:
                i = list_of_legs.index(i)
                a_side = list_of_legs[i][0]
                b_side = list_of_legs[i][1]
                if a_side > 0 and b_side > 0:
                    c_side = math.sqrt(a_side ** 2 + b_side ** 2)
                    s = (a_side * b_side) / 2
                    print(f'Triangle {i + 1} have legs {a_side} and {b_side} square {s} and hypotenuse {c_side}')
                else:
                    print(f"Triangle sides ({a_side}, {b_side}) need to be greater than 0")
        else:
            if int(a) > 0 and int(b) > 0:
                a_side = int(a)
                b_side = int(b)
                c_side = math.sqrt(a_side ** 2 + b_side ** 2)
                s = (a_side * b_side) / 2
                print(f'Triangle 1 have legs {a_side} and {b_side} square {s} and hypotenuse {c_side}')
            else:
                print(f"Triangle sides ({int(a)}, {int(b)}) need to be greater than 0")
    else:
        print("Rows that you entered not equal")

triangle_function_first()


# Второй вариант


def triangle_function_second():
    sides = input("Enter triangle sides with space between (if you enter more than two sides keep typing with space): ")
    sides = sides.split()
    if len(sides) % 2 == 0:
        sides = [int(i) for i in sides]
        a = [item for item in sides if sides.index(item) % 2 == 0]
        b = [item for item in sides if sides.index(item) % 2 != 0]
        list_of_legs = list(zip(a, b))
        for i in list_of_legs:
            i = list_of_legs.index(i)
            a_side = list_of_legs[i][0]
            b_side = list_of_legs[i][1]
            if a_side > 0 and b_side > 0:
                c_side = math.sqrt(a_side ** 2 + b_side ** 2)
                s = (a_side * b_side) / 2
                print(f'Triangle {i + 1} have legs {a_side} and {b_side} square {s} and hypotenuse {c_side}')
            else:
                print(f"Triangle sides ({a_side}, {b_side}) need to be greater than 0")
    else:
        print("Your string have odd number of literals. Please enter the even number of literals")
triangle_function_second()


# Создайте список словарей, которые одержат поля имя, возраст и пол.


def persons_function():
    persons = [
        {
            "name": "Anna",
            "age": 19,
            "gender": "female"
        }, {
            "name": "Anna",
            "age": 29,
            "gender": "female"
        }, {
            "name": "Ivan",
            "age": 30,
            "gender": "male"
        }, {
            "name": "Ivan",
            "age": 10,
            "gender": "male"
        }, {
            "name": "Tatyana",
            "age": 24,
            "gender": "female"
        }, {
            "name": "Ilya",
            "age": 25,
            "gender": "male"
        }, {
            "name": "Ilya",
            "age": 21,
            "gender": "male"
        }, {
            "name": "Mikhail",
            "age": 21,
            "gender": "male"
        }, {
            "name": "Kristina",
            "age": 21,
            "gender": "female"
        }, {
            "name": "Fred",
            "age": 40,
            "gender": "male"
        }, {
            "name": "Frank",
            "age": 35,
            "gender": "male"
        }
    ]

    persons_number = len(persons)
    persons_number_male = len([d for d in persons if d["gender"] == "male"])
    persons_number_female = len([d for d in persons if d["gender"] == "female"])
    persons_who_adult = len([d for d in persons if d["age"] >= 18])
    persons_all_names = [d.get("name") for d in persons]
    persons_unique_ages = sorted(set([d.get("age") for d in persons]))
    persons_three_most_popular_names = Counter([d.get("name") for d in persons]).most_common(3)
    persons_male_sort_by_first_letter_F_and_age = [d.get("name") for d in persons if
                                                   d.get("name")[0] == "F" and d.get("age") > 35]
    print(f'Persons number: {persons_number}\n'
          f'Number of male: {persons_number_male}\n'
          f'Number of female: {persons_number_female}\n'
          f'Number of adult persons: {persons_who_adult}\n'
          f'All names from persons: {persons_all_names}\n'
          f'Unique ages of all persons: {persons_unique_ages}\n'
          f'Three most popular names: {persons_three_most_popular_names}\n'
          f'Three most popular names: {persons_male_sort_by_first_letter_F_and_age}\n')


persons_function()
