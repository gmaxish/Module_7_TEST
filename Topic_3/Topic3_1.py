"""
Тема 3: “Работа с файлами”
	•	Дан некоторый файл students.txt, который содержит список студентов (имя и фамилия студента в каждой строке),
отсортированный в алфавитном порядке. Реализуйте следующие функции:
	•	добавить нового студента в список. Функция должна принимать два параметра: имя и фамилия, - и добавлять нового
студента в файл, не нарушая сортировку списка.
	•	найти студента. Функция должна принимать один обязательный параметр - фамилия - и один опциональный параметр -
имя. Если передается только фамилия, то функция должна вывести на экран список всех студентов с данной фамилией или
сообщение о том, что студенты с данной фамилией не найдены. Если в функцию передаются оба параметра, то она должна
вывести на экран сообщение о том, находится ли данный студент в группе.
	•	редактировать информацию о студенте. Функция должна принимать 2 обязательных параметра: текущие имя и фамилия
студента, - и 2 опциональных параметра: новые имя или фамилия студента. Функция должна найти студента с заданными
параметрами в списке и изменить его имя или фамилию (или и то, и другое в зависимости от переданных опциональных
параметров), сохраняя сортировку списка. Если заданный студент в списке не найден, необходимо вывести на экран
соответствующее сообщение.
	•	удалить студента. Функция принимает один обязательный параметр - фамилия студента, и 1 опциональный - имя
студента. Если в функцию передана только фамилия студента, и список содержит несколько студентов с указанной фамилией,
то функция должна вывести на экран их список и попросить пользователя ввести также имя студента, и после этого удалить
заданного студента из списка. Если в функцию переданы оба параметра, то она проверяет, находится ли студент в списке и
удаляет его. Если студент(ы) с заданными параметрами не найдены, должно быть выведено соответствующее сообщение.
"""
from typing import final

FILE_PATH: final = "../Files/students.txt"


def readFile(file_path=FILE_PATH):
    students = []
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        surname, name = line.split()
        students.append({"surname": surname, "name": name})

    return students


def writeFile(students, file_path=FILE_PATH):
    students_sorted = sorted(students, key=lambda st: st["surname"])
    with open(file_path, 'w') as f:
        for elem in students_sorted:
            f.write(f'{elem["surname"]} {elem["name"]}\n')



def addStudent(surname, name):
    students = readFile(FILE_PATH)
    print(students)
    students.append({"surname": surname, "name": name})
    writeFile(students)


def findStudent(surname, name=None):
    student = readFile()

    if name is None:
        res = list(filter(lambda i: i['surname'] == surname, student))
        if not res:
            print(f'Студенты с фамилией {surname!r} не найдены')
            return []
        print("Студенты найдены:")
        for st in res:
            print(f'{st["name"]} {st["surname"]}')
        return res
    res = list(filter(lambda i: i['surname'] == surname and i['name'] == name, student))
    print(f"Студент '{name} {surname}' {'не ' if not res else ''}находится в группе.")
    return res


def editStudent(name, surname, new_name=None, new_surname=None):
    students = readFile()

    st = findStudent(surname=surname, name=name)
    if st:
        new_st = {"name": new_name if new_name is not None else name,
                  "surname": new_surname if new_surname is not None else surname}
        students = list(filter(lambda i: i["name"] != name or i["surname"] != surname, students))
        students.append(new_st)
        writeFile(students)
        print(f'Изменения были успешно внесены!')


def delStudent(surname, name=None):
    students = findStudent(surname=surname, name=name)

    if len(students) == 0:
        return
    if len(students) > 1:
        name = input("Введите имя студента: ")
        st = list(filter(lambda i: i["name"] == name, students))
        if not st:
            print("Студент не найден")
            return
    all_students = readFile()
    all_students = list(filter(lambda i: (i["name"] != name is not None) or i["surname"] != surname, all_students))
    writeFile(all_students)
    print(f"Студент '{name if name is not None else ''} {surname}' успешно удален.")



#addStudent("Hryhorovych", "Maksym")
#addStudent("Hryhorovych", "Daryna")

# findStudent("Hryhorovych")
# findStudent("abram")
# findStudent(name="Maksym", surname="Hryhorovych")
# findStudent(name="Ivan", surname="Alekseev")

#editStudent(name="Maksym", surname="Hryhorovych", new_name="Iryna")
#editStudent(name="Maksym", surname="Hryhorovych", new_name="Iryn")
#editStudent(name="Iryna", surname="Hryhorovych", new_name="Maksym", new_surname="Hryhorovych")

#delStudent(surname="Fox")
#delStudent(surname="Hryhorovych")