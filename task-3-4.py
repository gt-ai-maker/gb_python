# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень

def my_fun(x, y):
    """возведения числа x в степень y"""
    print(x**abs(y))

    i = 1  # текущая степень
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    print(result)


my_fun(3, -3)
