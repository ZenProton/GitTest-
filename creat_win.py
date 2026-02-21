import sys
import os
from PyQt6.QtWidgets import*
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)
win = QMainWindow()

    # value windows
win.setWindowTitle("mon projet")
win.setGeometry(100,100,500,500)

link = os.path.join(os.path.dirname(__file__),"files/img/logo.ico")
win.setWindowIcon(QIcon(link)) # add icone

win.setStyleSheet("background: red")

label = QLabel("Yolo",win)
label.setStyleSheet("color:blue;background:green;font-size:20px")
label.setGeometry(25,25,100,100)

win.show()

sys.exit(app.exec())