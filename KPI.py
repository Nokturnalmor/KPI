import Cust_Functions as F
import autorization as aut
import shabloni as shabl
import kpi_sotr as kps
import vnesh as vnsh
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWinExtras import QtWin

import os

from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


# pyuic5 P:\Python\GUI\mydesign.ui -o P:\Python\GUI\mydesign.py
# pyinstaller.exe --onefile --noconsole KPI.py
class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Расчет КПЭ")
        self.init_ui()
        self.app_icons()
        self.actions()
        self.uiconnect()


    def uiconnect(self):
        self.ui.pushButton_login.clicked.connect(lambda: aut.log_in(self))
        self.ui.pushButton_logout.clicked.connect(lambda: aut.log_out(self))
        self.ui.pushButton_save_struktura.clicked.connect(lambda: aut.save_strukt(self))
        self.ui.comboBox_dolgn_red.currentIndexChanged.connect(lambda: shabl.vibor_shablon_rabotn(self))
        self.ui.comboBox_rabotn.currentIndexChanged.connect(lambda: kps.set_rabotn(self))
        self.ui.pushButton_save_red_kpi.clicked.connect(lambda: shabl.save_red_kpi(self))
        self.ui.pushButton_del_red_kpi.clicked.connect(lambda: shabl.del_red_kpi(self))
        self.ui.pushButton_save_sotr.clicked.connect(lambda: kps.save_sotr(self))
        self.ui.calendarWidget.currentPageChanged.connect(self.setdate)
        self.ui.pushButton_rasschet.clicked.connect(lambda: kps.rasschet_sotr(self))
        self.ui.pushButton_dell_line.clicked.connect(lambda: shabl.dell_line(self))
        self.ui.pushButton_line_up.clicked.connect(lambda: shabl.line_up(self))
        self.ui.tabWidget.currentChanged.connect(self.tab_click)
        self.ui.pushButton_del_kpi_sotr.clicked.connect(lambda: kps.del_kpi_sotr(self))


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
        F.ust_cvet_videl_tab(self.ui.tableWidget_kpi_sotr)
        F.ust_cvet_videl_tab(self.ui.tableWidget_kpi_vnesh)
        F.ust_cvet_videl_tab(self.ui.calendarWidget)

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
        self.KPITIPS = ['Непрерывный', 'Понижающий', 'Отескающий']
        self.PROC = [str(i * 5) for i in range(1, 20)]

        self.shapka_shablonkpi = [
            ["Цель", "Наименование КПЭ", "Ед. изм.", "Уров.вып.№1", "Уров.вып.№2", "Уров.вып.№3", "Вес КПЭ", "Тип КПЭ",
             "Методика расчета", "Примечание"],
            ["-", "-", "-", "50", "100", "150", "-", "-",
             "-", "-"]]

        self.ui.calendarWidget.setSelectionMode(0)
        self.setdate(self.ui.calendarWidget.yearShown(), self.ui.calendarWidget.monthShown())

        pixmap = QtGui.QPixmap(os.path.join("icons", "001.png"))
        self.ui.label_img.setPixmap(pixmap)


    def app_icons(self):
        self.ui.pushButton_login.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogYesButton)))
        self.ui.pushButton_logout.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogNoButton)))
        self.ui.pushButton_del_red_kpi.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))
        self.ui.pushButton_dell_line.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton)))
        self.ui.pushButton_del_kpi_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))
        self.ui.pushButton_line_up.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_ArrowUp)))
        self.ui.pushButton_save_struktura.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.pushButton_save_red_kpi.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.pushButton_save_vn.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.pushButton_load_vn.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogOpenButton)))
        self.ui.pushButton_save_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.pushButton_rasschet.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView)))
        self.ui.pushButton_del_kpi_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))

    def keyReleaseEvent(self, e):
        # print(str(int(e.modifiers())) + ' ' +  str(e.key()))
        if self.ui.lineEdit_parol.hasFocus():
            if e.key() == 16777220:
                self.ui.lineEdit_parol.clearFocus()
                aut.log_in(self)

    def load_combo(self):
        self.ui.comboBox_dolgn_red.clear()
        self.ui.comboBox_dolgn_red.addItems(self.spis_dolg_filtr)

    def setdate(self, g, m):
        self.ui.label_period.setText(f'{self.month_name(m).capitalize()} {str(g)}')
        self.tab_click1()


    def month_name(self, num):
        ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
              'октябрь', 'ноябрь', 'декабрь']
        return ru[num - 1]

    def tab_click(self):
        if self.windowTitle() == 'Расчет КПЭ':
            return
        if self.ui.tabWidget.currentIndex() == 1:
            self.tab_click1()  # Дата
        if self.ui.tabWidget.currentIndex() == 2:
            self.tab_click2()  # КПЭсотр.
        if self.ui.tabWidget.currentIndex() == 3:
            self.tab_click3()  # КПЭвнеш.
        if self.ui.tabWidget.currentIndex() == 4:
            self.tab_click4()  # Редактор КПЭ
        if self.ui.tabWidget.currentIndex() == 5:
            self.tab_click5()  # Структура

    def tab_click5(self):
        aut.load_strukt(self)
        aut.load_filtr(self)

    def tab_click4(self):
        aut.load_strukt(self)
        self.load_combo()

    def tab_click3(self):
        vnsh.zapoln_vnsh_tabl(self)

    def tab_click2(self):
        aut.load_combo_sotr(self)

    def tab_click1(self):
        self.ui.label_kpi_otd.setText(str(0))
        if self.windowTitle() == 'Расчет КПЭ':
            return
        period = self.ui.label_period.text()
        if F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + period + F.sep()) == False:
            return
        spis_files = F.spis_files(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + period + F.sep())[0]
        summ = 0
        shet= 0
        for i in spis_files[2]:
            spis = F.otkr_f(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + period + F.sep()+i)

            if kps.proverka_dannih(self,spis) == False:
                continue

            kol_fact = F.nom_kol_po_im_v_shap(spis, 'Факт. вып.')
            kol_tip = F.nom_kol_po_im_v_shap(spis, "Тип КПЭ")
            kol_z1 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№1")
            kol_z2 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№2")
            kol_z3 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№3")
            kol_ves = F.nom_kol_po_im_v_shap(spis, "Вес КПЭ")
            for i in range(2, len(spis)):
                if spis[i][kol_tip] == self.KPITIPS[0]:
                    summ += kps.rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3) * int(spis[i][kol_ves]) / 100
                if spis[i][kol_tip] == self.KPITIPS[1]:
                    summ -= int(spis[i][kol_fact]) * int(spis[i][kol_ves])
                if spis[i][kol_tip] == self.KPITIPS[2]:
                    summ -= summ * int(spis[i][kol_fact])
            shet+=1
        summ = round(summ/shet,1)
        self.ui.label_kpi_otd.setText(str(summ))




app = QtWidgets.QApplication([])

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))

S = F.scfg('Stile').split(",")
app.setStyle(S[1])

application = Mywindow()
application.show()

sys.exit(app.exec())
