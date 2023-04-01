import calendar
from datetime import datetime as date
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from formular_ui import Ui_Dialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
full_hours = 0


text = ''


def next_month(d):
    try:
        n = d.replace(d.year, d.month + 1, d.day)
    except ValueError:
        n = d.replace(d.year + 1, 1, d.day)

    return n


def process(date_one, date_two, hours_one, full_hours_one):
    date1 = date_one
    date2 = date_two
    hours = hours_one
    global full_hours

    flag = True
    new_date = date1
    while True:
        if flag:
            if (date1.year, date1.month) == (date2.year, date2.month):
                res = date2.day - date1.day + 1
                output(date1, res, hours)
                return
            res = calendar.monthrange(date1.year, date1.month)[1] - date1.day + 1
            output(date1, res, hours)
            flag = False

        new_date = next_month(new_date)
        if new_date > date2:
            output(date2, date2.day, hours)
            return

        output(new_date, calendar.monthrange(new_date.year, new_date.month)[1], hours)


def output(d, res, hours):
    global full_hours
    global text
    full_hours += (res * hours)
    result = f"в месяце - {d.strftime('%Y-%B')}, объект проработал - {res*hours} часов, всего - {full_hours}\n" \
            f" --------------------------------------------------------------\n"
    text += result


def start():
    global full_hours
    date1 = date(ui.date1.date().year(), ui.date1.date().month(), ui.date1.date().day())
    date2 = date(ui.date2.date().year(), ui.date2.date().month(), ui.date2.date().day())
    hours = int(ui.hours.text())
    full_hours = int(ui.full_hours.text())
    if hours > 24 or hours < 0 or full_hours < 0 or date1 > date2:
        QMessageBox().warning(window, "Warning", "Введите корректные значения!!!", QMessageBox.StandardButton.Ok)
        return
    process(date1, date2, hours, full_hours)
    f = open('results.txt', 'w')
    f.write(text)
    f.close()
    QMessageBox().information(window, "Warning", "Рсчет в файле results.txt в каталоге с исполняемым файлом",
                              QMessageBox.StandardButton.Ok)

ui.pushButton.clicked.connect(start)

window.show()
sys.exit(app.exec())