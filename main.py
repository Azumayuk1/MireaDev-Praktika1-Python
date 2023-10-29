import os
import json
import xml.etree.ElementTree as ET
import zipfile


class DiskInfo:
    def __init__(self):
        pass

    def get_disk_info(self):
        for disk in os.popen('wmic logicaldisk get caption, volumename, filesystem, size'):
            print(disk.strip())


class FileOperations:
    def __init__(self):
        pass

    filename = ''

    def work_with_files(self):
        filename = input("Введите имя файла: ")
        filename += ".txt"

        while True:
            print("1. Открыть и записать в файл\n"
                  "2. Прочитать файл\n"
                  "3. Удалить файл\n"
                  "4. Выйти\n")
            choice = input("Выберите действие (введите номер):")

            match choice:
                case '1':
                    self.create_file(filename)
                case '2':
                    self.read_file(filename)
                case '3':
                    self.delete_file(filename)
                case '4':
                    break

    def create_file(self, filename):
        with open(filename, 'w') as f:
            user_input = input("Введите строку для записи в файл: ")
            f.write(user_input)

    def read_file(self, filename):
        with open(filename, 'r') as f:
            print(f.read())

    def delete_file(self, filename):
        os.remove(filename)


class JsonOperations:
    def __init__(self):
        pass

    def work_with_json(self):
        filename = input("Введите имя файла: ")
        filename += ".json"

        while True:
            print("1. Открыть / Создать JSON файл\n"
                  "2. Прочитать JSON файл\n"
                  "3. Удалить JSON файл\n"
                  "4. Выйти\n")
            choice = input("Выберите действие (введите номер):")

            match choice:
                case '1':
                    self.create_json_file(filename)
                case '2':
                    self.read_json_file(filename)
                case '3':
                    self.delete_json_file(filename)
                case '4':
                    break

    def create_json_file(self, filename):
        data = {}
        data['name'] = input("Введите имя человека: ")
        data['age'] = input("Введите возраст: ")
        with open(filename, 'w') as f:
            json.dump(data, f)

    def read_json_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            print(data)

    def delete_json_file(self, filename):
        os.remove(filename)


class XmlOperations:
    def __init__(self):
        pass

    def work_with_xml(self):
        filename = input("Введите имя файла: ")
        filename += ".xml"

        while True:
            print("1. Открыть / Создать XML файл\n"
                  "2. Прочитать XML файл\n"
                  "3. Удалить XML файл\n"
                  "4. Выйти\n")
            choice = input("Выберите действие (введите номер):")

            match choice:
                case '1':
                    self.create_xml_file(filename)
                case '2':
                    self.read_xml_file(filename)
                case '3':
                    self.delete_xml_file(filename)
                case '4':
                    break

    def create_xml_file(self, filename):
        root = ET.Element("person")
        name = ET.SubElement(root, "name")
        name.text = input("Введите имя человека: ")
        age = ET.SubElement(root, "age")
        age.text = input("Введите возраст: ")
        tree = ET.ElementTree(root)
        tree.write(filename)

    def read_xml_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.text)

    def delete_xml_file(self, filename):
        os.remove(filename)


class ZipOperations:
    def __init__(self):
        pass

    def work_with_zip(self):
        zipname: str = input("Введите имя Zip: ")
        zipname += ".zip"

        while True:
            print("1. Открыть / Создать Zip\n"
                  "2. Добавить файл в архив\n"
                  "3. Разархивировать\n"
                  "4. Узнать размер архива\n"
                  "5. Удалить архив\n"
                  "6. Выйти\n")
            choice = input("Выберите действие (введите номер): ")

            match choice:
                case '1':
                    self.create_zip_file(zipname)
                case '2':
                    filename = input("Введите имя файла (с расширением): ")
                    self.add_file_to_zip(filename, zipname)
                case '3':
                    filename = input("Введите имя файла (с расширением): ")
                    self.extract_file_from_zip(filename, zipname)
                case '4':
                    self.get_zip_size(zipname)
                case '5':
                    self.delete_zip_file(zipname)
                case '6':
                    break

    def create_zip_file(self, zipname):
        with zipfile.ZipFile(zipname, 'w') as myzip:
            pass

    def add_file_to_zip(self, filename, zipname):
        with zipfile.ZipFile(zipname, 'a') as myzip:
            myzip.write(filename)

    def extract_file_from_zip(self, filename, zipname):
        with zipfile.ZipFile(zipname, 'r') as myzip:
            myzip.extract(filename)

    def get_zip_size(self, zipname):
        size = os.path.getsize(zipname)
        print(f"Размер архива {zipname}: {size} байт")

    def delete_zip_file(self, zipname):
        os.remove(zipname)


if __name__ == '__main__':
    disk_info = DiskInfo()
    file_ops = FileOperations()
    json_ops = JsonOperations()
    xml_ops = XmlOperations()
    zip_ops = ZipOperations()

    while True:
        print("Выберите действие:")
        print("1. Вывести информацию о дисках")
        print("2. Работа с файлами")
        print("3. Работа с форматом JSON")
        print("4. Работа с форматом XML")
        print("5. Создание zip архива")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        match choice:
            case '1':
                disk_info.get_disk_info()
            case '2':
                file_ops.work_with_files()
            case '3':
                json_ops.work_with_json()
            case '4':
                xml_ops.work_with_xml()
            case '5':
                zip_ops.work_with_zip()
            case '6':
                break
            case _:
                print("Неправильный ввод.")