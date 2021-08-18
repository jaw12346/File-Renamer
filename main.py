from renamer_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

ALLOWED_TYPES = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]


def selected_renamer(in_dir, files, delimiter, delimiter_location, keep_where):

    if delimiter_location == "First":
        if keep_where == "Before Delimiter":
            print(f"\tFiles will be renamed based on the text before the first delimiter.")
        if keep_where == "After Delimiter":
            print(f"\tFiles will be renamed based on the text after the first delimiter.")
    elif delimiter_location == "Last":
        if keep_where == "Before Delimiter":
            print(f"\tFiles will be renamed based on the text before the last delimiter.")
        if keep_where == "After Delimiter":
            print(f"\tFiles will be renamed based on the text after the last delimiter.")

    file_counter = 1
    for file in files:
        file_name = file
        file_type = "." + file_name.split(".")[-1]
        if delimiter in file_name and file_type in ALLOWED_TYPES:
            if delimiter_location == "First":
                old_full = in_dir + '\\' + file_name

                if keep_where == "Before Delimiter":
                    new_file_name = file_name.split(delimiter)[0]
                elif keep_where == "After Delimiter":
                    new_file_name = file_name.split(delimiter)[1]

                if file_type not in new_file_name:
                    new_file_name += file_type

                new_file_name = check_name(new_file_name, in_dir)
                new_full = in_dir + '\\' + new_file_name
                os.rename(old_full, new_full)
                show_new = new_full.split('\\')[-1]
                print(f"({file_counter})\t{file_name} -> {show_new}")
                file_counter += 1
            elif delimiter_location == "Last":
                old_full = in_dir + '\\' + file_name

                if keep_where == "Before Delimiter":
                    new_file_name = file_name.split(delimiter)[-2]
                elif keep_where == "After Delimiter":
                    new_file_name = file_name.split(delimiter)[-1]

                if file_type not in new_file_name:
                    new_file_name += file_type

                new_file_name = check_name(new_file_name, in_dir)
                new_full = in_dir + '\\' + new_file_name
                os.rename(old_full, new_full)
                show_new = new_full.split('\\')[-1]
                print(f"({file_counter})\t{file_name} -> {show_new}")
                file_counter += 1


def numerical_renamer(in_dir, files):
    print("\tFiles will be renamed numerically based on the order in which "
          "they appear in the directory.")
    file_counter = 1
    for file in files:
        file_name = file
        file_type = "." + file_name.split(".")[-1]
        if file_type in ALLOWED_TYPES:
            file_name = file
            old_full = in_dir + '\\' + file_name
            file_type = "." + file_name.split(".")[-1]
            new_file_name = str(file_counter) + file_type
            new_file_name = check_name(new_file_name, in_dir)
            new_full = in_dir + '\\' + new_file_name
            os.rename(old_full, new_full)
            show_new = new_full.split('\\')[-1]
            print(f"({file_counter})\t{file_name} -> {show_new}")
            file_counter += 1


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
            return str(new_name)


def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
