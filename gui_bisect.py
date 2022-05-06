# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyautogui as au
import time
import subprocess



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(688, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.log_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.log_textEdit.setGeometry(QtCore.QRect(370, 10, 311, 311))
        self.log_textEdit.setReadOnly(False)
        self.log_textEdit.setObjectName("log_textEdit")

        self.sorce_path_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sorce_path_LineEdit.setGeometry(QtCore.QRect(110, 10, 251, 20))
        self.sorce_path_LineEdit.setObjectName("sorce_path_LineEdit")

        self.sorce_path_lable = QtWidgets.QLabel(self.centralwidget)
        self.sorce_path_lable.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.sorce_path_lable.setObjectName("sorce_path_lable")

        self.exe_path_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.exe_path_LineEdit.setGeometry(QtCore.QRect(110, 40, 251, 20))
        self.exe_path_LineEdit.setObjectName("exe_path_LineEdit")

        self.exe_path_lable = QtWidgets.QLabel(self.centralwidget)
        self.exe_path_lable.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.exe_path_lable.setObjectName("exe_path_lable")

        self.exe_file_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.exe_file_LineEdit.setGeometry(QtCore.QRect(110, 70, 170, 20))
        self.exe_file_LineEdit.setObjectName("exe_file_LineEdit")

        self.exe_file_lable = QtWidgets.QLabel(self.centralwidget)
        self.exe_file_lable.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.exe_file_lable.setObjectName("exe_file_lable")

        self.image_lable = QtWidgets.QLabel(self.centralwidget)
        self.image_lable.setGeometry(QtCore.QRect(10, 120, 67, 13))
        self.image_lable.setObjectName("image_lable")

        self.image_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_lineEdit.setGeometry(QtCore.QRect(10, 140, 131, 20))
        self.image_lineEdit.setObjectName("image_lineEdit")

        self.action_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.action_comboBox.setGeometry(QtCore.QRect(150, 140, 131, 22))
        self.action_comboBox.addItems(["Click", "RMB_Click", "DoubleClick","MoveCursor", "TypeText", "Sleep", "Screenshot"])
        self.action_comboBox.setObjectName("action_comboBox")

        self.image_type_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.image_type_comboBox.setGeometry(QtCore.QRect(10, 180, 60, 22))
        self.image_type_comboBox.addItems(["png", "jpeg", "jpg", "ico", "bmp", "raw", "tiff"])
        self.image_type_comboBox.setObjectName("image_type_comboBox")

        self.image_type_label = QtWidgets.QLabel(self.centralwidget)
        self.image_type_label.setGeometry(QtCore.QRect(10, 165, 55, 13))
        self.image_type_label.setObjectName("image_type_label")

        self.action_label = QtWidgets.QLabel(self.centralwidget)
        self.action_label.setGeometry(QtCore.QRect(150, 120, 47, 13))
        self.action_label.setObjectName("action_label")

        self.record_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.record_pushButton.setGeometry(QtCore.QRect(290, 140, 75, 23))
        self.record_pushButton.setObjectName("record_pushButton")

        self.run_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.run_pushButton.setGeometry(QtCore.QRect(290, 170, 75, 23))
        self.run_pushButton.setObjectName("run_pushButton")

        self.run_loop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.run_loop_pushButton.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.run_loop_pushButton.setObjectName("run_loop_pushButton")

        self.error_log = QtWidgets.QTextEdit(self.centralwidget)
        self.error_log.setGeometry(QtCore.QRect(10, 250, 350, 70))
        self.error_log.setObjectName("error_log")

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(10, 200, 350, 70))
        self.error_label.setObjectName("error_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sorce_path_lable.setText(_translate("MainWindow", "Images folder path"))
        self.exe_path_lable.setText(_translate("MainWindow", "exe-files folder path"))
        self.exe_file_lable.setText(_translate("MainWindow", "exe-file"))
        self.image_lable.setText(_translate("MainWindow", "Image/Text"))
        self.image_type_label.setText(_translate("MainWindow", "Image type"))
        self.error_label.setText(_translate("MainWindow", "ERROR LOG"))
        self.action_label.setText(_translate("MainWindow", "Action"))
        self.record_pushButton.setText(_translate("MainWindow", "Record"))
        self.run_pushButton.setText(_translate("MainWindow", "Run"))
        self.run_loop_pushButton.setText(_translate("MainWindow", "Run loop"))

    def add_functions(self):
        self.record_pushButton.clicked.connect(lambda: self.action_recorder())
        self.run_pushButton.clicked.connect(lambda: self.run_scenario())

    DEFAULT_SLEEP_TIME = 1
    DEFAULT_CONFIDENCE = .9


    def run_loop(self, exe_path, exe_file):
        for dir in os.listdir(self.exe_path_LineEdit.text()):
            subprocess.call(f'{self.exe_path_LineEdit.text()}{dir}\{self.exe_file_LineEdit.text()}')
            time.sleep(10)
            self.run_scenario()
            time.sleep(1)
            au.screenshot(f'{dir}.png')
            #os.system(f'taskkill /f /im  {self.exe_file_LineEdit}')


    def click_on_screen(self, template):
        try:
            au.click(au.locateOnScreen(f'{self.sorce_path_LineEdit.text()}{template}', confidence=self.DEFAULT_CONFIDENCE))
            time.sleep(self.DEFAULT_SLEEP_TIME)
        except Exception:
            self.error_log.append(f'ERROR: Can\'t find image: \"{self.sorce_path_LineEdit.text()}{template}\"')

    def RMB_click_on_screen(self, template):
        try:
            au.rightClick(au.locateOnScreen(f'{self.sorce_path_LineEdit.text()}{template}', confidence=self.DEFAULT_CONFIDENCE))
           #au.click(au.locateOnScreen(f'{self.sorce_path_LineEdit.text()}{template}', confidence=self.DEFAULT_CONFIDENCE))
            time.sleep(self.DEFAULT_SLEEP_TIME)
        except Exception:
            self.error_log.append(f'ERROR: Can\'t find image: \"{self.sorce_path_LineEdit.text()}{template}\"')

    def Move_cursor_to_image(self, template):
        try:
            au.moveTo(au.locateOnScreen(f'{self.sorce_path_LineEdit.text()}{template}', confidence=self.DEFAULT_CONFIDENCE))
            time.sleep(self.DEFAULT_SLEEP_TIME)
        except Exception:
            self.error_log.append(f'ERROR: Can\'t find image: \"{self.sorce_path_LineEdit.text()}{template}\"')

    def doubleclick_on_screen(self, template):
        try:
            au.doubleClick(au.locateOnScreen(f'{self.sorce_path_LineEdit.text()}{template}', confidence=self.DEFAULT_CONFIDENCE))
            time.sleep(self.DEFAULT_SLEEP_TIME)
        except Exception:
            self.error_log.append(f'ERROR: Can\'t find image: \"{self.sorce_path_LineEdit.text()}{template}\"')

    def type_users_text(self, text):
        try:
            au.typewrite(text)
            time.sleep(self.DEFAULT_SLEEP_TIME)
        except Exception:
            self.error_log.append(f'ERROR: Can\'t type: \"{text}\"')

    def users_set_sleep_time(self, sleep_time):
        try:
            time.sleep(int(sleep_time))
        except Exception:
            self.error_log.append(f'ERROR: Can\'t wait: \"{sleep_time}\" seconds')

    # def get_screenshot(self, sleep_time):
        # try:
        #     au.screenshot("test.png")
        # except Exception:
        #     self.error_log.append(f'ERROR: Can\'t save screenshot')

    def action_recorder(self):
        ignore_list =["TypeText", "Sleep", "Screenshot"]
        if self.action_comboBox.currentText() in ignore_list:
            self.log_textEdit.append(f'{self.image_lineEdit.text()}-->{self.action_comboBox.currentText()}')
        else:
            self.log_textEdit.append(f'{self.image_lineEdit.text()}.{self.image_type_comboBox.currentText()}-->{self.action_comboBox.currentText()}')

    def run_scenario(self):
        commands_list = []
        commands_list.append(self.log_textEdit.toPlainText().split('\n'))
        for command in commands_list[0]:
            try:
                if command.split('-->')[1] == 'Click':
                    self.click_on_screen(command.split('-->')[0])
                elif command.split('-->')[1] == 'RMB_Click':
                    self.RMB_click_on_screen(command.split('-->')[0])
                elif command.split('-->')[1] == 'DoubleClick':
                    self.doubleclick_on_screen(command.split('-->')[0])
                elif command.split('-->')[1] == 'MoveCursor':
                    self.doubleclick_on_screen(command.split('-->')[0])
                elif command.split('-->')[1] == 'TypeText':
                    self.type_users_text(command.split('-->')[0])
                elif command.split('-->')[1] == 'Sleep':
                    self.users_set_sleep_time(command.split('-->')[0])
                elif command.split('-->')[1] == 'Screenshot':
                    au.screenshot(f'{self.image_lineEdit.text()}.png')
            except Exception:
                self.error_log.append("WARRNING: Can\'t parse one of the line")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
