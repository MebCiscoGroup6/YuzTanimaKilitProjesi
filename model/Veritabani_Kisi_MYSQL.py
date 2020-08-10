from model.Kisi import Kisi
from model.Veritabani import Veritabani
import mysql.connector
from mysql.connector import Error
from collections import namedtuple

class VeriTabaniKisi(Veritabani):
    def __init__(self):
        self.KisiListesi = []
        self.connection = mysql.connector.connect()
        self.kTuple = namedtuple('Kisi', ['kisiId', 'adSoyad', 'okulNo', 'sinif', 'resim'])
        pass

    def Bagla(self):
        try:
            if (self.connection.is_connected() == False):
                self.connection = mysql.connector.connect(host='localhost',
                                                          database='db_python_kisiler',
                                                          user='root',
                                                          password='MegeBursa16+')
            else:
                print("Zaten bağlı")

        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))
        finally:
            pass

    def Kes(self):
        if (self.connection.is_connected()):
            self.connection.close()
            # print("Bağlantı kapatıldı.")

    def Ekle(self, kisi):
        try:
            cursor = self.connection.cursor()
            parameters = [kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim]
            cursor.callproc('spKisiEkle', parameters)
            self.connection.commit()
            cursor.close()
            print("Kayıt başarı ile gerçekleştirildi.")
        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Sil(self, id):
        try:
            cursor = self.connection.cursor()
            parameters = [id]
            cursor.callproc('spKisiSil', parameters)
            self.connection.commit()
            cursor.close()
            print("Kayıt başarı ile silindi.")
        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Guncelle(self, kisi):
        try:
            cursor = self.connection.cursor()
            parameters = [kisi.kisiId, kisi.adSoyad, kisi.okulNo, kisi.sinif, kisi.resim]
            cursor.callproc('spKisiGuncelle', parameters)
            self.connection.commit()
            cursor.close()
            print("Kayıt başarı ile güncelleştirildi.")
        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))

    def Getir(self, id):
        try:
            cursor = self.connection.cursor()
            parameters = [id]
            cursor.callproc('spKisiGetir', parameters)
            k = [r.fetchall() for r in cursor.stored_results()][0][0]
            cursor.close()

            kisi = self.kTuple(k[0],k[1],k[2],k[3],k[4])
            return kisi
            print("Kayıt başarı ile getirildi.")
        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None

    def TumunuGetir(self):
        try:
            cursor = self.connection.cursor()
            parameters = []
            cursor.callproc('spTumKisiler', parameters)
            kisiListesi =[r.fetchall() for r in cursor.stored_results()][0]
            kisiListesi = [self.kTuple(k[0],k[1],k[2],k[3],k[4]) for k in kisiListesi]
            cursor.close()
            print("Kayıtlar başarı ile getirildi.")
            return kisiListesi
        except mysql.connector.Error as error:
            print("Bağlantı sorunu:{}".format(error))
            return None
