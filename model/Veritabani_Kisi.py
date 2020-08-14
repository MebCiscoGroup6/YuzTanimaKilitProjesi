from model.Veritabani import Veritabani
from collections import namedtuple
import sqlite3
from enum import Enum

class RaporTuru(Enum):
    TekTarih = 1
    TarihAraligi = 2
    KisiyeGore = 3

class VeriTabaniKisi(Veritabani):
    def __init__(self):
        self.KisiListesi = []
        self.kTuple = namedtuple('Kisi', ['kisiId', 'adSoyad', 'okulNo', 'sinif', 'resim'])
        pass

    def Bagla(self):
        try:
            self.conn = sqlite3.connect('db/db_python_kisiler.db')

        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
        finally:
            pass

    def Kes(self):
        self.conn.close()

    def Ekle(self, kisi):
        try:
            cursor = self.conn.cursor()
            sorgu = "Insert into tbKisiler(ad_soyad,okul_no,sinif,resim) Values('{}',{},'{}','{}')". \
                format(kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim)
            cursor.execute(sorgu)
            self.conn.commit()
            cursor.close()
            print("Kayıt başarı ile gerçekleştirildi.")
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Sil(self, id):
        try:
            cursor = self.conn.cursor()
            sorgu = "Delete from tbKisiler Where kisi_id={}".format(id)
            cursor.execute(sorgu)
            self.conn.commit()
            print("Kayıt başarı ile silindi.")
        except self.conn.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Guncelle(self, kisi):
        try:
            cursor = self.conn.cursor()
            sorgu = "Update tbKisiler Set ad_soyad='{}', okul_no={}, sinif='{}', resim='{}' Where kisi_id={}". \
                format(kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim, kisi.kisiId)
            cursor.execute(sorgu)
            self.conn.commit()
            print("Kayıt başarı ile güncelleştirildi.")
        except self.conn.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Getir(self, id):
        try:
            cursor = self.conn.cursor()
            sorgu = "Select * from tbKisiler Where kisi_id={}".format(id)
            cursor.execute(sorgu)
            k = cursor.fetchone()
            kisi = self.kTuple(k[0], k[1], k[2], k[3], k[4])
            cursor.close()
            return kisi
            print("Kayıt başarı ile getirildi.")
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None
    def GetirOkulNo(self, okulNo):
        try:
            cursor = self.conn.cursor()
            sorgu = "Select * from tbKisiler Where okul_no={}".format(okulNo)
            cursor.execute(sorgu)
            k = cursor.fetchone()
            kisi = self.kTuple(k[0], k[1], k[2], k[3], k[4])
            cursor.close()
            return kisi
            print("Kayıt başarı ile getirildi.")
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None
    def TumunuGetir(self):
        try:
            cursor = self.conn.cursor()
            sorgu = "SELECT * FROM tbkisiler ORDER By ad_soyad ASC"
            cursor.execute(sorgu)
            kisiListesi = cursor.fetchall()
            kisiListesi = [self.kTuple(k[0], k[1], k[2], k[3], k[4]) for k in kisiListesi]
            cursor.close()
            print("Kayıtlar başarı ile getirildi.")
            return kisiListesi
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None

    def RaporEkle(self,kisi_id, tarih):
        try:
            cursor = self.conn.cursor()
            sorgu = "Insert Into tbraporlar(kisi_id,tarih) Values('{}','{}')".\
                format(kisi_id,tarih)
            cursor.execute(sorgu)
            self.conn.commit()
            print("Kişi kaydedildi.")
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None

    def KisiRaporlari(self, raporTuru,**kwargs):
        try:
            #buradaki dict_items degerlerini yine kwargs degiskeni olarak yolladim
            cursor = self.conn.cursor()
            sorgu = self.KisiRaporlariSorgu(raporTuru=raporTuru, kwargs=kwargs)
            cursor.execute(sorgu)
            raporListesi = cursor.fetchall()
            #bu alana rapor sonucları gelecek


            pass
        except self.conn.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None

    def KisiRaporlariSorgu(self, raporTuru, kwargs):
        sorgu = ""
        if raporTuru == RaporTuru.TekTarih:
            _,tarih= list(kwargs.items())[0]
            sorgu = "SELECT * from tbraporlar Where substr(tarih,1,10) = '{}'".\
                format(tarih)
        elif raporTuru == RaporTuru.TarihAraligi:
            _,tarih1= list(kwargs.items())[0]
            _,tarih2 = list(kwargs.items())[0]
            sorgu = "SELECT * from tbraporlar Where substr(tarih,1,10) BETWEEN '{}' AND '{}'".\
                format(tarih1, tarih2)
        elif raporTuru == RaporTuru.KisiyeGore:
            _,kisi_id= list(kwargs.items())[0]
            sorgu = "SELECT * from tbraporlar Where kisi_id={}".format(kisi_id)
        return sorgu