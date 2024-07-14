import argparse
import logging
from HW12_task1 import Student, StudentNameError, InvalidSubjectError, InvalidScoreError

logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)

        # Вызываем ошибку класса Student

        student.add_score("Философия", 5)
        student.add_test_result("Математика", 95)

    except StudentNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e}')


if __name__ == '__main__':
    main()

# python HW15.py иван subjects.csv - запуск из командной строки
# Здесь HW15.py - имя файла со скриптом, иван - имя студента, subjects.csv - имя CSV-файла с предметами."""
