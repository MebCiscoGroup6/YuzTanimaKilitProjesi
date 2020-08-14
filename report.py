from PyQt5.QtWidgets import *
from arayuzler.ui_report import Ui_Report
from model.Veritabani_Kisi import VeriTabaniKisi

class Report(QWidget):
    def __init__(self):
        super(Report, self).__init__()
        self.ui = Ui_Report()
        self.ui.setupUi(self)
        self.vtk = VeriTabaniKisi()