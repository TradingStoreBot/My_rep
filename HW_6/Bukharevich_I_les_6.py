import json
import csv
"""
Задание 1
Кодировки
"""
# cod_val_1 = b'r\xc3\xa9sum\xc3\xa9'
#
# decod_val_2 = cod_val_1.decode()
# print(decod_val_2)
#
# cod_val_2 = decod_val_2.encode("latin1")
# print(cod_val_2)
#
# decod_val_3 = cod_val_2.decode("latin1")
# print(decod_val_3)



"""
Задание 2
Ввести 4 строки сохранить в 4-ре разные переменные.
Создать файл и записать в него 2 строки, закрыть файлю.
Затем открыть и добавить 2-е оставшиеся.
В итоге 4 строки должны начинаться с новой строки.
"""
# str_1 = input('Введите первую строку: ')
# str_2 = input('Введите вторую строку: ')
# str_3 = input('Введите третью строку: ')
# str_4 = input('Введите четвертую строку: ')
# file_name = open('text_hw_2.txt', 'w')
# file_name.write(str_1 + '\n' + str_2 + '\n')
# file_name.close()
# file_name = open('text_hw_2.txt', 'a')
# file_name.write(str_3 + '\n' + str_4)
# file_name.close()


"""
Задание 3
Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""
#
# data = {
#     100001: ('Oleg', 25),
#     100002: ('Dime', 19),
#     100003: ('Valodya', 36),
#     100004: ('Vasilisa', 29),
#     100005: ('Petr', 23),
#     100006: ('Kostya', 28),
# }
#
# with open('id_people.json', 'w') as file:
#     json.dump(data, file)
#
# with open('id_people.json', 'r') as file:
#     data_new_json = json.load(file)
#     print(data_new_json)
