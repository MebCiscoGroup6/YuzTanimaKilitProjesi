# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'people.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.btnKisiler = QtWidgets.QPushButton(self.centralwidget)
        self.btnKisiler.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnKisiler.setFont(font)
        self.btnKisiler.setObjectName("btnKisiler")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btnKisiler)
        self.btnKisiEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKisiEkle.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnKisiEkle.setFont(font)
        self.btnKisiEkle.setObjectName("btnKisiEkle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.btnKisiEkle)
        self.btnRaporlar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRaporlar.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnRaporlar.setFont(font)
        self.btnRaporlar.setObjectName("btnRaporlar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.btnRaporlar)
        self.btnOgrenciKontrol = QtWidgets.QPushButton(self.centralwidget)
        self.btnOgrenciKontrol.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnOgrenciKontrol.setFont(font)
        self.btnOgrenciKontrol.setObjectName("btnOgrenciKontrol")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btnOgrenciKontrol)
        self.btnOnYukleme = QtWidgets.QPushButton(self.centralwidget)
        self.btnOnYukleme.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnOnYukleme.setFont(font)
        self.btnOnYukleme.setObjectName("btnOnYukleme")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btnOnYukleme)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kişiler Yönetimi"))
        self.btnKisiler.setText(_translate("MainWindow", "Kişiler"))
        self.btnKisiEkle.setText(_translate("MainWindow", "Kişi Ekle"))
        self.btnRaporlar.setText(_translate("MainWindow", "Raporlar"))
        self.btnOgrenciKontrol.setText(_translate("MainWindow", "Kapı Kontrol"))
        self.btnOnYukleme.setText(_translate("MainWindow", "Resimleri Önyükleme Güncelle"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
