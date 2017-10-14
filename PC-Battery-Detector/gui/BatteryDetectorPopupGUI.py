# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatteryDetectorPopup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_batteryDetectorPopup_dialog(object):
    def setupUi(self, batteryDetectorPopup_dialog):
        batteryDetectorPopup_dialog.setObjectName("batteryDetectorPopup_dialog")
        batteryDetectorPopup_dialog.setWindowModality(QtCore.Qt.WindowModal)
        batteryDetectorPopup_dialog.resize(567, 109)
        batteryDetectorPopup_dialog.setStyleSheet("QDialog#batteryDetectorPopup_dialog{\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        batteryDetectorPopup_dialog.setModal(False)
        self.close_btn = QtWidgets.QPushButton(batteryDetectorPopup_dialog)
        self.close_btn.setGeometry(QtCore.QRect(480, 72, 75, 31))
        self.close_btn.setStyleSheet("QPushButton#close_btn{\n"
"background-color:rgb(255, 0, 0);color:rgb(255, 255, 255)\n"
"\n"
"}")
        self.close_btn.setObjectName("close_btn")
        self.alert_text = QtWidgets.QLabel(batteryDetectorPopup_dialog)
        self.alert_text.setGeometry(QtCore.QRect(100, 10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.alert_text.setFont(font)
        self.alert_text.setStyleSheet("QLabel#alert_text{\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.alert_text.setObjectName("alert_text")
        self.notify_text = QtWidgets.QLabel(batteryDetectorPopup_dialog)
        self.notify_text.setGeometry(QtCore.QRect(100, 50, 171, 16))
        self.notify_text.setStyleSheet("QLabel#notify_text{\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.notify_text.setObjectName("notify_text")

        self.retranslateUi(batteryDetectorPopup_dialog)
        QtCore.QMetaObject.connectSlotsByName(batteryDetectorPopup_dialog)

    def retranslateUi(self, batteryDetectorPopup_dialog):
        _translate = QtCore.QCoreApplication.translate
        batteryDetectorPopup_dialog.setWindowTitle(_translate("batteryDetectorPopup_dialog", "e~BD"))
        self.close_btn.setText(_translate("batteryDetectorPopup_dialog", "Close"))
        self.alert_text.setText(_translate("batteryDetectorPopup_dialog", "Your battery is running low (9%)"))
        self.notify_text.setText(_translate("batteryDetectorPopup_dialog", "You might want to charge your PC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    batteryDetectorPopup_dialog = QtWidgets.QDialog()
    ui = Ui_batteryDetectorPopup_dialog()
    ui.setupUi(batteryDetectorPopup_dialog)
    batteryDetectorPopup_dialog.show()
    sys.exit(app.exec_())

