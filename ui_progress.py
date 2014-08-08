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
class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        ProgressDialog.setObjectName("ProgressDialog")
        ProgressDialog.resize(350, 60)
        self.gridLayoutWidget = QtWidgets.QWidget(ProgressDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 42))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(ProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(ProgressDialog)

    def retranslateUi(self, ProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressDialog.setWindowTitle(_translate("ProgressDialog", "DSC :: Progress Bar"))
        self.label.setText(_translate("ProgressDialog", "Loading data from online..."))

