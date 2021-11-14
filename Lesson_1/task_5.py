# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.

import subprocess

PING_RESURS = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']]

for el in PING_RESURS:

    ping_process = subprocess.Popen(el, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 4:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('-' * 30)
            break