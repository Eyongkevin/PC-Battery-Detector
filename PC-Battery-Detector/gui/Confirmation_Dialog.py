# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Confirmation_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Confirmation_Dialog(object):
    def setupUi(self, Confirmation_Dialog):
        Confirmation_Dialog.setObjectName("Confirmation_Dialog")
        Confirmation_Dialog.resize(400, 133)
        self.Confirmation_buttonBox = QtWidgets.QDialogButtonBox(Confirmation_Dialog)
        self.Confirmation_buttonBox.setGeometry(QtCore.QRect(40, 100, 341, 32))
        self.Confirmation_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.Confirmation_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Confirmation_buttonBox.setObjectName("Confirmation_buttonBox")
        self.Confirmation_label = QtWidgets.QLabel(Confirmation_Dialog)
        self.Confirmation_label.setGeometry(QtCore.QRect(60, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Confirmation_label.setFont(font)
        self.Confirmation_label.setObjectName("Confirmation_label")

        self.retranslateUi(Confirmation_Dialog)
        self.Confirmation_buttonBox.accepted.connect(Confirmation_Dialog.accept)
        self.Confirmation_buttonBox.rejected.connect(Confirmation_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Confirmation_Dialog)

    def retranslateUi(self, Confirmation_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Confirmation_Dialog.setWindowTitle(_translate("Confirmation_Dialog", "Dialog"))
        self.Confirmation_label.setText(_translate("Confirmation_Dialog", "Do you really want to reset?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Confirmation_Dialog = QtWidgets.QDialog()
    ui = Ui_Confirmation_Dialog()
    ui.setupUi(Confirmation_Dialog)
    Confirmation_Dialog.show()
    sys.exit(app.exec_())

