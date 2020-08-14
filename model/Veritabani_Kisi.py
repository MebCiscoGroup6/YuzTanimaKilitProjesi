from model.Veritabani import Veritabani
from collections import namedtuple
import sqlite3
from enum import Enum
import functools

class RaporTuru(Enum):
    TekTarih = 1
    TarihAraligi = 2
    KisiyeGore = 3

class VeriTabaniKisi(Veritabani):
    def __init__(self):
        self.KisiListesi = []
        self.kTuple = namedtuple('Kisi', ['kisiId', 'adSoyad', 'okulNo', 'sinif', 'resim'])
        pass

    def HataYakala(fonk):
        @functools.wraps(fonk)
        def wrapper(self, *args, **kwargs):
            sonuc = None
            try:
                sonuc = fonk(self, *args, **kwargs)
            except self.conn.Error as error:
                print("Bağlantı sorunu:{}".format(error))
            return sonuc
        return wrapper

    @HataYakala
    def Bagla(self):
        self.conn = sqlite3.connect('db/db_python_kisiler.db')

    def Kes(self):
        self.conn.close()

    @HataYakala
    def Ekle(self, kisi):
        cursor = self.conn.cursor()
        sorgu = "Insert into tbKisiler(ad_soyad,okul_no,sinif,resim) Values('{}',{},'{}','{}')". \
            format(kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim)
        cursor.execute(sorgu)
        self.conn.commit()
        cursor.close()
        print("Kayıt başarı ile gerçekleştirildi.")

    @HataYakala
    def Sil(self, id):
        cursor = self.conn.cursor()
        sorgu = "Delete from tbKisiler Where kisi_id={}".format(id)
        cursor.execute(sorgu)
        self.conn.commit()
        print("Kayıt başarı ile silindi.")

    @HataYakala
    def Guncelle(self, kisi):
        cursor = self.conn.cursor()
        sorgu = "Update tbKisiler Set ad_soyad='{}', okul_no={}, sinif='{}', resim='{}' Where kisi_id={}". \
            format(kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim, kisi.kisiId)
        cursor.execute(sorgu)
        self.conn.commit()
        print("Kayıt başarı ile güncelleştirildi.")

    @HataYakala
    def Getir(self, id):
        cursor = self.conn.cursor()
        sorgu = "Select * from tbKisiler Where kisi_id={}".format(id)
        cursor.execute(sorgu)
        k = cursor.fetchone()
        kisi = self.kTuple(k[0], k[1], k[2], k[3], k[4])
        cursor.close()
        return kisi
        print("Kayıt başarı ile getirildi.")

    @HataYakala
    def GetirOkulNo(self, okulNo):
        cursor = self.conn.cursor()
        sorgu = "Select * from tbKisiler Where okul_no={}".format(okulNo)
        cursor.execute(sorgu)
        k = cursor.fetchone()
        kisi = self.kTuple(k[0], k[1], k[2], k[3], k[4])
        cursor.close()
        return kisi
        print("Kayıt başarı ile getirildi.")

    @HataYakala
    def TumunuGetir(self):
        cursor = self.conn.cursor()
        sorgu = "SELECT * FROM tbkisiler ORDER By ad_soyad ASC"
        cursor.execute(sorgu)
        kisiListesi = cursor.fetchall()
        kisiListesi = [self.kTuple(k[0], k[1], k[2], k[3], k[4]) for k in kisiListesi]
        cursor.close()
        print("Kayıtlar başarı ile getirildi.")
        return kisiListesi

    @HataYakala
    def RaporEkle(self,kisi_id, tarih):
        cursor = self.conn.cursor()
        sorgu = "Insert Into tbraporlar(kisi_id,tarih) Values('{}','{}')". \
            format(kisi_id, tarih)
        cursor.execute(sorgu)
        self.conn.commit()
        print("Kişi kaydedildi.")

    @HataYakala
    def KisiRaporlari(self, raporTuru,**kwargs):
        # buradaki dict_items degerlerini yine kwargs degiskeni olarak yolladim
        cursor = self.conn.cursor()
        sorgu = self.KisiRaporlariSorgu(raporTuru=raporTuru, kwargs=kwargs)
        cursor.execute(sorgu)
        raporListesi = cursor.fetchall()
        # bu alana rapor sonucları gelecek
        return raporListesi

    def KisiRaporlariSorgu(self, raporTuru, kwargs):
        sorgu = "SELECT rp.*,ks.ad_soyad from tbraporlar rp Inner JOIN tbkisiler ks On rp.kisi_id=ks.kisi_id"
        if raporTuru == RaporTuru.TekTarih:
            _,tarih= list(kwargs.items())[0]
            sorgu = sorgu + " Where substr(rp.tarih,1,10) = '{}'".\
                format(tarih)
        elif raporTuru == RaporTuru.TarihAraligi:
            _,tarih1= list(kwargs.items())[0]
            _,tarih2 = list(kwargs.items())[1]
            sorgu = sorgu + " Where substr(rp.tarih,1,10) BETWEEN '{}' AND '{}'".\
                format(tarih1, tarih2)
        elif raporTuru == RaporTuru.KisiyeGore:
            _,kisi_id= list(kwargs.items())[0]
            sorgu = sorgu + " Where rp.kisi_id={}".format(kisi_id)
        else:
            sorgu = ""
        return sorgu