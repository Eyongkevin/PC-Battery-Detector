# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerLevel_label = QtWidgets.QLabel(self.centralwidget)
        self.powerLevel_label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.powerLevel_label.setObjectName("powerLevel_label")
        self.batteryStatus_label = QtWidgets.QLabel(self.centralwidget)
        self.batteryStatus_label.setGeometry(QtCore.QRect(240, 10, 121, 16))
        self.batteryStatus_label.setObjectName("batteryStatus_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 80, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BatteryLevel_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatteryLevel_progressBar.setGeometry(QtCore.QRect(50, 40, 451, 23))
        self.BatteryLevel_progressBar.setProperty("value", 100)
        self.BatteryLevel_progressBar.setObjectName("BatteryLevel_progressBar")
        self.DisableAlam_label = QtWidgets.QLabel(self.centralwidget)
        self.DisableAlam_label.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.DisableAlam_label.setObjectName("DisableAlam_label")
        self.DisableAlarm_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.DisableAlarm_checkBox.setGeometry(QtCore.QRect(160, 120, 16, 17))
        self.DisableAlarm_checkBox.setText("")
        self.DisableAlarm_checkBox.setObjectName("DisableAlarm_checkBox")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 120, 21, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 130, 16, 81))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.AlarmPawerLevel_Label = QtWidgets.QLabel(self.centralwidget)
        self.AlarmPawerLevel_Label.setGeometry(QtCore.QRect(60, 150, 161, 16))
        self.AlarmPawerLevel_Label.setObjectName("AlarmPawerLevel_Label")
        self.AlarmPawerLevel_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.AlarmPawerLevel_spinBox.setGeometry(QtCore.QRect(230, 150, 42, 16))
        self.AlarmPawerLevel_spinBox.setMinimum(10)
        self.AlarmPawerLevel_spinBox.setObjectName("AlarmPawerLevel_spinBox")
        self.Repeat_Label = QtWidgets.QLabel(self.centralwidget)
        self.Repeat_Label.setGeometry(QtCore.QRect(60, 180, 71, 16))
        self.Repeat_Label.setObjectName("Repeat_Label")
        self.Repeat_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.Repeat_spinBox.setGeometry(QtCore.QRect(140, 180, 42, 16))
        self.Repeat_spinBox.setObjectName("Repeat_spinBox")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 200, 21, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.NotifyOnBatteryFull_Label = QtWidgets.QLabel(self.centralwidget)
        self.NotifyOnBatteryFull_Label.setGeometry(QtCore.QRect(40, 230, 181, 16))
        self.NotifyOnBatteryFull_Label.setObjectName("NotifyOnBatteryFull_Label")
        self.NotifyOnBatteryFull_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.NotifyOnBatteryFull_checkBox.setGeometry(QtCore.QRect(230, 230, 16, 17))
        self.NotifyOnBatteryFull_checkBox.setText("")
        self.NotifyOnBatteryFull_checkBox.setObjectName("NotifyOnBatteryFull_checkBox")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(270, 90, 20, 151))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.DisableSound_label = QtWidgets.QLabel(self.centralwidget)
        self.DisableSound_label.setGeometry(QtCore.QRect(320, 120, 71, 16))
        self.DisableSound_label.setObjectName("DisableSound_label")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(290, 130, 16, 101))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(300, 220, 21, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(300, 120, 21, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.DisableSound_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.DisableSound_checkBox.setGeometry(QtCore.QRect(420, 120, 16, 17))
        self.DisableSound_checkBox.setText("")
        self.DisableSound_checkBox.setObjectName("DisableSound_checkBox")
        self.setDefaultBeep_label = QtWidgets.QLabel(self.centralwidget)
        self.setDefaultBeep_label.setGeometry(QtCore.QRect(320, 150, 81, 16))
        self.setDefaultBeep_label.setObjectName("setDefaultBeep_label")
        self.BrowseSound_label = QtWidgets.QLabel(self.centralwidget)
        self.BrowseSound_label.setGeometry(QtCore.QRect(320, 180, 111, 16))
        self.BrowseSound_label.setObjectName("BrowseSound_label")
        self.setDefaultBeep_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.setDefaultBeep_checkBox.setGeometry(QtCore.QRect(420, 150, 16, 17))
        self.setDefaultBeep_checkBox.setText("")
        self.setDefaultBeep_checkBox.setObjectName("setDefaultBeep_checkBox")
        self.BrowseSound_btn = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseSound_btn.setGeometry(QtCore.QRect(354, 200, 51, 23))
        self.BrowseSound_btn.setObjectName("BrowseSound_btn")
        self.Reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_btn.setGeometry(QtCore.QRect(40, 260, 51, 23))
        self.Reset_btn.setObjectName("Reset_btn")
        self.Apply_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Apply_btn.setGeometry(QtCore.QRect(350, 300, 51, 23))
        self.Apply_btn.setObjectName("Apply_btn")
        self.Cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel_btn.setGeometry(QtCore.QRect(430, 300, 51, 23))
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.leveIndicator = QtWidgets.QLabel(self.centralwidget)
        self.leveIndicator.setGeometry(QtCore.QRect(230, 170, 31, 16))
        self.leveIndicator.setStyleSheet("color:rgb(190, 190, 190)")
        self.leveIndicator.setObjectName("leveIndicator")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.powerLevel_label.setText(_translate("MainWindow", "Power Level 100 %"))
        self.batteryStatus_label.setText(_translate("MainWindow", "Plugged in, Charging"))
        self.DisableAlam_label.setText(_translate("MainWindow", "Disable Alarm"))
        self.AlarmPawerLevel_Label.setText(_translate("MainWindow", "Alarm When Power Level Drop To"))
        self.Repeat_Label.setText(_translate("MainWindow", "Repeat Every "))
        self.NotifyOnBatteryFull_Label.setText(_translate("MainWindow", "Notify When Battery Is Fully Charged"))
        self.DisableSound_label.setText(_translate("MainWindow", "Disable Sound"))
        self.setDefaultBeep_label.setText(_translate("MainWindow", "Set Default Beep"))
        self.BrowseSound_label.setText(_translate("MainWindow", "Browse Sound To Play"))
        self.BrowseSound_btn.setText(_translate("MainWindow", "Browse"))
        self.Reset_btn.setText(_translate("MainWindow", "Reset"))
        self.Apply_btn.setText(_translate("MainWindow", "Apply"))
        self.Cancel_btn.setText(_translate("MainWindow", "Exit"))
        self.leveIndicator.setText(_translate("MainWindow", "10-99"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

