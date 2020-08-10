from abc import ABCMeta, abstractmethod


class Veritabani(metaclass=ABCMeta):

    @abstractmethod
    def Bagla(self):
        pass

    @abstractmethod
    def Kes(self):
        pass

    @abstractmethod
    def Ekle(self, obj):
        pass

    @abstractmethod
    def Sil(self, id):
        pass

    @abstractmethod
    def Guncelle(self, obj):
        pass

    @abstractmethod
    def Getir(self, id):
        pass

    @abstractmethod
    def TumunuGetir(self):
        pass
