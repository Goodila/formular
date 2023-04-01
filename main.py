from datetime import datetime as date
import calendar

y1, m1, d1 = map(int, input('дата начала работы:  ').split('.'))
y2, m2, d2 = map(int, input('дата отчета:  ').split('.'))
date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

hours = int(input('количество часов:  '))
full_hours = int(input('наработка часов:   '))

def check_dates():
    if date1 > date2:
        raise ValueError('первая дата должна быть больше второй')
    return


def next_month(d):
    try:
        n = d.replace(d.year, d.month + 1, d.day)
    except ValueError:
        n = d.replace(d.year + 1, 1, d.day)

    return n


def process():
    '''TODO: жрет один день в первом месяце, отрабатывает последний месяц полностью'''
    flag = True
    new_date = date1
    while True:
        if flag:
            if (date1.year, date1.month) == (date2.year, date2.month):
                res = date2.day - date1.day + 1
                output(date1, res)
                return print('работал меньше месяца')
            res = calendar.monthrange(date1.year, date1.month)[1] - date1.day + 1
            output(date1, res)
            flag = False

        new_date = next_month(new_date)
        if new_date > date2:
            output(date2, date2.day)
            return print(f'достиг конца в {new_date.strftime("%Y-%B")}')

        output(new_date, calendar.monthrange(new_date.year, new_date.month)[1])
        print('-----------')


def output(d, res):

    global full_hours
    full_hours += (res * hours)
    print(f"в месяце - {d.strftime('%Y-%B')}, объект проработал - {res*hours} часов, всего - {full_hours}")



check_dates()

process()

