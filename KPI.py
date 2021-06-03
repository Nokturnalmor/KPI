import Cust_Functions as F
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWinExtras import QtWin
import os
import time
import subprocess
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.app_icons()
        self.actions()

    def actions(self):
        self.action_Smena_Parol = self.ui.action_2
        self.action_Smena_Parol.triggered.connect(self.Smena_Parol)


    def init_UI(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.lineEdit_3_nParol.setVisible(False)
        self.ui.lineEdit_3_nParol_2.setVisible(False)

    def app_icons(self):
        self.ui.pushButton_login.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogYesButton)))
        self.ui.pushButton_logout.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogNoButton)))

    def Smena_Parol(self):
        self.ui.lineEdit_3_nParol.setVisible(True)
        self.ui.lineEdit_3_nParol_2.setVisible(True)
        self.ui.pushButton_logout.setText("Сменить и выйти")
        self.regim_new_parol = True


app = QtWidgets.QApplication([])

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))

S = F.scfg('Stile').split(",")
app.setStyle(S[1])

application = mywindow()
application.show()

sys.exit(app.exec())
