value_1: str = input("Введите число 1: ")
if not value_1.isdigit():
    print('Вы ввели не число')
    exit()

value_2 = input("Введите число 2: ")
if not value_2.isdigit():
    print('Вы ввели не число')
    exit()

operator = input("Введите оперант (-\+\*\/): ")


if operator == "+":
    print(int(value_1) + int(value_2))

elif operator == "-":
    print(int(value_1) - int(value_2))

elif operator == "/":
    print(int(value_1) / int(value_2))

elif operator == "*":
    print(int(value_1) * int(value_2))

else:
    print('bad operator')