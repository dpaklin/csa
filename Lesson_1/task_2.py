# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов # (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

BYTE_LIST = [b'class', b'function', b'method']

for el in BYTE_LIST:
    print(el, type(el), len(el))
    print('-' * 30)