value_1 = input("value: ")
if not value_1.isdigit():
    print('bad_value1')
    exit()

value_2 = input("value: ")
if not value_2.isdigit():
    print('bad_value2')
    exit()

operator = input("operator (-\+\*\/): ")


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