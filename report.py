from PyQt5.QtWidgets import *
from arayuzler.ui_report import Ui_Report
from model.Veritabani_Kisi import VeriTabaniKisi, RaporTuru
import numpy as np
import pandas as pd

class Report(QWidget):
    def __init__(self):
        super(Report, self).__init__()
        self.ui = Ui_Report()
        self.ui.setupUi(self)
        self.vtk = VeriTabaniKisi()
        self.kisileriGetir()
        self.sorguTurleriniGetir()
        self.ui.btnSorgula.clicked.connect(self.clickSorgulamaBaslat)
        self.raporListesi = []

    def kisileriGetir(self):
        self.kisiListesi = self.vtk.TumunuGetir()
        self.ui.cmbKisiAdi.clear()
        self.ui.cmbKisiAdi.addItem("Seçiniz", "")
        for kisi in self.kisiListesi:
            self.ui.cmbKisiAdi.addItem(kisi.adSoyad, kisi.kisiId)

    def sorguTurleriniGetir(self):
        self.ui.cmbSorguTuru.clear()
        self.ui.cmbSorguTuru.addItem("Seçiniz", "")
        self.ui.cmbSorguTuru.addItem("Tek Tarih Sorgula", RaporTuru.TekTarih)
        self.ui.cmbSorguTuru.addItem("Tarih Aralığı Sorgula", RaporTuru.TarihAraligi)
        self.ui.cmbSorguTuru.addItem("Kişiye Göre Sorgula", RaporTuru.KisiyeGore)

    def clickSorgulamaBaslat(self):
        sorgulamaTuru = self.ui.cmbSorguTuru.currentData()
        if sorgulamaTuru == RaporTuru.TekTarih:
            tarih = self.tarihDuzenle(self.ui.leTarih1.text())
            self.raporListesi = self.vtk.KisiRaporlari(raporTuru=RaporTuru.TekTarih, tarih=tarih)
        elif sorgulamaTuru == RaporTuru.TarihAraligi:
            tarih1 = self.tarihDuzenle(self.ui.leTarih1.text())
            tarih2 = self.tarihDuzenle(self.ui.leTarih2.text())
            self.raporListesi = self.vtk.KisiRaporlari(raporTuru=RaporTuru.TarihAraligi, tarih1=tarih1, tarih2=tarih2)
        elif sorgulamaTuru == RaporTuru.KisiyeGore:
            kisiId = self.ui.cmbKisiAdi.currentData()
            self.raporListesi = self.vtk.KisiRaporlari(raporTuru=RaporTuru.KisiyeGore, kisi_id=kisiId)

        self.tabloOlustur()
        self.grafikOlustur()

    def tabloOlustur(self):

        satirSayisi = len(self.raporListesi)
        sutunSayisi = 3  # gosterilecek sutun sayisi
        self.ui.tbwRaporlar.setRowCount(satirSayisi)
        self.ui.tbwRaporlar.setColumnCount(sutunSayisi)
        # #sutunlar
        self.ui.tbwRaporlar.setHorizontalHeaderItem(0, QTableWidgetItem("Rapor Id"))
        self.ui.tbwRaporlar.setHorizontalHeaderItem(1, QTableWidgetItem("Ad Soyad"))
        self.ui.tbwRaporlar.setHorizontalHeaderItem(2, QTableWidgetItem("Tarih"))
        # #satirlar
        for satir, rapor in enumerate(self.raporListesi):
            self.ui.tbwRaporlar.setItem(satir, 0, QTableWidgetItem(str(rapor.raporId)))
            self.ui.tbwRaporlar.setItem(satir, 1, QTableWidgetItem(rapor.adSoyad))
            self.ui.tbwRaporlar.setItem(satir, 2, QTableWidgetItem(rapor.tarih))

    def tarihDuzenle(self, tarih):
        tarih = str(tarih).replace(".", "-").replace("/", "-")
        tmp = tarih.split("-")
        tarih = tmp[2] + "-" + tmp[1] + "-" + tmp[0]
        return tarih

    def grafikOlustur(self):
        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.draw()

        #Burada giriş yapan kişilerin giriş sayılarına göra bir raporlama yapılacak.
        veriKumesi = pd.DataFrame(self.raporListesi)
        # print(veriKumesi)
        veriler = ['adSoyad', 'tarih']
        tablo = veriKumesi[veriler].groupby(['adSoyad']).size().reset_index(name="sayi")
        x = tablo.adSoyad
        y = tablo.sayi

        self.ui.MplWidget.canvas.ax.plot(x, y)
        self.ui.MplWidget.canvas.draw()