from PyQt5.QtWidgets import QApplication
from people import People

if __name__ == '__main__':
    app = QApplication([])
    window = People()
    window.show()
    app.exec_()

