# Задание №6
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
from pathlib import Path
import logging
from collections import namedtuple

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='../../../../../Downloads/sem15/info_6.log',
                    encoding='utf-8')
logger = logging.getLogger('task06')
File = namedtuple('File', 'name, extension, dir, parent')


def read_dir(path):
    for item in path.iterdir():
        obj = File(item.stem if item.is_file() else item.name, item.suffix, item.is_dir(), item.parent)
        logger.info(obj)


def parse_dir(): # python task06.py -p D:\MSP\pp\sem15
    parser = argparse.ArgumentParser(description='Получаем путь к директории',
                                     epilog='При отсутствии значений параметров берется  текущая директория')
    parser.add_argument('-p', '--path', help='Введите путь к директории', required=True, type=Path)
    args = parser.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    parse_dir()
