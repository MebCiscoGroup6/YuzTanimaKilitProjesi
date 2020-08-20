from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from arayuzler.ui_door_check import Ui_DoorCheck
import cv2
import face_recognition
import numpy as np
import glob
import os
from model.Veritabani_Kisi import VeriTabaniKisi
from datetime import datetime
from threading import Thread


class DoorCheck(QWidget):
    def __init__(self):
        super(DoorCheck, self).__init__()
        self.ui = Ui_DoorCheck()
        self.ui.setupUi(self)
        self.timer = QTimer()

        self.vtk = VeriTabaniKisi()

        self.klasorBilgileri()  # klasörlerdeki bilgileri alıyoruz.
        # kameraOynat ve kontrolBaslat timerdan once olmali
        self.kameraOynat()
        self.kontrolBaslat = False
        self.timer.timeout.connect(self.goruntuGoster)
        self.Uzaklik = 0.6  # tanima orani
        self.ui.btnTekrarDene.clicked.connect(self.clickKameraAc)

        pass

    def closeEvent(self, event):
        self.kameraDurdur()

    def klasorBilgileri(self):
        sozluk = {}
        Resimler = "resimler/kisiler"
        print(glob.glob((os.path.join(Resimler, '*.jpg'))))
        # fotolar = [x for x in os.listdir(Resimler) if os.path.isdir(x)]
        thread1 = Thread(target=self.threadFaceSozluk, args=(Resimler, sozluk))
        thread1.start()

    def sozlukOku(self):
        data = np.loadtxt("takas/yuzler.csv", delimiter=',')
        self.yuzler = [np.array(x) for x in data]

        data = np.loadtxt("takas/adlar.csv", delimiter=',', dtype=object)
        self.adlar = [tuple(x) for x in data]

    def sozlukYaz(self, Resimler, sozluk):
        tumResimler = glob.glob((os.path.join(Resimler, '*.jpg')))
        tumResimSayisi = len(tumResimler)
        r = 0
        for dosyaad in tumResimler:
            image_rgb = face_recognition.load_image_file(dosyaad)
            kimlik = os.path.splitext(os.path.basename(dosyaad))
            r += 1
            self.ui.btnTekrarDene.setEnabled(False)
            self.setWindowTitle("Yüklenen resim {}/{} - Resim:{}".format(r, tumResimSayisi, dosyaad))
            # burada tanimlamalarin sisteme yuklenmesi icin thread yapmaliyiz.

            konumlar = face_recognition.face_locations(image_rgb)
            kodlamalar = face_recognition.face_encodings(image_rgb, konumlar)
            sozluk[kimlik] = kodlamalar[0]

        self.ui.btnTekrarDene.setEnabled(True)
        self.yuzler = list(sozluk.values())
        self.adlar = list(sozluk.keys())

        data = np.asarray(self.yuzler)
        np.savetxt("takas/yuzler.csv", data, delimiter=',')

        data = np.asarray(self.adlar, dtype=object)
        np.savetxt("takas/adlar.csv", data, delimiter=',', fmt='%s')
        #veritabanından degil dosyadan bakacak.
        self.vtk.DegisiklikYapildi(degisiklikTuru=False)

    def threadFaceSozluk(self, Resimler, sozluk):

        self.sozlukOku()
        # if self.vtk.DegisiklikDurum() == True:
        #     self.sozlukYaz(Resimler, sozluk)
        # else:
        #     self.sozlukOku()

    def goruntuGoster(self):
        ret, kare = self.kamera.read()
        kare = cv2.cvtColor(kare, cv2.COLOR_BGR2RGB)
        height, width, channel = kare.shape
        step = channel * width
        self.sonGoruntu = kare  # resmin ekrandaki son  temiz hali
        kontrolluResim = kare
        if self.kontrolBaslat == True:
            kontrolluResim = self.kontrolluResimGoster(kare)

        qImg = QImage(kontrolluResim.data, width, height, step, QImage.Format_RGB888)
        self.ui.lbKamera.setPixmap(QPixmap.fromImage(qImg))

    def kameraOynat(self):
        if not self.timer.isActive():
            self.kamera = cv2.VideoCapture(0)
            self.ui.btnTekrarDene.setText("Kontrol Et")
            self.timer.start(20)
        else:
            self.kameraDurdur()

    def clickKameraAc(self):
        self.kontrolBaslat = not self.kontrolBaslat
        if self.kontrolBaslat == False:
            self.kameraOynat()
            self.ui.lbDurum.setText("Onay Durumu: Bekleniyor")

    def kameraDurdur(self):
        self.ui.btnTekrarDene.setText("Tekrar Dene")
        self.timer.stop()
        self.kamera.release()

    def kontrolluResimGoster(self, kare):
        # kare = cv2.flip(kare, 1)  # 1 yatay 0 ise dikey
        kucuk_kare = cv2.resize(kare, (0, 0), fx=0.25, fy=0.25)
        rgb_kucuk_kare = kucuk_kare[:, :, ::-1]  # BGR -> RGB dönüsümü
        konumlar = face_recognition.face_locations(rgb_kucuk_kare)
        kodlamalar = face_recognition.face_encodings(rgb_kucuk_kare, konumlar)
        for konum, kodlama in zip(konumlar, kodlamalar):
            mesafeler = face_recognition.face_distance(self.yuzler, kodlama)
            if np.any(mesafeler <= self.Uzaklik):
                en_uygun = np.argmin(mesafeler)
                ad = self.adlar[en_uygun]
                # öğrenci tanındı.
                print("Taninan ogrenci", ad[0])
                okulNo = int(ad[0])
                self.kisiGetir(okulNo=okulNo)
            else:
                # ogrenci tanınmadı
                ad = None
                self.ui.lbDurum.setText("Durum: Kişi Tanınmadı")
            tepe, sag, alt, sol = konum

            # eger goruntuyu kuculttuysek yeniden büyütmek gerekir
            tepe *= 4
            sag *= 4
            alt *= 4
            sol *= 4

            if ad is None:
                ad = "Bilinmiyor"
                renk = (0, 0, 255)
            else:
                renk = (0, 255, 0)

            # cerceve
            cv2.rectangle(kare, (sol, tepe), (sag, alt), renk, 2)

            # yazi arkaplani
            cv2.rectangle(kare, (sol, alt), (sag, alt + 30), renk, cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(kare, ad[0], (sol + 25, alt + 25), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        return kare

    def kisiGetir(self, okulNo):
        self.kameraDurdur()
        kisi = self.vtk.GetirOkulNo(okulNo)
        self.ui.lbDurum.setText(kisi.adSoyad + " Giriş Başarılı")
        tarih = str(datetime.now())
        tarih = tarih[:tarih.find('.')]

        self.vtk.RaporEkle(kisi_id=kisi.kisiId, tarih=tarih)
        # resmi kaydedelim
        tmp = tarih.replace("-", "_").replace(" ", "_").replace(":", "_")
        tmp = tmp + "_kisi_" + str(kisi.kisiId) + ".jpg"
        kayit_yolu = "resimler/raporlar/" + tmp
        cv2.imwrite(kayit_yolu, self.sonGoruntu)

