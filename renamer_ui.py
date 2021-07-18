# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renamer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 400))
        MainWindow.setMaximumSize(QtCore.QSize(900, 400))
        MainWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 150, 731, 86))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.dir_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dir_label.setFont(font)
        self.dir_label.setObjectName("dir_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dir_label)
        self.dir_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dir_input.setFont(font)
        self.dir_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dir_input.setObjectName("dir_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dir_input)
        self.delim_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.delim_label.setFont(font)
        self.delim_label.setObjectName("delim_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.delim_label)
        self.delim_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delim_input.sizePolicy().hasHeightForWidth())
        self.delim_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delim_input.setFont(font)
        self.delim_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delim_input.setObjectName("delim_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delim_input)
        self.delim_location_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.delim_location_label.setFont(font)
        self.delim_location_label.setObjectName("delim_location_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.delim_location_label)
        self.delim_location_input = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delim_location_input.sizePolicy().hasHeightForWidth())
        self.delim_location_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.delim_location_input.setFont(font)
        self.delim_location_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delim_location_input.setObjectName("delim_location_input")
        self.delim_location_input.addItem("")
        self.delim_location_input.addItem("")
        self.delim_location_input.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.delim_location_input)
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(390, 330, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.go_button.setFont(font)
        self.go_button.setStyleSheet("color: rgb(0, 170, 0);")
        self.go_button.setObjectName("go_button")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(375, 30, 151, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.go_button.clicked.connect(self.go_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Renamer"))
        self.dir_label.setText(_translate("MainWindow", "File Directory:"))
        self.delim_label.setText(_translate("MainWindow", "Delimiter:"))
        self.delim_location_label.setText(_translate("MainWindow", "Delimiter Location:"))
        self.delim_location_input.setItemText(0, _translate("MainWindow", "----------"))
        self.delim_location_input.setItemText(1, _translate("MainWindow", "Front"))
        self.delim_location_input.setItemText(2, _translate("MainWindow", "Back"))
        self.go_button.setText(_translate("MainWindow", "GO"))
        self.title_label.setText(_translate("MainWindow", "File Renamer"))

    def go_clicked(self):
        in_dir = str(self.dir_input.text())
        in_delim = str(self.delim_input.text())
        in_delim_location = str(self.delim_location_input.currentText())
        files = os.listdir(in_dir)

        allowed_types = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        print(f"Renaming files in \"{in_dir}\"")

        if in_delim != "" and in_delim_location != "":
            file_counter = 1
            for file in files:
                file_name = file
                file_type = "." + file_name.split(".")[-1]
                if in_delim in file_name and file_type in allowed_types:
                    if in_delim_location == "Front":
                        old_full = in_dir + '\\' + file_name
                        new_file_name = file_name.split(in_delim)[0] + file_type

                        new_file_name = check_name(new_file_name, in_dir)

                        new_full = in_dir + '\\' + new_file_name
                        os.rename(old_full, new_full)
                        show_new = new_full.split('\\')[-1]
                        print(f"{file_name} -> {show_new}")
                        file_counter += 1
                    elif in_delim_location == "Back":
                        old_full = in_dir + '\\' + file_name
                        new_full = in_dir + '\\' + file_name.split(in_delim)[-1]
                        os.rename(old_full, new_full)
                        show_new = new_full.split('\\')[-1]
                        print(f"{file_name} -> {show_new}")
                        file_counter += 1

        else:
            file_counter = 1
            for file in files:
                file_name = file
                old_full = in_dir + '\\' + file_name
                file_type = "." + file_name.split(".")[-1]
                new_full = in_dir + '\\' + str(file_counter) + file_type
                os.rename(old_full, new_full)
                print(f"{old_full} -> {new_full}")
                file_counter += 1
        print("DONE!\n--------------------------------")


def check_name(name, this_dir):
    files = os.listdir(this_dir)
    file_type = "." + str(name.split(".")[-1])
    file_prefix_list = name.split(".")[:-1]
    file_prefix = ''.join([str(elem) for elem in file_prefix_list])
    new_name = name
    counter = 2
    while True:
        if new_name in files:
            new_name = file_prefix + "-" + str(counter) + file_type
            counter += 1
        else:
            return new_name




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
