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
class Ui_FlightDialog(object):
    def setupUi(self, FlightDialog):
        FlightDialog.setObjectName("FlightDialog")
        FlightDialog.resize(794, 340)
        self.FlightInformation = QtWidgets.QGroupBox(FlightDialog)
        self.FlightInformation.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.FlightInformation.setObjectName("FlightInformation")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.FlightInformation)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 361, 204))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtReturnTakeoff = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtReturnTakeoff.setEnabled(True)
        self.txtReturnTakeoff.setReadOnly(True)
        self.txtReturnTakeoff.setObjectName("txtReturnTakeoff")
        self.gridLayout_2.addWidget(self.txtReturnTakeoff, 5, 1, 1, 1)
        self.txtReturnLanding = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtReturnLanding.setEnabled(True)
        self.txtReturnLanding.setReadOnly(True)
        self.txtReturnLanding.setObjectName("txtReturnLanding")
        self.gridLayout_2.addWidget(self.txtReturnLanding, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.txtAirline = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtAirline.setEnabled(True)
        self.txtAirline.setReadOnly(True)
        self.txtAirline.setObjectName("txtAirline")
        self.gridLayout_2.addWidget(self.txtAirline, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.txtClass = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtClass.setEnabled(True)
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.gridLayout_2.addWidget(self.txtClass, 2, 1, 1, 1)
        self.txtPrice = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtPrice.setEnabled(True)
        self.txtPrice.setReadOnly(True)
        self.txtPrice.setObjectName("txtPrice")
        self.gridLayout_2.addWidget(self.txtPrice, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)
        self.txtDepartLanding = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtDepartLanding.setEnabled(True)
        self.txtDepartLanding.setReadOnly(True)
        self.txtDepartLanding.setObjectName("txtDepartLanding")
        self.gridLayout_2.addWidget(self.txtDepartLanding, 4, 1, 1, 1)
        self.txtDepartTakeoff = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtDepartTakeoff.setEnabled(True)
        self.txtDepartTakeoff.setReadOnly(True)
        self.txtDepartTakeoff.setObjectName("txtDepartTakeoff")
        self.gridLayout_2.addWidget(self.txtDepartTakeoff, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 7, 0, 1, 1)
        self.txtLayover = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtLayover.setReadOnly(True)
        self.txtLayover.setObjectName("txtLayover")
        self.gridLayout_2.addWidget(self.txtLayover, 7, 1, 1, 1)
        self.FlightInformation_2 = QtWidgets.QGroupBox(FlightDialog)
        self.FlightInformation_2.setGeometry(QtCore.QRect(10, 250, 381, 81))
        self.FlightInformation_2.setObjectName("FlightInformation_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.FlightInformation_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.txtTicket = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.txtTicket.setEnabled(True)
        self.txtTicket.setReadOnly(True)
        self.txtTicket.setObjectName("txtTicket")
        self.gridLayout_3.addWidget(self.txtTicket, 0, 1, 1, 1)
        self.txtDate = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.txtDate.setEnabled(True)
        self.txtDate.setReadOnly(True)
        self.txtDate.setObjectName("txtDate")
        self.gridLayout_3.addWidget(self.txtDate, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(FlightDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(400, 20, 381, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtBillingAddress = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtBillingAddress.setReadOnly(True)
        self.txtBillingAddress.setObjectName("txtBillingAddress")
        self.gridLayout.addWidget(self.txtBillingAddress, 2, 2, 1, 1)
        self.txtCcType = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtCcType.setEnabled(True)
        self.txtCcType.setReadOnly(True)
        self.txtCcType.setObjectName("txtCcType")
        self.gridLayout.addWidget(self.txtCcType, 0, 2, 1, 1)
        self.txtBillingName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtBillingName.setReadOnly(True)
        self.txtBillingName.setObjectName("txtBillingName")
        self.gridLayout.addWidget(self.txtBillingName, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.txtPhone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPhone.setReadOnly(True)
        self.txtPhone.setObjectName("txtPhone")
        self.gridLayout.addWidget(self.txtPhone, 3, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(FlightDialog)
        self.groupBox.setGeometry(QtCore.QRect(399, 140, 381, 80))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.txtFrom = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.txtFrom.setReadOnly(True)
        self.txtFrom.setObjectName("txtFrom")
        self.gridLayout_4.addWidget(self.txtFrom, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        self.txtTo = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.txtTo.setReadOnly(True)
        self.txtTo.setObjectName("txtTo")
        self.gridLayout_4.addWidget(self.txtTo, 1, 2, 1, 1)

        self.retranslateUi(FlightDialog)
        QtCore.QMetaObject.connectSlotsByName(FlightDialog)

    def retranslateUi(self, FlightDialog):
        _translate = QtCore.QCoreApplication.translate
        FlightDialog.setWindowTitle(_translate("FlightDialog", "DSC :: Flight Summary"))
        self.FlightInformation.setTitle(_translate("FlightDialog", "Flight Information"))
        self.label_13.setText(_translate("FlightDialog", "Return Landing:"))
        self.label_10.setText(_translate("FlightDialog", "Depart Takeoff:"))
        self.label_11.setText(_translate("FlightDialog", "Depart Landing:"))
        self.label_12.setText(_translate("FlightDialog", "Return Takeoff:"))
        self.label_7.setText(_translate("FlightDialog", "Airline Name:"))
        self.label_9.setText(_translate("FlightDialog", "Airplane Class:"))
        self.label_8.setText(_translate("FlightDialog", "Trip Price:"))
        self.label_2.setText(_translate("FlightDialog", "Layover:"))
        self.FlightInformation_2.setTitle(_translate("FlightDialog", "Ticket Information"))
        self.label_15.setText(_translate("FlightDialog", "Ticket No."))
        self.label_16.setText(_translate("FlightDialog", "Date Purchased:"))
        self.label_4.setText(_translate("FlightDialog", "Billing Name:"))
        self.label_5.setText(_translate("FlightDialog", "Billing Address:"))
        self.label.setText(_translate("FlightDialog", "Credit Card Type:"))
        self.label_6.setText(_translate("FlightDialog", "Phone Number:"))
        self.groupBox.setTitle(_translate("FlightDialog", "Destination"))
        self.label_3.setText(_translate("FlightDialog", "From:"))
        self.label_14.setText(_translate("FlightDialog", "To:"))

