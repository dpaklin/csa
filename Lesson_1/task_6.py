# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.

import locale

STR_LIST = ['сетевое программирование', 'сокет', 'декоратор']

with open('res.txt', 'w+') as file:
    for i in STR_LIST:
        file.write(i + '\n')
    file.seek(0)

print(file)

FILE_CODING = locale.getpreferredencoding()

with open('res.txt', 'r', encoding=FILE_CODING) as file:
    for i in file:
        print(i)

    file.seek(0)