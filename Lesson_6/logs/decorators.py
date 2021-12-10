import inspect
import sys
import logging
import traceback

import Lesson_6.logs.config_server_log
import Lesson_6.logs.config_client_log

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


class Log:
    def __call__(self, func):
        def write_log(*args, **kwargs):
            main_func = func(*args, **kwargs)
            LOGGER.debug(f'Вызов из {func.__module__} функции {func.__name__}. Параметры {args}, {kwargs} '
                         f'Вызванная из функции {traceback.format_stack()[0].strip().split()[-1]} '
                         f'из функции {inspect.stack()[1][3]}')
            return main_func

        return write_log