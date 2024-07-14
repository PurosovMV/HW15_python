# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
import logging

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

    count = int(count[:-2])
    weekday = week_dict[weekday]
    month = month_dict[month]
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


if __name__ == '__main__':
    print(date_find('1-й четверг ноября'))
    print(date_find('8-я среда мая'))
    print(date_find('7-я среда мая'))