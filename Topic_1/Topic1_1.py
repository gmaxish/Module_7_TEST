"""
Тема 1: “Стандартные функции ввода-вывода”
	•	Напишите программу, которая спрашивала бы у пользователя его имя, пол, возраст и место жительства,
а затем выводила бы полученную информацию на экран в следующем формате:
This is [name].
He (she) is [age] years old.
He (she) lives in [city].
"""
name = input("Enter your name: ")
gender = input("Enter your gender: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

if gender == "Male" or "male":
    gender = "He"
elif gender == "Famale" or "famale":
    gender = "She"

print(f'This id {name}. \n{gender} is {age} years old. \n{gender} lives in {city}')