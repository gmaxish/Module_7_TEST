"""
	•	Дана последовательность чисел (количество чисел может изменяться). Используя форматированный вывод, выведите на
экран количество чисел в последовательности, а затем и сами числа.
Например, для чисел (2, 3, 5) вывод может иметь следующий вид:
“The 3 numbers are: 2, 3, 5.”
"""

numbers = (2, 3, 5, 7, 9, 11, 2, 43)

print(f'The {len(numbers)} numbers are: {str(numbers).replace("(","").replace(")", "")}')
