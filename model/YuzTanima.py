import face_recognition
import os
import numpy as np
import glob
from threading import Thread

class YuzTanima:
    def __init__(self):
        self.yuzler=[]
        self.adlar=[]


    def SozlukEkle(self, dosyaAd):
        Resimler = "resimler/kisiler"
        dosyaAd = Resimler + '/' + dosyaAd
        sozluk = {}
        image_rgb = face_recognition.load_image_file(dosyaAd)
        kimlik = os.path.splitext(os.path.basename(dosyaAd))
        konumlar = face_recognition.face_locations(image_rgb)
        kodlamalar = face_recognition.face_encodings(image_rgb, konumlar)
        sozluk[kimlik] = kodlamalar[0]

        print(kodlamalar[0])
        key = list(sozluk.keys())[0]
        value = list(sozluk.values())[0]
        print(key,value,"degerler")

        self.SozlukGetir()
        self.yuzler.append(value)
        self.adlar.append(key)
        self.SozlukYaz()

    def SozlukGetir(self):
        data = np.loadtxt("takas/yuzler.csv", delimiter=',')
        self.yuzler = [np.array(x) for x in data]

        data = np.loadtxt("takas/adlar.csv", delimiter=',', dtype=object)
        self.adlar = [tuple(x) for x in data]

    def SozlukYaz(self):
        data = np.asarray(self.yuzler)
        np.savetxt("takas/yuzler.csv", data, delimiter=',')

        data = np.asarray(self.adlar, dtype=object)
        np.savetxt("takas/adlar.csv", data, delimiter=',', fmt='%s')

    def __OnYukle(self,parent):
        sozluk = {}
        Resimler = "resimler/kisiler"
        tumResimler = glob.glob((os.path.join(Resimler, '*.jpg')))
        tumResimSayisi = len(tumResimler)
        r = 0
        for dosyaad in tumResimler:
            image_rgb = face_recognition.load_image_file(dosyaad)
            kimlik = os.path.splitext(os.path.basename(dosyaad))
            r += 1
            parent.statusBar().showMessage("Yüklenen resim {}/{} - Resim:{}".format(r, tumResimSayisi, dosyaad))
            # burada tanimlamalarin sisteme yuklenmesi icin thread yapmaliyiz.

            konumlar = face_recognition.face_locations(image_rgb)
            kodlamalar = face_recognition.face_encodings(image_rgb, konumlar)
            sozluk[kimlik] = kodlamalar[0]

        self.yuzler = list(sozluk.values())
        self.adlar = list(sozluk.keys())

        self.SozlukYaz()
        parent.ui.btnOnYukleme.setEnabled(True)

    def SozlukCsvTumunuYenile(self, parent):
        thread1 = Thread(target=self.__OnYukle, args=(parent,))
        thread1.start()


