# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_number = 0
while number != 0:
    last_namber = number % 10
    if last_namber > max_number:
        max_number = last_namber
    number //= 10

print(f"Самоя большая цыфра {max_number}")