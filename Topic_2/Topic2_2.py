"""
•	Результаты экзамена хранятся в словаре: {‘John’: 75, ‘Ann’: 80, ‘Ally’: 60}. Используя форматированный вывод,
выведите результаты экзамена сначала в одной строке, а затем построчно для каждого студента. При этом результаты должны
быть отсортированы в порядке убывания полученных баллов.
"""
lib = {"John": 75, "Ann": 80, "Ally": 60}

sorted_lib = sorted(lib.items(), key=lambda pair: pair[1], reverse=True)

sorted_lib_str = ", ".join(map(lambda item: f'{item[0]} - {item[1]}', sorted_lib))
print(sorted_lib_str)
print('*'*50)
print("\n".join(map(lambda item: f'{item[0]} - {item[1]}', sorted_lib)))
