

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_PopUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PopUp.setGeometry(QtCore.QRect(180, 270, 301, 131))
        self.pushButton_PopUp.setObjectName("pushButton_PopUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_PopUp.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_PopUp.setText(_translate("MainWindow", "POP UP WINDOW"))
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error Messages")
        msg.setText("Error Reading File")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore )
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Informative Messages ")

        msg.setDetailedText("See Details Below")

        msg.buttonClicked.connect(self.Button_for_popup)
      
        x = msg.exec_()
     
    def Button_for_popup(self,i):
        print(i.text())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
