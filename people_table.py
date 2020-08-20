from PyQt5.QtWidgets import *
from arayuzler.ui_people_table import Ui_PeopleTable
from model.Veritabani_Kisi import VeriTabaniKisi

class PeopleTable(QWidget):
    def __init__(self):
        super(PeopleTable, self).__init__()
        self.ui = Ui_PeopleTable()
        self.ui.setupUi(self)
        self.vtk = VeriTabaniKisi()
        self.verileriGetir()

        self.ui.tbwKisiler.clicked.connect(self.selectedTwbKisiler)

    def verileriGetir(self):
        self.kisiListesi = self.vtk.TumunuGetir()
        self.tabloOlustur()
        print(self.kisiListesi)

    def tabloOlustur(self):

        satirSayisi = len(self.kisiListesi)
        sutunSayisi = 3 #gosterilecek sutun sayisi
        self.ui.tbwKisiler.setRowCount(satirSayisi)
        self.ui.tbwKisiler.setColumnCount(sutunSayisi)
        #sutunlar
        self.ui.tbwKisiler.setHorizontalHeaderItem(0,QTableWidgetItem("Okul No"))
        self.ui.tbwKisiler.setHorizontalHeaderItem(1,QTableWidgetItem("Ad Soyad"))
        self.ui.tbwKisiler.setHorizontalHeaderItem(2,QTableWidgetItem("Sınıf"))
        #satirlar
        for satir, kisi in enumerate(self.kisiListesi):
            self.ui.tbwKisiler.setItem(satir,0, QTableWidgetItem(str(kisi.okulNo)))
            self.ui.tbwKisiler.setItem(satir,1, QTableWidgetItem(kisi.adSoyad))
            self.ui.tbwKisiler.setItem(satir,2, QTableWidgetItem(kisi.sinif))

    def selectedTwbKisiler(self):
        # tüm seçilenleri gostermek için
        # for item in self.ui.tbwKisiler.selectedItems():
        #     print("Değer: {}, satir:{}, sütun:{}".format(item.text(), item.row(), item.column()))
        secilenIndex = self.ui.tbwKisiler.selectedItems()[0].row()
        kisi = self.kisiListesi[secilenIndex]
        print(kisi.adSoyad)
