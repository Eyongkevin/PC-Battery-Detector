# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sun Oct 08 16:55:11 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_frame(object):
    def setupUi(self, MainWindow_frame):
        MainWindow_frame.setObjectName("MainWindow_frame")
        MainWindow_frame.resize(141, 219)
        MainWindow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        MainWindow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting_btn = QtWidgets.QPushButton(MainWindow_frame)
        self.setting_btn.setGeometry(QtCore.QRect(0, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setting_btn.setFont(font)
        self.setting_btn.setObjectName("setting_btn")
        self.about_btn = QtWidgets.QPushButton(MainWindow_frame)
        self.about_btn.setGeometry(QtCore.QRect(0, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.about_btn.setFont(font)
        self.about_btn.setStyleSheet("")
        self.about_btn.setObjectName("about_btn")
        self.exit_btn = QtWidgets.QPushButton(MainWindow_frame)
        self.exit_btn.setGeometry(QtCore.QRect(0, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("color:red")
        self.exit_btn.setObjectName("exit_btn")
        self.BatteryLevelDisplay_frame = QtWidgets.QFrame(MainWindow_frame)
        self.BatteryLevelDisplay_frame.setGeometry(QtCore.QRect(0, 0, 141, 91))
        self.BatteryLevelDisplay_frame.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.BatteryLevelDisplay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BatteryLevelDisplay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BatteryLevelDisplay_frame.setObjectName("BatteryLevelDisplay_frame")
        self.batteryLevel_label = QtWidgets.QLabel(self.BatteryLevelDisplay_frame)
        self.batteryLevel_label.setGeometry(QtCore.QRect(20, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.batteryLevel_label.setFont(font)
        self.batteryLevel_label.setStyleSheet("color:rgb(255, 255, 255)")
        self.batteryLevel_label.setObjectName("batteryLevel_label")

        self.retranslateUi(MainWindow_frame)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_frame)

    def retranslateUi(self, MainWindow_frame):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_frame.setWindowTitle(_translate("MainWindow_frame", "Frame"))
        self.setting_btn.setText(_translate("MainWindow_frame", "Setting"))
        self.about_btn.setText(_translate("MainWindow_frame", "About"))
        self.exit_btn.setText(_translate("MainWindow_frame", "Exit"))
        self.batteryLevel_label.setText(_translate("MainWindow_frame", "10%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_frame = QtWidgets.QFrame()
    ui = Ui_MainWindow_frame()
    ui.setupUi(MainWindow_frame)
    MainWindow_frame.show()
    sys.exit(app.exec_())

