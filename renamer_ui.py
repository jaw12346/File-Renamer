# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'renamer.ui'
# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import os


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
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 150, 731, 138))
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
        font.setBold(True)
        font.setWeight(75)
        self.delim_location_input.setFont(font)
        self.delim_location_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delim_location_input.setObjectName("delim_location_input")
        self.delim_location_input.addItem("")
        self.delim_location_input.addItem("")
        self.delim_location_input.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.delim_location_input)
        self.keep_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.keep_label.setFont(font)
        self.keep_label.setObjectName("keep_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.keep_label)
        self.keep_input = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keep_input.sizePolicy().hasHeightForWidth())
        self.keep_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keep_input.setFont(font)
        self.keep_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.keep_input.setObjectName("keep_input")
        self.keep_input.addItem("")
        self.keep_input.addItem("")
        self.keep_input.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.keep_input)
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(390, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.go_button.setFont(font)
        self.go_button.setStyleSheet("color: rgb(0, 170, 0);")
        self.go_button.setObjectName("go_button")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(360, 30, 181, 23))
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

        self.go_button.clicked.connect(self.run_renamer)  # Driver for renaming functionality

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Renamer"))
        self.dir_label.setText(_translate("MainWindow", "File Directory:"))
        self.dir_input.setPlaceholderText(_translate("MainWindow", "Enter full directory here"))
        self.delim_label.setText(_translate("MainWindow", "Delimiter:"))
        self.delim_location_label.setText(_translate("MainWindow", "Delimiter Location:"))
        self.delim_location_input.setItemText(0, _translate("MainWindow", "------------------"))
        self.delim_location_input.setItemText(1, _translate("MainWindow", "First"))
        self.delim_location_input.setItemText(2, _translate("MainWindow", "Last"))
        self.keep_label.setText(_translate("MainWindow", "Keep Contents:"))
        self.keep_input.setItemText(0, _translate("MainWindow", "-----------------------"))
        self.keep_input.setItemText(1, _translate("MainWindow", "Before Delimiter"))
        self.keep_input.setItemText(2, _translate("MainWindow", "After Delimiter"))
        self.go_button.setText(_translate("MainWindow", "GO"))
        self.title_label.setText(_translate("MainWindow", "File Renamer"))

    def run_renamer(self):
        in_dir = str(self.dir_input.text())  # Directory where names will be changes
        in_delim = str(self.delim_input.text())  # Delimiter
        in_delim_location = str(self.delim_location_input.currentText())  # First or last delimiter
        keep_where = str(self.keep_input.currentText())  # Keep text before or after delimiter
        files = os.listdir(in_dir)  # Files in the provided directory

        if "-" in in_delim_location or "-" in keep_where or in_delim == "":
            in_delim_location = ""
            keep_where = ""
            in_delim = ""

        print(f"Renaming files in \"{in_dir}\"")

        if in_delim != "" and in_delim_location != "" and keep_where != "":
            selected_renamer(in_dir, files, in_delim, in_delim_location, keep_where)
        else:
            numerical_renamer(in_dir, files)

        print("DONE!\n--------------------------------")

        # TODO: Maybe add a backup folder and a dialog asking if the files were renamed correctly.
        #  Delete the folder contents if yes.

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
