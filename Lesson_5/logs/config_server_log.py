"""Кофнфиг серверного логгера"""

import sys
import os
import logging
import logging.handlers
# sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('../')
from Lesson_5.common.variables import LOGGING_LEVEL

# создаём формировщик логов (formatter):
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
PATH = os.path.join(PATH, 'server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(LOGGING_LEVEL)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='S')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
