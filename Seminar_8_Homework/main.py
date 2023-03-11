# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

import export_import as ex
import model as m

phone_book = []

def menu(data: dict, id_client: int):
    while True:
        print('Выберите действие: ')
        print('0 - Выйти из справочника')
        print('1 - Создать новую запись')
        print('2 - Распечатать содержимое справочника')
        print('3 - Выбрать запись по первой части фамилии')
        print('4 - Изменить поле(я) выбранной записи')
        print('5 - Удалить записи из справочника')
        print('6 - Импортировать данные с текстового файла')
        print('7 - Экспортировать данные из текстового файла')

        get = input('Введите действие: ')
        if get == '0':
            print('До свидания!')
            break
        elif get == '1':
            data = m.create(data, m.get_data())
        elif get == '2':
            m.print_phone_book(data)
        elif get == '3':
            m.read(data)
        elif get == '4':
            m.update(data)
        elif get == '5':
            m.delete(data)
        elif get == '6':
            name_file = ex.get_file_name()
            batch_data = ex.get_bath_data(name_file)
            data = m.batch_create(data, batch_data)
        elif get == '7':
            name_file = ex.get_file_name()
            ex.record_data(name_file, data)
        else:
            print('Некорректный ввод данных, введите ещё раз: ')


menu(phone_book, id_client)



def create(data: dict, id: int, elem: tuple) -> dict: # добавляет запись в существующую телефонную книгу
    data[id] = elem
    return data

def print_phone_book(data: dict) -> None:
    for key, values in data.items():
        print(f'Идентификатор: {key}, {values}')

def get_data() -> tuple: # запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription)
