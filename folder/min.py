from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 

import sys 

class MinWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MinWindow,self).__init__(*args, **kwargs) 
        self.setWindowTitle("Ttitle ")
        FirstLabel = QLabel("HELLO LABEL 1")
        FirstLabel.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(FirstLabel)

        SecondLabel = QLabel("HELLO LABEL 2 ")
        SecondLabel.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(SecondLabel)    


app = QApplication(sys.argv) 

window = MinWindow()
window.show()   


app.exec_()