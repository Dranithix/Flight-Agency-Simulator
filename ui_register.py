#-------------------------------------------------------------------------------
# Name:        DSCTravelAgency
# Purpose:     Allows clients of a travel agency to book a flight.
#
# Author:      Kenta Iwasaki
#
# Created:     29/05/2014
# Copyright:   (c) Kenta Iwasaki 2014
# Licence:     N/A
#-------------------------------------------------------------------------------

# PyQT Imports
from PyQt5 import QtCore, QtGui, QtWidgets

# UI Layout and Setup
class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName("RegisterDialog")
        RegisterDialog.resize(349, 131)
        self.gridLayoutWidget = QtWidgets.QWidget(RegisterDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtPass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.gridLayout.addWidget(self.txtPass, 1, 1, 1, 1)
        self.txtName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtName.setObjectName("txtName")
        self.gridLayout.addWidget(self.txtName, 0, 1, 1, 1)
        self.txtDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.txtDate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.txtDate.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.txtDate.setCalendarPopup(True)
        self.txtDate.setObjectName("txtDate")
        self.gridLayout.addWidget(self.txtDate, 2, 1, 1, 1)
        self.btnRegister = QtWidgets.QPushButton(RegisterDialog)
        self.btnRegister.setGeometry(QtCore.QRect(220, 100, 121, 23))
        self.btnRegister.setObjectName("btnRegister")

        self.retranslateUi(RegisterDialog)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "DSC :: Register"))
        self.label.setText(_translate("RegisterDialog", "Name:"))
        self.label_3.setText(_translate("RegisterDialog", "Date of Birth: "))
        self.label_2.setText(_translate("RegisterDialog", "Password:"))
        self.btnRegister.setText(_translate("RegisterDialog", "Register"))

