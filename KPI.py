import Cust_Functions as F
import autorization as aut
import shabloni as shabl
import kpi_sotr as kps
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWinExtras import QtWin
import os

from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.app_icons()
        self.actions()
        self.uiconnect()
        self.setWindowTitle("Расчет КПЭ")


    def uiconnect(self):
        self.ui.pushButton_login.clicked.connect(lambda: aut.log_in(self))
        self.ui.pushButton_logout.clicked.connect(lambda: aut.log_out(self))
        self.ui.pushButton_save_struktura.clicked.connect(lambda: aut.save_strukt(self))
        self.ui.comboBox_dolgn_red.currentIndexChanged.connect(lambda: shabl.vibor_shablon_rabotn(self))
        self.ui.comboBox_rabotn.currentIndexChanged.connect(lambda: kps.set_rabotn(self))
        self.ui.pushButton_save_red_kpi.clicked.connect(lambda: shabl.save_red_kpi(self))
        self.ui.pushButton_del_red_kpi.clicked.connect(lambda: shabl.del_red_kpi(self))
        self.ui.pushButton_save_sotr.clicked.connect(lambda: kps.save_sotr(self))

    def showdialog(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(msg)
        msg_box.setWindowTitle("Внимание!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)  # | QtWidgets.QMessageBox.Cancel)
        msg_box.exec()

    def showdialogYN(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(msg)
        msg_box.setWindowTitle("Внимание!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        return msg_box.exec()

    def actions(self):
        self.action_Smena_Parol = self.ui.action_chnge_pass
        self.action_Smena_Parol.triggered.connect(lambda: aut.smena_parol(self))
        self.action_new_user = self.ui.action_new_user
        self.action_new_user.triggered.connect(lambda: aut.new_user(self))



    def init_ui(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.lineEdit_3_nParol.setVisible(False)
        self.ui.lineEdit_3_nParol_2.setVisible(False)
        self.spis_emploe = F.otkr_f(F.tcfg('employee'), True, ',')
        F.ust_cvet_videl_tab(self.ui.tableWidget_struktura)
        F.ust_cvet_videl_tab(self.ui.tableWidget_red_kpi)

        self.spis_str_emploee = []
        for i in self.spis_emploe:
            self.spis_str_emploee.append(' '.join(i))
        self.ui.comboBox_empl.addItems(self.spis_str_emploee)
        self.regim_new_parol = False

        self.spis_dolg = []
        for i in self.spis_emploe:
            self.spis_dolg.append(' '.join(i[3:]))
        self.spis_dolg = list(set(self.spis_dolg))
        self.spis_dolg.sort()

        self.spis_dolg_filtr = []
        self.KPITIPS = ['Непрерывный','Понижающий','Отескающий']
        self.PROC = [str(i*5) for i in range(1,20)]

        self.shapka_shablonkpi = [
            ["Цель", "Наименование КПЭ", "Ед. изм.", "Уров.вып.№1", "Уров.вып.№2", "Уров.вып.№3", "Вес КПЭ", "Тип КПЭ",
             "Методика расчета", "Примечание"],
            ["-", "-", "-", "50", "100", "150", "-", "-",
             "-", "-"]]

    def app_icons(self):
        self.ui.pushButton_login.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogYesButton)))
        self.ui.pushButton_logout.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogNoButton)))
        self.ui.pushButton_del_red_kpi.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_BrowserStop)))

    def keyReleaseEvent(self, e):
        # print(str(int(e.modifiers())) + ' ' +  str(e.key()))
        if self.ui.lineEdit_parol.hasFocus():
            if e.key() == 16777220:
                self.ui.lineEdit_parol.clearFocus()
                aut.log_in(self)

    def load_combo(self):
        self.ui.comboBox_dolgn_red.addItems(self.spis_dolg_filtr)




app = QtWidgets.QApplication([])

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))

S = F.scfg('Stile').split(",")
app.setStyle(S[1])

application = Mywindow()
application.show()

sys.exit(app.exec())
