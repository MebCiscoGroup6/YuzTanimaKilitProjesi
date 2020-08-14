from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
#
class MplWidget(QWidget):
    def __init__(self, parent = None, **kwargs):
        QWidget.__init__(self, parent)
        pass
