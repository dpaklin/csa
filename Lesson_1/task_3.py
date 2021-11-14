# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

def try_encoding():
    STR_LIST = ["attribute", "класс", "функция", "type"]
    for word in STR_LIST:
        try:
            encode_word = bytes(word, 'ascii')
        except:
            print('Word: {0} cannot be written in bytes'.format(word))

try_encoding()