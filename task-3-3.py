# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    """возвращает сумму наибольших двух аргументов"""
    func_list = [a, b, c]
    func_list.sort()
    return func_list[1] + func_list[2]

print(my_func(5, 2, 3))