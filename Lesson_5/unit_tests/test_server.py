"""Unit-тесты сервера"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from Lesson_4.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, PORT, DEFAULT_PORT, \
    RESPONDEFAULT_IP_ADDRESSSE, ANSWER
from Lesson_4.server import process_clients_message


class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    err_dict = {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200, ANSWER: f'Guest, hello!'}

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(process_clients_message(
            {ACTION: PRESENCE, TIME: 1.1, PORT: DEFAULT_PORT, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_clients_message(
            {TIME: '1.1', PORT: DEFAULT_PORT, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(process_clients_message(
            {ACTION: 'Wrong', TIME: '1.1', PORT: DEFAULT_PORT, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(process_clients_message(
            {ACTION: PRESENCE, PORT: DEFAULT_PORT, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(process_clients_message(
            {ACTION: PRESENCE, PORT: DEFAULT_PORT, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(process_clients_message(
            {ACTION: PRESENCE, PORT: DEFAULT_PORT, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)

    def test_no_port(self):
        """Ошибка - нет порта"""
        self.assertEqual(process_clients_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()
