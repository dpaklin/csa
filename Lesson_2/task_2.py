'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными.

Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''


import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('Files\orders.json', 'r', encoding='utf-8') as from_file:
        data = json.load(from_file)

    with open('Files\orders.json', 'w', encoding='utf-8') as to_file:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, to_file, indent=4)


write_order_to_json('notebook', '1', '57990', 'Ivanov I.I.', '19.11.2021')
