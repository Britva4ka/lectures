import pathlib
#
# p = pathlib.PureWindowsPath("setup.py")
# print(p)

# p = pathlib.Path(__file__) #Путь к файлу рабочему
# print("current file", p)
# print((p.parent)) #Родитель файла
# for parent in p.parents: #Список из родителей
#     print(parent)
# print(p.home().joinpath("Docments", "kakashka"))

"""
cwd - рабочая директория
name - имя файла
stem.suffix
exist 
"""
# p = pathlib.Path(__file__) #Путь к файлу рабочему
# print("current file", p)
# p2 = pathlib.PureWindowsPath(r"C:\Users\User\PycharmProjects")
# print(p2.__repr__())
# print(p.is_relative_to(p2))
# for child in p.parent.parent.iterdir(): #Ітерація по файлам в батьківскій аудиторії
#     print(child)
#
# print(p.stat().st_size) #Статы файла, обращениек размеру
# print(p.is_dir())
# print(p.is_file())
p = pathlib.Path(__file__) #Путь к файлу рабочему
print("current file", p)
p2 = p.with_name("pathlib_usage")
"""
ЗАпись путей файлов в родительской директории
"""
# with p2.open("a") as f:
#     files = [str(child) for child in p.parent.iterdir()]
#     p2.write_text("\n".join(files))
# p2.replace(p.with_name("renamed")) # Смена имени файла
# p.unlink() анлинк удаление файла
# p.rmdir() Папку кслм пустач
#p.touch() Создает вроде бы файл
print(p.exists())
