# Задание №3 Доработаем задачу 2.Сохраняйте в лог файл раздельно:
# уровень логирования, дату события, имя функции (не декоратора),
# аргументы вызова, результат.


import logging
import os

import logging

FORMAT = '{levelname:<8} - {asctime}. {msg}'

# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#          'в строке {lineno:03d} функция "{funcName}()" ' \
#          'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='error_1.log',
                    encoding='utf-8')
logger = logging.getLogger('task03')

# logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='error_2.log',
# encoding='utf-8')
handler2 = logging.FileHandler('error_2.log', mode='w', encoding='utf-8')
handler2.setLevel(logging.DEBUG)
# formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
formatter2 = logging.Formatter(FORMAT, style='{')
handler2.setFormatter(formatter2)
logger.addHandler(handler2)


def my_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'args': args, **kwargs}
        logger.info(f'Функция: {func.__name__}, Аргументы функции {info_dict}, результат: {result}')

        return result

    return wrapper


@my_logger
def sum_numbers(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    sum_numbers(10, 5, 15, 16, z=8, c='Привет')
sum_numbers(x=20, y=3)
sum_numbers(100, 999)
