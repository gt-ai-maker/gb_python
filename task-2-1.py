# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

lists = [100, "200", True, [1, 2, 3], "строка"]

for element_list in lists:
    print(f"{element_list} > type {type(element_list)}")
