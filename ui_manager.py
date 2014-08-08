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
class Ui_ManagerDialog(object):
    def setupUi(self, ManagerDialog):
        ManagerDialog.setObjectName("ManagerDialog")
        ManagerDialog.resize(732, 382)
        self.gridLayoutWidget = QtWidgets.QWidget(ManagerDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 711, 361))
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
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.transactions = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.transactions.setObjectName("transactions")
        self.transactions.setColumnCount(8)
        self.transactions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.transactions, 3, 0, 1, 2)
        self.txtFinalIncome = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtFinalIncome.setObjectName("txtFinalIncome")
        self.gridLayout.addWidget(self.txtFinalIncome, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.txtIncome = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtIncome.setObjectName("txtIncome")
        self.gridLayout.addWidget(self.txtIncome, 0, 1, 1, 1)
        self.txtCommission = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtCommission.setObjectName("txtCommission")
        self.gridLayout.addWidget(self.txtCommission, 1, 1, 1, 1)

        self.retranslateUi(ManagerDialog)
        QtCore.QMetaObject.connectSlotsByName(ManagerDialog)

    def retranslateUi(self, ManagerDialog):
        _translate = QtCore.QCoreApplication.translate
        ManagerDialog.setWindowTitle(_translate("ManagerDialog", "DSC :: Manager Panel"))
        self.label.setText(_translate("ManagerDialog", "Final Income:"))
        self.label_3.setText(_translate("ManagerDialog", "Overall Income:"))
        item = self.transactions.horizontalHeaderItem(0)
        item.setText(_translate("ManagerDialog", "User ID"))
        item = self.transactions.horizontalHeaderItem(1)
        item.setText(_translate("ManagerDialog", "Date"))
        item = self.transactions.horizontalHeaderItem(2)
        item.setText(_translate("ManagerDialog", "Price"))
        item = self.transactions.horizontalHeaderItem(3)
        item.setText(_translate("ManagerDialog", "Airline"))
        item = self.transactions.horizontalHeaderItem(4)
        item.setText(_translate("ManagerDialog", "Ticket No."))
        item = self.transactions.horizontalHeaderItem(5)
        item.setText(_translate("ManagerDialog", "Billing Name"))
        item = self.transactions.horizontalHeaderItem(6)
        item.setText(_translate("ManagerDialog", "Billing Address"))
        item = self.transactions.horizontalHeaderItem(7)
        item.setText(_translate("ManagerDialog", "Phone Number"))
        self.txtFinalIncome.setText(_translate("ManagerDialog", "null"))
        self.label_4.setText(_translate("ManagerDialog", "Commission:"))
        self.txtIncome.setText(_translate("ManagerDialog", "null"))
        self.txtCommission.setText(_translate("ManagerDialog", "null"))

