from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from arayuzler.ui_people_add import Ui_PeopleAdd
from model.Kisi import Kisi
from model.Veritabani_Kisi import VeriTabaniKisi
import cv2


class PeopleAdd(QWidget):
    #people add sınıfı tanımlanmaktadır.
    def __init__(self):
        super(PeopleAdd, self).__init__()
        self.ui = Ui_PeopleAdd()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.kameraGoster)

        self.ui.btnDegistir.clicked.connect(self.clickKameraAc)
        self.imgNoBody = cv2.imread("resimler/nobody.jpg", 0)

        self.ui.btnCek.clicked.connect(self.clickResimKaydet)
        self.ui.btnKaydet.clicked.connect(self.clickKisiKaydet)

        self.vtk = VeriTabaniKisi()

    def clickKisiKaydet(self):
         #Veri tabanına kişinin bilgilerini kaydeden fonsiyon
        self.vtk.Bagla()
        okulNo = self.ui.lbOkulNo.text()
        resimAdi = self.ui.lbOkulNo.text() + ".jpg"
        adSoyad = self.ui.lbAdSoyad.text()
        sinif = self.ui.lbSinif.text()
        kisi = Kisi(kisiId=None, okulNo=int(okulNo), adSoyad=adSoyad, sinif=sinif, resim=resimAdi)
        self.vtk.Ekle(kisi)
        print("Kişi kaydedildi.")
        self.vtk.Kes()
        self.close()
      .

    def clickResimKaydet(self):
        resimAdi = self.ui.lbOkulNo.text() + ".jpg"
        rgb = cv2.cvtColor(self.sonGoruntu, cv2.COLOR_RGB2BGR)
        cv2.imwrite("resimler/kisiler/" + resimAdi, rgb)

    def klavuzluResimGoster(self, kare):
        height, width, channel = kare.shape
        self.imgNoBody = cv2.resize(self.imgNoBody, (width, height))
        _, thresh = cv2.threshold(self.imgNoBody, 100, 255, cv2.THRESH_BINARY_INV)
        konturlar, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cizgili = cv2.drawContours(kare.copy(), konturlar, -1, (0, 255, 0), -1)
        klavuzlu = cv2.addWeighted(kare, .80, cizgili, .20, 0)
        return klavuzlu

    def kameraGoster(self):
        ret, kare = self.kamera.read()
        kare = cv2.cvtColor(kare, cv2.COLOR_BGR2RGB)
        height, width, channel = kare.shape
        step = channel * width

        klavuzlu = self.klavuzluResimGoster(kare)
        self.sonGoruntu = kare  # resmin ekrandaki son  temiz hali
        qImg = QImage(klavuzlu.data, width, height, step, QImage.Format_RGB888)
        self.ui.lbResim.setPixmap(QPixmap.fromImage(qImg))

    def clickKameraAc(self):
        #kamera açma fonksiyonu tanımlanmaktadır.
        if not self.timer.isActive():
            self.kamera = cv2.VideoCapture(0)
            self.ui.btnDegistir.setText("Durdur")
            self.timer.start(20)
        else:
            self.ui.btnDegistir.setText("Değiştir")
            self.timer.stop()
            self.kamera.release()
