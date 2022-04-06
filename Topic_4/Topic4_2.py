"""
	•	Выведите на экран сначала все файлы, а затем все директории, расположенные в корневой директории созданного
в предыдущей задаче дерева.
"""
import os, os.path

root_dir = "Work"

objs = os.listdir(root_dir)
objs = list(map(lambda i: os.path.join(root_dir, i), objs))
print(objs)

sorted_objs = list(sorted(objs, key=os.path.isfile, reverse=True))
print(sorted_objs)


