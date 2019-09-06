# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtWidgets, QtGui
import re




class DialogBN(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogBN, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(453, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 20, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setWindowTitle("Dialog")
        self.label.setText("Add Black List:")
        self.label.setStyleSheet("color: red;")
        self.lineEdit.setPlaceholderText( "No special letter like!@# allowed")
        self.lineEdit.setStyleSheet("color: red;")
        self.lineEdit_2.setStyleSheet("color: red;")
        self.lineEdit_3.setStyleSheet("color: red;")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.nList=[]

    def plateNumber(self):
        return self.nList

    def accept(self):
        if not self.lineEdit.text():
            self.lineEdit.setText(" ")
        if not self.lineEdit_2.text():
            self.lineEdit_2.setText(" ")
        if not self.lineEdit_3.text():
            self.lineEdit_3.setText(" ")
        if not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit.text()) or not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit_2.text()) or not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit_3.text()):
            QtWidgets.QMessageBox.information(self, "Format Error", "The Number can only contain alphanumeric and space!")
        else:
            # self.str1=self.lineEdit.text()
            str1=self.lineEdit.text()
            str2=self.lineEdit_2.text()
            str3=self.lineEdit_3.text()
            str1=str1.replace(" ", "")
            str2=str2.replace(" ", "")
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
        dialog=DialogBN(parent)
        result=dialog.exec_()
        if result==1:
            numbers = dialog.plateNumber()
            return (numbers, 1)
        else:
            return (0, -1)



class DialogWN(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogWN, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(453, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 20, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.setWindowTitle("Dialog")
        self.label.setText("Add White List:")
        self.label.setStyleSheet("color: green;")
        self.lineEdit.setPlaceholderText( "No special letter like!@# allowed")
        self.lineEdit.setStyleSheet("color: green;")
        self.lineEdit_2.setStyleSheet("color: green;")
        self.lineEdit_3.setStyleSheet("color: green;")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.nList=[]

    def plateNumber(self):
        return self.nList

    def accept(self):
        if not self.lineEdit.text():
            self.lineEdit.setText(" ")
        if not self.lineEdit_2.text():
            self.lineEdit_2.setText(" ")
        if not self.lineEdit_3.text():
            self.lineEdit_3.setText(" ")
        if not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit.text()) or not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit_2.text()) or not re.match(pattern="^([A-Za-z0-9 ])+$", string=self.lineEdit_3.text()):
            QtWidgets.QMessageBox.information(self, "Format Error", "The Number can only contain alphanumeric and space!")
        else:
            # self.str1=self.lineEdit.text()
            str1=self.lineEdit.text()
            str2=self.lineEdit_2.text()
            str3=self.lineEdit_3.text()
            str1=str1.replace(" ", "")
            str2=str2.replace(" ", "")
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
        dialog=DialogWN(parent)
        result=dialog.exec_()
        if result==1:
            numbers = dialog.plateNumber()
            return (numbers, 1)
        else:
            return (0, -1)



