from PyQt5.QtWidgets import *
from arayuzler.ui_people import Ui_MainWindow
from people_table import PeopleTable
from people_add import PeopleAdd
from door_check import DoorCheck
# from PyQt5.QtCore import pyqtSignal

class People(QMainWindow):
    # signalKisiler = pyqtSignal(str)
    def __init__(self):
        super(People, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.people_table_page = PeopleTable()
        self.ui.btnKisiler.clicked.connect(self.clickKisilerAc)

        self.ui.btnKisiEkle.clicked.connect(self.clickKisiEkleAc)
        self.people_add_page = PeopleAdd()

        self.ui.btnOgrenciKontrol.clicked.connect(self.clickKapiKontrol)
        self.door_check_page = DoorCheck()


    def clickKisilerAc(self):

        self.people_table_page.show()

    def clickKisiEkleAc(self):
        self.people_add_page.show()

    def clickKapiKontrol(self):
        self.door_check_page.show()
