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
class Ui_AirportDialog(object):
    def setupUi(self, AirportDialog):
        AirportDialog.setObjectName("AirportDialog")
        AirportDialog.resize(390, 243)
        self.gridLayoutWidget = QtWidgets.QWidget(AirportDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtAirport = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtAirport.setObjectName("txtAirport")
        self.gridLayout.addWidget(self.txtAirport, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 1, 2, 1, 1)
        self.btnSelectAirport = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSelectAirport.setObjectName("btnSelectAirport")
        self.gridLayout.addWidget(self.btnSelectAirport, 3, 2, 1, 1)
        self.airportList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.airportList.setObjectName("airportList")
        self.gridLayout.addWidget(self.airportList, 2, 0, 1, 3)

        self.retranslateUi(AirportDialog)
        QtCore.QMetaObject.connectSlotsByName(AirportDialog)

    def retranslateUi(self, AirportDialog):
        _translate = QtCore.QCoreApplication.translate
        AirportDialog.setWindowTitle(_translate("AirportDialog", "DSC :: Airport Search"))
        self.label.setText(_translate("AirportDialog", "Airport Name:"))
        self.btnSearch.setText(_translate("AirportDialog", "Search"))
        self.btnSelectAirport.setText(_translate("AirportDialog", "Select Airport"))

