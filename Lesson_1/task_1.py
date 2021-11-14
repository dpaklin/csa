# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
# содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в
# формат Unicode и также проверить тип и содержимое переменных.

STR_LIST = ['разработка', 'сокет', 'декоратор']

for el in STR_LIST:
    print(type(el))
    print(el)

print('-' * 30)

str_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
str_2 = '\u0441\u043e\u043a\u0435\u0442'
str_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

UNIC_LIST = [str_1, str_2, str_3]

for el in UNIC_LIST:
    print(type(el))
    print(el)
