# Form implementation generated from reading ui file 'formular_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 211, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 209, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 181, 31))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 209, 33))
        self.label_2.setObjectName("label_2")
        self.hours = QtWidgets.QLineEdit(parent=Dialog)
        self.hours.setGeometry(QtCore.QRect(10, 130, 209, 20))
        self.hours.setObjectName("hours")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 209, 17))
        self.label.setObjectName("label")
        self.date1 = QtWidgets.QDateEdit(parent=Dialog)
        self.date1.setGeometry(QtCore.QRect(10, 40, 209, 20))
        self.date1.setObjectName("date1")
        self.date2 = QtWidgets.QDateEdit(parent=Dialog)
        self.date2.setGeometry(QtCore.QRect(10, 90, 209, 20))
        self.date2.setObjectName("date2")
        self.full_hours = QtWidgets.QLineEdit(parent=Dialog)
        self.full_hours.setGeometry(QtCore.QRect(10, 180, 209, 20))
        self.full_hours.setObjectName("full_hours")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Сколько часов в день работает прибор"))
        self.pushButton.setText(_translate("Dialog", "РАССЧИТАТЬ"))
        self.label_4.setText(_translate("Dialog", "Изначальныая наработка часов"))
        self.label_2.setText(_translate("Dialog", "ДАТА КОНЦА ОТСЧЕТА"))
        self.hours.setText(_translate("Dialog", "24"))
        self.label.setText(_translate("Dialog", "ДАТА НАЧАЛА ОТСЧЕТА"))
        self.full_hours.setText(_translate("Dialog", "0"))
