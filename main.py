import os

# Объявляем константу и размещаем в ней путь к папке с файлами для обработки
DIRECTORY = r"C:\Dev\Change_name_file\Backup"


# Объявляем функцию которая получает на вход объявленную ранее константу и циклом проходит
# по ней вытаскивая директорию, названия файлов через метод walk
# и передаём полученные данные далее созданной функции для обработки полученных данных
def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name):
    name = name.replace("_Diff.", "_BC.")
    name = name.replace("_Diffuse.", "_BC.")
    name = name.replace("_Normal.", "_N.")
    name = name.replace("_ORM.", "_AORM.")
    name = name.replace("_O.", "_A.")
    if not name.startswith("T_"):
        name = "T_" + name
    return name


if __name__ == '__main__':
    rename_files(DIRECTORY)
