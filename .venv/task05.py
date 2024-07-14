# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from datetime import datetime
import logging
import argparse

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='../../../../../Downloads/sem15/error_1.log',
                    encoding='utf-8')
logger = logging.getLogger('t_4')
week_dict = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5,
             'воскресенье': 6}
month_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
              'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}


def date_find(text):
    try:
        count, weekday, month = text.split()
    except ValueError:
        logger.error('не смог прочитать строку')
        return

    count = int(count[:-2]) if not count.isdigit() else int(count)
    weekday = week_dict[weekday] if not weekday.isdigit() else int(weekday)
    month = month_dict[month] if not month.isdigit() else int(month)
    year = datetime.now().year
    count_week = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == weekday:
            count_week += 1
            if count_week == count:
                return date
    logger.error(f'Нет такой даты - {text} в текущем году')
    return


def parse():  # Запуск  python task05.py -c 1-й -w четверг -m ноября
    parser = argparse.ArgumentParser(description='Получаем строку с датой', prog='date_find()',
                                     epilog='При отсутствии значений параметров берется текущий день или текущий месяц')
    parser.add_argument('-c', '--count', default=1, help='День недели по счету')
    parser.add_argument('-w', '--weekday', default=datetime.now().weekday(), help='Название дня недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='Название месяца')
    args = parser.parse_args()
    print(args)
    return date_find(f'{args.count} {args.weekday} {args.month}')


# def parse2():
#     parser = argparse.ArgumentParser(description='Получаем строку с датой', prog='date_find()',
#                                      epilog='При отсутствии значений параметров берется текущий день или текущий месяц')
#     parser.add_argument('-c', '--count', default='1-й четверг ноября', help='День недели по счету')
#     # parser.add_argument('-w', '--weekday', default=datetime.now().weekday(), help='Название дня недели')
#     # parser.add_argument('-m', '--month', default=datetime.now().month, help='Название месяца')
#     args = parser.parse_args()
#     print(args)
#     print(args.count)
#     count, weekday, month = args.count.split()
#     print(count, weekday, month)
#     return date_find(f'{count} {weekday} {month}')


if __name__ == '__main__':
    print(parse())
    # print(parse2())

    # print(date_find('1-й четверг ноября'))
    # print(date_find('8-я среда мая'))
    # print(date_find('7-я среда мая'))
