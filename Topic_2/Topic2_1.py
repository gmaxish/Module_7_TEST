"""
Тема 2: “Форматированный вывод”
	•	Напишите программу, запрашивающую у пользователя 4 числа. Отдельно сложите первые два числа, а затем вторые два
числа. Разделите первую сумму на вторую и выведите результат на экран так, чтобы ответ содержал знак и две цифры после
запятой.
"""
print("Введите, по очереди, 4 любых числа")
a = input("Введите любое число: ")
b = input("Введите любое число: ")
c = input("Введите любое число: ")
d = input("Введите любое число: ")
result = int(a + b) / int(c + d)

print("{:.2}".format(result))
print(f'{result:.2}')