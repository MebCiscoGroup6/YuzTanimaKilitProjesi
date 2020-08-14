# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Report(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(952, 524)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(490, 20, 441, 151))
        self.tableView.setObjectName("tableView")
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setGeometry(QtCore.QRect(20, 190, 911, 321))
        self.MplWidget.setObjectName("MplWidget")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(18, 20, 451, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cmbKisiAdi = QtWidgets.QComboBox(self.widget)
        self.cmbKisiAdi.setObjectName("cmbKisiAdi")
        self.gridLayout.addWidget(self.cmbKisiAdi, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.leTarih1 = QtWidgets.QLineEdit(self.widget)
        self.leTarih1.setObjectName("leTarih1")
        self.gridLayout.addWidget(self.leTarih1, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.leTarih2 = QtWidgets.QLineEdit(self.widget)
        self.leTarih2.setObjectName("leTarih2")
        self.gridLayout.addWidget(self.leTarih2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.cmbSorguTuru = QtWidgets.QComboBox(self.widget)
        self.cmbSorguTuru.setObjectName("cmbSorguTuru")
        self.gridLayout.addWidget(self.cmbSorguTuru, 3, 1, 1, 1)
        self.btnSorgula = QtWidgets.QPushButton(self.widget)
        self.btnSorgula.setObjectName("btnSorgula")
        self.gridLayout.addWidget(self.btnSorgula, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kişi Raporları"))
        self.label.setText(_translate("Form", "Kişi Adı:"))
        self.label_2.setText(_translate("Form", "Başlangıç Tarihi:"))
        self.label_3.setText(_translate("Form", "Bitiş Tarihi:"))
        self.label_4.setText(_translate("Form", "Sorgu Türü:"))
        self.btnSorgula.setText(_translate("Form", "Sorgula"))
from arayuzler.mplwidget import MplWidget


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Report()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
