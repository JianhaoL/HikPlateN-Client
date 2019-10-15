# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogBlacklist.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re

class DialogBN(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogBN, self).__init__(parent)
        self.nList = []
        self.dList = []
        self.setObjectName("Dialog")
        self.resize(540, 572)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.date2 = QtWidgets.QDateEdit(Dialog)
        self.date2.setMinimumDate(QtCore.QDate(2019, 10, 15))
        self.date2.setObjectName("date2")
        self.gridLayout.addWidget(self.date2, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.date1 = QtWidgets.QDateEdit(Dialog)
        self.date1.setMinimumDate(QtCore.QDate(2019, 10, 15))
        self.date1.setObjectName("date1")
        self.gridLayout.addWidget(self.date1, 1, 1, 1, 1)
        self.date3 = QtWidgets.QDateEdit(Dialog)
        self.date3.setMinimumDate(QtCore.QDate(2019, 10, 15))
        self.date3.setObjectName("date3")
        self.gridLayout.addWidget(self.date3, 3, 1, 1, 1)
        self.number1 = QtWidgets.QLineEdit(Dialog)
        self.number1.setObjectName("number1")
        self.gridLayout.addWidget(self.number1, 1, 0, 1, 1)
        self.number2 = QtWidgets.QLineEdit(Dialog)
        self.number2.setObjectName("number2")
        self.gridLayout.addWidget(self.number2, 2, 0, 1, 1)
        self.number3 = QtWidgets.QLineEdit(Dialog)
        self.number3.setObjectName("number3")
        self.gridLayout.addWidget(self.number3, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Blacklist Number:"))
        self.label_2.setText(_translate("Dialog", "Expire Date"))
        self.number1.setPlaceholderText(_translate("Dialog", "No special symbols like @!#$%"))
        self.label_3.setText(_translate("Dialog", "Plate Number:"))

    def plateNumber(self):
        return self.nList

    def accept(self):
        if not self.number1.text():
            self.lineEdit.setText(" ")
        if not self.number2.text():
            self.number2.setText(" ")
        if not self.number3.text():
            self.number3.setText(" ")
        if not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.number1.text()) or not re.match(
                pattern="^([A-Za-z0-9 ])+$", string=self.number2.text()) or not re.match(pattern="^([A-Za-z0-9 ])+$",
                                                                                            string=self.number3.text()):
            QtWidgets.QMessageBox.information(self, "Format Error",
                                              "The Number can only contain alphanumeric and space!")
        else:
            # self.str1=self.lineEdit.text()
            str1 = self.number1.text()
            str2 = self.number2.text()
            str3 = self.number3.text()
            str1 = str1.replace(" ", "")
            str2 = str2.replace(" ", "")
            str3 = str3.replace(" ", "")
            if str1:
                self.nList.append(str1)
            if str2:
                self.nList.append(str2)
            if str3:
                self.nList.append(str3)
            if not self.nList:
                QtWidgets.QMessageBox.information(self, "Empty Error", "The Number cant be empty!")
            else:
                self.done(1)

    def reject(self):
        self.done(-1)

    @staticmethod
    def getNumber(parent=None):
        dialog = DialogBN(parent)
        result = dialog.exec_()
        if result == 1:
            numbers = dialog.plateNumber()
            return (numbers, 1)
        else:
            return (0, -1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DialogBN(Dialog)
    result=ui.exec_()
    if result == 1:
        print("succeed")
    else:
        print("fail")

