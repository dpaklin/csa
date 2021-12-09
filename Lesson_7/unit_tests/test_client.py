"""Unit-тесты клиента"""

import sys
import os
import unittest

# sys.path.append(os.path.join(os.getcwd(), '..'))
from ..common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ANSWER, DEFAULT_PORT, PORT
from ..client import create_presence_users, process_answer


class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence_users()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        port = DEFAULT_PORT
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, PORT: port, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_answer, {ERROR: 'Bad Request'})

    def test_message_ans(self):
        """Проверка на наличие входящего сообщения от сервера"""
        self.assertIn('Hello', process_answer({RESPONSE: 200, ANSWER: 'Hello'}))


if __name__ == '__main__':
    unittest.main()