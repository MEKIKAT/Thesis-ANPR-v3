from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPhoto = QtWidgets.QLabel(self.centralwidget)
        self.labelPhoto.setGeometry(QtCore.QRect(10, 0, 771, 451))
        self.labelPhoto.setText("")
        self.labelPhoto.setPixmap(QtGui.QPixmap("C:/Users/mekik/Pictures/Screenshots/Screenshot (5).png"))
        self.labelPhoto.setScaledContents(True)
        self.labelPhoto.setObjectName("labelPhoto")
        self.pushButton_Preview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Preview.setGeometry(QtCore.QRect(10, 460, 381, 41))
        self.pushButton_Preview.setObjectName("pushButton_Preview")
        self.pushButton__Next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__Next.setGeometry(QtCore.QRect(410, 460, 371, 41))
        self.pushButton__Next.setObjectName("pushButton__Next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton__Next.clicked.connect(self.show_image1)
        self.pushButton_Preview.clicked.connect(self.show_image2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Preview.setText(_translate("MainWindow", "PreView"))
        self.pushButton__Next.setText(_translate("MainWindow", "Next"))

    def show_image1(self):
        self.labelPhoto.setPixmap(QtGui.QPixmap("C:/Users/mekik/Pictures/Screenshots/Screenshot (5).png"))
        
    def show_image2(self):
        self.labelPhoto.setPixmap(QtGui.QPixmap("C:/Users/mekik/Pictures/Screenshots/DSC_1210.JPG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
