from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class root(QMainWindow):
    def __init__(self):
        super(root, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Aguy")

        self.initUi()   
    
    def initUi(self):
        self.Label1 = QtWidgets.QLabel(self)
        self.Label1.setText("Label 1")
        self.Label1.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Button 1")
        self.b1.clicked.connect(self.Clicked)

    def Clicked(self):
        self.Label1.setText("Clicked aaaaaaaaaaaaaa")
        self.update()
    
    def update(self):
        self.Label1.adjustSize()


  

def clicked1():
    print ("Clicked 1")     

def window():
    app = QApplication(sys.argv)
    win = root()
    win.show()
    sys.exit(app.exec_())


window()