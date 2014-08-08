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
class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(372, 99)
        self.gridLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 79))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtPass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.gridLayout.addWidget(self.txtPass, 1, 1, 1, 1)
        self.txtUser = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtUser.setObjectName("txtUser")
        self.gridLayout.addWidget(self.txtUser, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnRegister = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnRegister.setObjectName("btnRegister")
        self.gridLayout_2.addWidget(self.btnRegister, 0, 1, 1, 1)
        self.btnLogin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.gridLayout_2.addWidget(self.btnLogin, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "DSC :: Login"))
        self.label.setText(_translate("LoginDialog", "User ID: "))
        self.label_2.setText(_translate("LoginDialog", "Password: "))
        self.btnRegister.setText(_translate("LoginDialog", "Register"))
        self.btnLogin.setText(_translate("LoginDialog", "Login"))

