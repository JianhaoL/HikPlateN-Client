# -*- coding: utf-8 -*-
import os
import io
import sys
def _append_run_path():
    if getattr(sys, 'frozen', False):
        pathlist = []

        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        pathlist.append(sys._MEIPASS)

        # the application exe path
        _main_app_path = os.path.dirname(sys.executable)
        pathlist.append(_main_app_path)

        # append to system path enviroment
        os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)
_append_run_path()
from PyQt5 import QtCore, QtGui, QtWidgets
from QDIALOG import DialogBN, DialogWN
from HttpConnection import connect_getPlate, connect_putPlate, connect_getDevInfo, connect_putPlateNVR
from xlwt import Workbook
import xlrd
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#
def file_path(filename):
    relative_path = filename
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.rowIndex=0
        self.NVR=False
        self.showW=0
        self.showB=0
        self.logout=1
        self.user=""
        self.ipAddress0=""
        self.passwd=""
        self.MainWindow=MainWindow
        self.list_b=[]
        self.list_p=[]
        MainWindow.setObjectName("HikVision Plate Export & Import")
        MainWindow.resize(700, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ipEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ipEdit.setObjectName("ipEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ipEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setObjectName("userEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.passwdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdEdit.setObjectName("passwdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwdEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.loginButton)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.graphicsLabel= QtWidgets.QLabel(self.centralwidget)
        self.graphicsLabel.setObjectName("graphicsLabel")
        self.gridLayout.addWidget(self.graphicsLabel, 0, 1, 1, 1)
        self.graphicsLabel.resize(200, 100)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBlack = QtWidgets.QPushButton(self.centralwidget)
        self.addBlack.setObjectName("addBlack")
        self.horizontalLayout.addWidget(self.addBlack)
        self.addWhite = QtWidgets.QPushButton(self.centralwidget)
        self.addWhite.setObjectName("addWhite")
        self.horizontalLayout.addWidget(self.addWhite)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.VLayout_2 = QtWidgets.QVBoxLayout()
        self.VLayout_2.setObjectName("VLayout_2")
        self.deviceName= QtWidgets.QLineEdit(self.centralwidget)
        self.deviceName.setReadOnly(True)
        self.deviceName.setObjectName("deviceName")


        self.deviceModelLabel = QtWidgets.QLabel(self.centralwidget)
        self.deviceModelLabel.setObjectName("deviceModelLabel")

        self.deviceModel = QtWidgets.QLineEdit(self.centralwidget)
        self.deviceModel.setReadOnly(True)
        self.deviceModel.setObjectName("deviceModel")


        self.firmwareVLabel = QtWidgets.QLabel(self.centralwidget)
        self.firmwareVLabel.setObjectName("firmwareVLabel")

        self.firmwareV = QtWidgets.QLineEdit(self.centralwidget)
        self.firmwareV.setReadOnly(True)
        self.firmwareV.setObjectName("firmwareV")

        self.deviceNamelabel = QtWidgets.QLabel(self.centralwidget)
        self.deviceNamelabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deviceNamelabel.setObjectName("deviceNamelabel")

        self.filterBlackList =QtWidgets.QPushButton(self.centralwidget)
        self.filterBlackList.setText("Show blacklist only")
        self.filterBlackList.setObjectName("filterBlackList")
        self.filterBlackList.setEnabled(False)

        self.filterWhiteList = QtWidgets.QPushButton(self.centralwidget)
        self.filterWhiteList.setText("Show whitelist only")
        self.filterWhiteList.setObjectName("filterWhiteList")
        self.filterWhiteList.setEnabled(False)

        self.searchN = QtWidgets.QLabel(self.centralwidget)
        self.searchN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchN.setObjectName("Search Number")
        self.searchN.setText("Search Plate Number:")



        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setObjectName("search for the number")
        action = QtWidgets.QAction(self.MainWindow)
        action.setIcon(QtGui.QIcon(resource_path("searchIcon.png")))
        self.searchInput.addAction(action, QtWidgets.QLineEdit.TrailingPosition)
        self.searchInput.textChanged.connect(self.search)
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setEnabled(False)



        self.VLayout_2.addWidget(self.deviceNamelabel)
        self.VLayout_2.addWidget(self.deviceName)
        self.VLayout_2.addWidget(self.deviceModelLabel)
        self.VLayout_2.addWidget(self.deviceModel)
        self.VLayout_2.addWidget(self.firmwareVLabel)
        self.VLayout_2.addWidget(self.firmwareV)
        self.VLayout_2.addWidget(self.filterBlackList)
        self.VLayout_2.addWidget(self.filterWhiteList)
        self.VLayout_2.addWidget(self.searchN)
        self.VLayout_2.addWidget(self.searchInput)

        self.VLayout_2.addStretch()
        self.gridLayout.addLayout(self.VLayout_2, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 8)
        self.gridLayout.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.saveFile = QtWidgets.QAction("Save File", self.MainWindow)
        self.saveFile.setShortcut("Ctrl+S")
        self.saveFile.setStatusTip('Export to xls file')
        self.saveFile.triggered.connect(self.exportE)
        self.fileMenu = self.menubar.addMenu('File')
        self.saveFile.setEnabled(False)
        self.fileMenu.addAction(self.saveFile)
        self.addBlack.clicked.connect(self.addBN)
        self.addWhite.clicked.connect(self.addWN)
        self.deleteButton.clicked.connect(self.deleteN)
        self.exportButton.clicked.connect(self.exportE)
        self.loginButton.clicked.connect(self.loginClicked)
        self.filterBlackList.clicked.connect(self.filterB)
        self.filterWhiteList.clicked.connect(self.filterW)
        self.addWhite.setStyleSheet("color: Green;")
        self.addBlack.setStyleSheet("color: red;")
        self.addWhite.setEnabled(False)
        self.addBlack.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        pixmap = QtGui.QPixmap(file_path(filename=resource_path('HikLogo.png')))
        self.graphicsLabel.setPixmap(pixmap.scaled(150, 100, QtCore.Qt.KeepAspectRatio))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HikVision Plate Export & Import"))
        self.label.setText(_translate("MainWindow", "Ip Address"))
        self.ipEdit.setInputMask(_translate("MainWindow", "000.000.000.000;_"))
        self.ipEdit.setText(_translate("MainWindow", "192.0.0.90"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.userEdit.setText(_translate("MainWindow", "admin"))
        self.userEdit.setPlaceholderText(_translate("MainWindow", "username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.passwdEdit.setText(_translate("MainWindow", "h1kv1s10n"))
        self.passwdEdit.setPlaceholderText(_translate("MainWindow", "password"))
        self.loginButton.setText(_translate("MainWindow", "login"))
        self.addBlack.setText(_translate("MainWindow", "Add BlackList"))
        self.addWhite.setText(_translate("MainWindow", "Add WhiteList"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.deviceModelLabel.setText(_translate("MainWindow", "Device Model:"))
        self.firmwareVLabel.setText(_translate("MainWindow", "Firmware Version:"))
        self.deviceNamelabel.setText(_translate("MainWindow", "Device  Name:"))
        self.menufile.setTitle(_translate("MainWindow", "file"))




    def loginClicked(self):
        if self.logout==1:
                ipAddress = self.ipEdit.text()
                self.user = self.userEdit.text()
                self.passwd = self.passwdEdit.text()
                self.ipAddress0 = str("http://" + ipAddress)
                (ok, status)=connect_getPlate(host=self.ipAddress0, usr=self.user, passwd=self.passwd)
                if (ok==200) or (ok==999):
                    if ok==999:
                        self.NVR=True
                    if ok == 200:
                        self.NVR =False
                    (ok, status_load)=self.readXls_loadT(status)
                    if ok==-1:
                        QtWidgets.QMessageBox.information(self.MainWindow, "ReadXLs Error", status_load)
                        return
                    self.loadDevInfo()
                    self.passwdEdit.setEnabled(False)
                    self.userEdit.setEnabled(False)
                    self.ipEdit.setEnabled(False)
                    self.addWhite.setEnabled(True)
                    self.saveFile.setEnabled(True)
                    self.addBlack.setEnabled(True)
                    self.deleteButton.setEnabled(True)
                    self.exportButton.setEnabled(True)
                    self.filterWhiteList.setEnabled(True)
                    self.filterBlackList.setEnabled(True)
                    self.searchInput.setEnabled(True)
                    self.loginButton.setText("Log out")
                    self.logout=0
                else:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Login Error", status)
        else:
            self.addBlack.setEnabled(False)
            self.addWhite.setEnabled(False)
            self.deleteButton.setEnabled(False)
            self.exportButton.setEnabled(False)
            self.saveFile.setEnabled(False)
            self.filterWhiteList.setEnabled(False)
            self.filterBlackList.setEnabled(False)
            self.searchInput.setEnabled(False)
            self.passwdEdit.setEnabled(True)
            self.userEdit.setEnabled(True)
            self.ipEdit.setEnabled(True)
            self.loginButton.setText("Log in")
            self.clear()
            self.logout=1
            self.NVR=False

    def loadDevInfo(self):
        dicJ=connect_getDevInfo(host=self.ipAddress0, usr=self.user, passwd=self.passwd)
        if dicJ[0]==-1:
            QtWidgets.QMessageBox.information(self.MainWindow, "Login Error", dicJ[1])
        else:
            self.deviceName.setText(dicJ[0])
            self.deviceModel.setText(dicJ[1])
            self.firmwareV.setText(dicJ[2])



    def readXls_loadT(self, status):
        try:
            book=xlrd.open_workbook(file_contents=status)
        except xlrd.biffh.XLRDError as e:
            return (-1, "problems reading data from an Excel file")
        first_sheet=book.sheet_by_index(0)
        column_p=first_sheet.col_values(1)
        column_p=column_p[1:]
        column_t=first_sheet.col_values(2)
        column_t=column_t[1:]
        row= len(column_p)
        self.createTable(row_n=row, column_n=2, plate_list=column_p, black_list=column_t)
        return (200, "succeed")



    def exportE(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.MainWindow, "QFileDialog.getSaveFileName()", "",
                                                  "Text Files (*.xls)")
        if fileName:
            listP = self.list_p[:]
            listB = self.list_b[:]
            book = Workbook()
            sheet1 = book.add_sheet("sheet1")
            row_0 = sheet1.row(0)
            row_0.write(0, "No")
            row_0.write(1, "Plate Num")
            row_0.write(2, "Group(0 black list, 1 white list)")
            for num in range(len(listP)):
                row = sheet1.row(num + 1)
                row.write(0, num)
                row.write(1, listP[num])
                row.write(2, listB[num])
            try:
                book.save(fileName)
            except OSError as e:
                QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error",
                                                  "Can't write file to the directory, check the access")
                return

    def filterB(self):
        if self.showB==0:
            for row in range(self.tableWidget.rowCount()):
                item=self.tableWidget.item(row, 1)
                if item.text()!="BlackList":
                    self.tableWidget.setRowHidden(item.row(), True)
            self.filterBlackList.setText("Show All")
            self.showB=1
        else:
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(row, False)
            self.filterBlackList.setText("Show blacklist only")
            self.showB = 0

    def filterW(self):
        if self.showW == 0:
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 1)
                if item.text() != "WhiteList":
                    self.tableWidget.setRowHidden(item.row(), True)
                else:
                    self.tableWidget.setRowHidden(item.row(), False)
            self.filterWhiteList.setText("Show All")
            self.showW = 1
        elif self.showW == 1:
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(row, False)
            self.filterWhiteList.setText("Show whitelist only")
            self.showW = 0


    def search(self):
        filter_text = str(self.searchInput.text()).lower()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if filter_text in str(item.text()).lower():
                self.tableWidget.setRowHidden(item.row(), False)
            else:
                self.tableWidget.setRowHidden(item.row(), True)



    def addBN(self):
        QDialog = QtWidgets.QDialog()
        numbers, ok = DialogBN.getNumber(QDialog)
        if ok == 1:
            if self.NVR:
                listP = self.list_p[:]
                listB = self.list_b[:]
                nm_rows = len(listP)
                row_index = 0
                for row_indext in range(nm_rows):
                    cell_val = listP[row_indext]
                    if cell_val == "":
                        for item in numbers:
                            listP[row_indext]=item
                            row_indext+=1
                        break
                    else:
                        row_index += 1

                row_index_t = row_index
                size = len(numbers)
                for ite in range(size):
                    listB[row_index_t]="0"
                    row_index_t+=1
            else:
                listP = self.list_p[:]
                listB = self.list_b[:]
                listP.extend(numbers)
                size = len(numbers)
                listofzeros = ["0"] * size
                listB.extend(listofzeros)
            book = Workbook()
            sheet1 = book.add_sheet("sheet1")
            row_0 = sheet1.row(0)
            row_0.write(0, "No")
            row_0.write(1, "Plate Num")
            row_0.write(2, "Group(0 black list, 1 white list)")
            for num in range(len(listP)):
                row = sheet1.row(num + 1)
                row.write(0, num)
                row.write(1, listP[num])
                row.write(2, listB[num])
            try:
                # book.save("fileName1.xls")
                f = io.BytesIO()
                book.save(f)
                data = f.getvalue()
                f.close()

            except OSError as e:
                QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error",
                                                  "Can't write file to the stream, check the access to ram")
                return
            if self.NVR:
                (ok, status) = connect_putPlateNVR(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                if ok != 200:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error", status)
                else:
                    row = len(listP)
                    self.refreshTable(row_n=row, column_n=2, plate_list=listP, black_list=listB)
            else:
                (ok, status) = connect_putPlate(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                if ok != 200:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error", status)
                else:
                    row = len(listP)
                    self.refreshTable(row_n=row, column_n=2, plate_list=listP, black_list=listB)




    def addWN(self):
        QDialog = QtWidgets.QDialog()
        numbers, ok = DialogWN.getNumber(QDialog)
        if ok == 1:
            if self.NVR:
                listP = self.list_p[:]
                listB = self.list_b[:]
                nm_rows = len(listP)
                row_index = 0
                for row_indext in range(nm_rows):
                    cell_val = listP[row_indext]
                    if cell_val == "":
                        for item in numbers:
                            listP[row_indext]=item
                            row_indext+=1
                        break
                    else:
                        row_index += 1

                row_index_t = row_index
                size = len(numbers)
                for ite in range(size):
                    listB[row_index_t]="1"
                    row_index_t+=1
            else:
                listP = self.list_p[:]
                listB = self.list_b[:]
                listP.extend(numbers)
                size = len(numbers)
                listofzeros = ["1"] * size
                listB.extend(listofzeros)
            book = Workbook()
            sheet1 = book.add_sheet("sheet1")
            row_0 = sheet1.row(0)
            row_0.write(0, "No")
            row_0.write(1, "Plate Num")
            row_0.write(2, "Group(0 black list, 1 white list)")
            for num in range(len(listP)):
                row = sheet1.row(num + 1)
                row.write(0, num)
                row.write(1, listP[num])
                row.write(2, listB[num])
            try:
                f = io.BytesIO()
                book.save(f)
                data = f.getvalue()
                f.close()

            except OSError as e:
                QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error",
                                                  "Can't write file to the stream, check the access to ram")
                return
            if self.NVR:
                (ok, status) = connect_putPlateNVR(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                if ok != 200:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error", status)
                else:
                    row = len(listP)
                    self.refreshTable(row_n=row, column_n=2, plate_list=listP, black_list=listB)
            else:
                (ok, status) = connect_putPlate(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                if ok != 200:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Add Number Error", status)
                else:
                    row = len(listP)
                    self.refreshTable(row_n=row, column_n=2, plate_list=listP, black_list=listB)

    def clear(self):
        self.tableWidget.setRowCount(0)
        self.deviceName.clear()
        self.deviceModel.clear()
        self.firmwareV.clear()

    def deleteN(self):
        if len(self.tableWidget.selectedItems()):
            selections = self.tableWidget.selectionModel()
            selectedsList = selections.selectedRows()
            rows = []
            for r in selectedsList:
                rows.append(r.row())
            if len(rows) == 0:
                for item in self.tableWidget.selectedItems():
                    rows.append(item.row())
            rr = QtWidgets.QMessageBox.question(self.MainWindow, "Warning", "Do you wanna delete all "+str(len(rows))+" numbers",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            if rr == QtWidgets.QMessageBox.Yes:
                if len(rows)==self.tableWidget.rowCount():
                    QtWidgets.QMessageBox.information(self.MainWindow, "Delete Error", "You cant delete all numbers")
                    return (-1, "You cant delete all numbers")

                listP = self.list_p[:]
                listB = self.list_b[:]
                for index in sorted(rows, reverse=True):
                    del listB[index]
                    del listP[index]
                if self.NVR:
                    listP+=[""]*(2048-len(listP))
                    listB += [""] * (2048 - len(listB))
                book =Workbook()
                sheet1 = book.add_sheet("sheet1")
                row_0 = sheet1.row(0)
                row_0.write(0, "No")
                row_0.write(1, "Plate Num")
                row_0.write(2, "Group(0 black list, 1 white list)")
                for num in range(len(listP)):
                    row = sheet1.row(num + 1)
                    row.write(0, num)
                    row.write(1, listP[num])
                    row.write(2, listB[num])
                try:
                    f = io.BytesIO()
                    book.save(f)
                    data = f.getvalue()
                    f.close()

                except OSError as e:
                    QtWidgets.QMessageBox.information(self.MainWindow, "Delete Error",
                                                      "Can't write data to the stream, check the access to ram")
                    return
                if self.NVR:
                    (ok, status) = connect_putPlateNVR(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                else:
                    (ok, status) = connect_putPlate(host=self.ipAddress0, usr=self.user, passwd=self.passwd, data=data)
                if ok!=200:
                    if ok==-400:
                        QtWidgets.QMessageBox.information(self.MainWindow, "Delete Error", "Excel format is wrong!")
                    QtWidgets.QMessageBox.information(self.MainWindow, "Delete Error", status)
                else:
                    row = len(listP)
                    self.refreshTable(row_n=row, column_n=2, plate_list=listP, black_list=listB)

    def createTable(self, row_n, column_n, plate_list, black_list):
        nm_rows=row_n
        row_index=0
        for row_indext in range(nm_rows):
            cell_val = plate_list[row_indext]
            if cell_val=="":
                row_index=row_indext
                break
            else:
                row_index+=1
        self.rowIndex=row_index
        self.tableWidget.setRowCount(row_index)
        self.tableWidget.setColumnCount(column_n)
        columnNames=["Plate Numbers", "Type"]
        self.tableWidget.setHorizontalHeaderLabels(columnNames)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_p=plate_list
        self.list_b=black_list
        for index, val in enumerate(self.list_p):
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(val)))
        for index, val in enumerate(self.list_b):
            if val!="1" and val!=1:
                tmp =QtWidgets.QTableWidgetItem("BlackList")
                tmp.setBackground(QtGui.QColor("red"))
                self.tableWidget.setItem(index, 1, tmp)
            else:
                tmp = QtWidgets.QTableWidgetItem("WhiteList")
                tmp.setBackground(QtGui.QColor("Green"))
                self.tableWidget.setItem(index, 1, tmp)


    def refreshTable(self, row_n, column_n, plate_list, black_list):
        nm_rows = row_n
        row_index = 0
        for row_indext in range(nm_rows):
            cell_val = plate_list[row_indext]
            if cell_val == "":
                row_index = row_indext
                break
            else:
                row_index += 1
        self.rowIndex = row_index
        self.tableWidget.setRowCount(row_index)
        self.tableWidget.setColumnCount(column_n)
        self.list_p = plate_list
        self.list_b = black_list
        for index, val in enumerate(self.list_p):
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(val)))
        for index, val in enumerate(self.list_b):
            if val!="1" and val!=1:
                tmp = QtWidgets.QTableWidgetItem("BlackList")
                tmp.setBackground(QtGui.QColor("red"))
                self.tableWidget.setItem(index, 1, tmp)
            else:
                tmp = QtWidgets.QTableWidgetItem("WhiteList")
                tmp.setBackground(QtGui.QColor("Green"))
                self.tableWidget.setItem(index, 1, tmp)
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(row, False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



