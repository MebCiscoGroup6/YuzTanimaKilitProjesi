from PyQt5.QtWidgets import QApplication
from people import People

app = QApplication([])
window = People()
window.show()
app.exec_()