"""Лаунчер"""
import random
import subprocess

PROCESS = []
NAME = ['Gleb', 'Lev', 'Noname', 'Alex', 'Roman', 'Anton', 'Olga']

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(2):
            command = f'python client.py -m send -n {random.choice(NAME)}'
            PROCESS.append(subprocess.Popen(command,
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(2):
            command = f'python client.py -m listen -n {random.choice(NAME)}'
            PROCESS.append(subprocess.Popen(command,
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()