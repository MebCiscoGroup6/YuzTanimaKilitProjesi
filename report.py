from PyQt5.QtWidgets import *
from arayuzler.ui_report import Ui_Report
from model.Veritabani_Kisi import VeriTabaniKisi,RaporTuru


class Report(QWidget):
    def __init__(self):
        super(Report, self).__init__()
        self.ui = Ui_Report()
        self.ui.setupUi(self)
        self.vtk = VeriTabaniKisi()
        self.vtk.Bagla()
        self.kisileriGetir()
        self.sorguTurleriniGetir()
        self.ui.btnSorgula.clicked.connect(self.clickSorgulamaBaslat)

    def kisileriGetir(self):
        self.kisiListesi = self.vtk.TumunuGetir()
        self.ui.cmbKisiAdi.clear()
        self.ui.cmbKisiAdi.addItem("Seçiniz", "")
        for kisi in self.kisiListesi:
            self.ui.cmbKisiAdi.addItem(kisi.adSoyad, kisi.kisiId)

    def sorguTurleriniGetir(self):
        self.ui.cmbSorguTuru.clear()
        self.ui.cmbSorguTuru.addItem("Seçiniz","")
        self.ui.cmbSorguTuru.addItem("Tek Tarih Sorgula",RaporTuru.TekTarih)
        self.ui.cmbSorguTuru.addItem("Tarih Aralığı Sorgula",RaporTuru.TarihAraligi)
        self.ui.cmbSorguTuru.addItem("Kişiye Göre Sorgula",RaporTuru.KisiyeGore)

    def clickSorgulamaBaslat(self):
        sorgulamaTuru = self.ui.cmbSorguTuru.currentData()
        if sorgulamaTuru == RaporTuru.TekTarih:
            print("Tek tarih")
        elif sorgulamaTuru == RaporTuru.TarihAraligi:
            print("Tarih Aralığı")
        elif sorgulamaTuru == RaporTuru.KisiyeGore:
            kisiId = self.ui.cmbKisiAdi.currentData()
            print("Kişiye göre", kisiId)

