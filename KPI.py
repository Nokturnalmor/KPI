import Cust_Functions as F
import autorization as aut
import shabloni as shabl
import kpi_sotr as kps
import vnesh as vnsh
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWinExtras import QtWin
import os
from docxtpl import DocxTemplate

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
        self.ui.btn_login.clicked.connect(lambda: aut.log_in(self))
        self.ui.btn_logout.clicked.connect(lambda: aut.log_out(self))
        self.ui.btn_save_struktura.clicked.connect(lambda: aut.save_strukt(self))
        self.ui.cmb_dolgn_red.currentIndexChanged.connect(lambda: shabl.vibor_shablon_rabotn(self))
        self.ui.cmb_rabotn.currentIndexChanged.connect(lambda: kps.set_rabotn(self))
        self.ui.btn_save_red_kpi.clicked.connect(lambda: shabl.save_red_kpi(self))
        self.ui.btn_del_red_kpi.clicked.connect(lambda: shabl.del_red_kpi(self))
        self.ui.btn_save_sotr.clicked.connect(lambda: kps.save_sotr(self))
        self.ui.clnd.currentPageChanged.connect(self.setdate)
        self.ui.btn_rasschet.clicked.connect(lambda: kps.rasschet_sotr(self))
        self.ui.btn_dell_line.clicked.connect(lambda: shabl.dell_line(self))
        self.ui.btn_line_up.clicked.connect(lambda: shabl.line_up(self))
        self.ui.tabWidget.currentChanged.connect(self.tab_click)
        self.ui.btn_del_kpi_sotr.clicked.connect(lambda: kps.del_kpi_sotr(self))
        self.ui.btn_save_vn.clicked.connect(lambda: vnsh.save_vn(self))
        self.ui.tbl_kpi_vnesh.cellChanged.connect(lambda: vnsh.podschet(self))
        self.ui.btn_export.clicked.connect(lambda: kps.export(self))
        self.ui.btn_export_pr.clicked.connect(self.export_pr)

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
        self.ui.le_3_nParol.setVisible(False)
        self.ui.le_3_nParol_2.setVisible(False)
        self.spis_emploe = F.otkr_f(F.tcfg('employee'), True, ',')
        F.ust_cvet_videl_tab(self.ui.tbl_struktura)
        F.ust_cvet_videl_tab(self.ui.tbl_red_kpi)
        F.ust_cvet_videl_tab(self.ui.tbl_kpi_sotr)
        F.ust_cvet_videl_tab(self.ui.tbl_kpi_vnesh)
        F.ust_cvet_videl_tab(self.ui.clnd)

        self.spis_str_emploee = []
        for i in self.spis_emploe:
            self.spis_str_emploee.append(' '.join(i))
        self.ui.cmb_empl.addItems(self.spis_str_emploee)
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

        self.ui.clnd.setSelectionMode(0)
        self.setdate(self.ui.clnd.yearShown(), self.ui.clnd.monthShown())

        pixmap = QtGui.QPixmap(os.path.join("icons", "001.png"))
        self.ui.l_img.setPixmap(pixmap)

    def app_icons(self):
        self.ui.btn_login.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogYesButton)))
        self.ui.btn_logout.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogNoButton)))
        self.ui.btn_del_red_kpi.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))
        self.ui.btn_dell_line.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton)))
        self.ui.btn_del_kpi_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))
        self.ui.btn_line_up.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_ArrowUp)))
        self.ui.btn_save_struktura.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.btn_save_red_kpi.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.btn_save_vn.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.btn_load_vn.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogOpenButton)))
        self.ui.btn_save_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton)))
        self.ui.btn_rasschet.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogDetailedView)))
        self.ui.btn_del_kpi_sotr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DialogDiscardButton)))
        self.ui.btn_export.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DriveHDIcon)))
        self.ui.btn_export_pr.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_DriveHDIcon)))
        self.ui.btn_utverg.setIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_BrowserReload)))#QStyle.SP_VistaShield

    def keyReleaseEvent(self, e):
        # print(str(int(e.modifiers())) + ' ' +  str(e.key()))
        if self.ui.le_parol.hasFocus():
            if e.key() == 16777220:
                self.ui.le_parol.clearFocus()
                aut.log_in(self)

    def load_combo(self):
        self.ui.cmb_dolgn_red.clear()
        self.ui.cmb_dolgn_red.addItems(self.spis_dolg_filtr)

    def setdate(self, g, m):
        self.ui.l_period.setText(f'{self.month_name(m).capitalize()} {str(g)}')
        self.tab_click1()

    @staticmethod
    def month_name(num):
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

    def msg_export(self):
        spis_otd = vnsh.spispok_otdelov(self, True)
        spis_otd_n = vnsh.spispok_otdelov(self)
        period = self.ui.l_period.text()
        kpi_otd_summ = 0
        sch = 0
        otsp = "  "
        msg = ''
        itog= ''
        for i in range(len(spis_otd)):
            fio_ruc = spis_otd[i]
            msg +=(f'Подразделение {spis_otd_n[i]}, руководитель {fio_ruc}:'+ '\n')
            spis_files = F.spis_files(F.scfg('strukt') + F.sep() + fio_ruc + F.sep() + period + F.sep())[0][2]
            msg +=(otsp + 'Сотрудники:'+ '\n')
            for sotr in spis_files:
                if "$vn" in sotr:
                    continue
                ima_sotr = sotr.split('$')[1]
                ima_sotr = otsp * 2 + ima_sotr.replace('.pickle', '')
                msg +=(ima_sotr + ' ' + str(self.rasch_kpi_sotr(fio_ruc, period, sotr)) + '%'+ '\n')
            spis_vn = self.rasch_kpi_otd_vn(spis_otd_n[i], True)
            for j in range(len(spis_vn)):
                msg +=(f'{otsp}Оценен подразделением {spis_vn[j][0]} на {spis_vn[j][1]}%:'+ '\n')
                for key in spis_vn[j][2].keys():
                    msg +=(f'{otsp * 2 + key}: {", ".join(spis_vn[j][2][key])}'+ '\n')

            spis_d_po_otdely = self.rasch_kpi_otdela(fio_ruc)
            summ = spis_d_po_otdely[0]
            sr_vn = spis_d_po_otdely[3]
            kpi_otd_num = round((summ * 2 + sr_vn) / 3)
            msg +=("КПЭ отдела: " + str(kpi_otd_num) + "%"+ '\n')
            msg +=( '\n')
            msg +=( '\n')
            kpi_otd_summ += kpi_otd_num
            sch += 1
        itog +=("КПЭ производства: " + str(round(kpi_otd_summ / sch)) + "%")
        return [msg, itog]

    def export_pr(self):
        if F.nalich_file(os.path.join("icons", "Шаблон_п.docx")) == False:
            self.showdialog("шаблон не найден")
            return
        s_msg = self.msg_export()
        msg = s_msg[0]
        itog = s_msg[1]

        doc = DocxTemplate(os.path.join("icons", "Шаблон_п.docx"))
        context = {'period': self.ui.l_period.text(), 'msg': msg,
                   'itog': itog, 'now': F.now()}

        doc.render(context)
        if F.nalich_file(F.put_po_umolch() + os.sep + 'КПЭ' + os.sep) == False:
            F.sozd_dir(F.put_po_umolch() + os.sep + 'КПЭ' + os.sep)
        putf = f'{F.put_po_umolch()}{os.sep}КПЭ{os.sep}Производство${self.ui.l_period.text()}.docx'
        doc.save(putf)
        F.zapyst_file(putf)
        return


    def rasch_kpi_sotr(self,fio_ruc,period,ima_faila):
        spis = F.otkr_f(F.scfg(
            'strukt') + F.sep() + fio_ruc + F.sep() + period + F.sep() + ima_faila)
        summ = 0
        if kps.proverka_dannih(self, spis) == False:
            return summ
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
        return round(summ,1)

    def rasch_kpi_otd_vn(self,ima_otd,export=False):
        summ_vn = 0
        schet_vn = 0
        spis_t = []
        if F.nalich_file(F.scfg(
                'strukt') + F.sep() + self.ui.l_period.text() + '$vn.pickle'):
            spis_vn = F.otkr_f(F.scfg(
                'strukt') + F.sep() + self.ui.l_period.text() + '$vn.pickle', False, "", True)
            for x in range(len(spis_vn)):
                for y in spis_vn[x]:
                    for z in spis_vn[x][y]:
                        if z == ima_otd:
                            summ_vn += int(spis_vn[x][y][z][0])
                            schet_vn += 1
                            if export== True:
                                spis_t.append([y,int(spis_vn[x][y][z][0]),{'Замечания': spis_vn[x][y][z][1],'Поощрения': spis_vn[x][y][z][2]}])
        if export:
            return spis_t
        else:
            return [summ_vn,schet_vn]

    def rasch_kpi_otdela(self, fio_ruc:str):
        period = self.ui.l_period.text()
        if F.nalich_file(F.scfg('strukt') + F.sep() + fio_ruc + F.sep() + period + F.sep()) == False:
            return
        spis_files = F.spis_files(F.scfg('strukt') + F.sep() + fio_ruc + F.sep() + period + F.sep())[0]
        summ = 0
        shet = 0
        for i in spis_files[2]:
            if "$vn" in i:
                continue
            summ_sotr = self.rasch_kpi_sotr(fio_ruc,period,i)
            summ += summ_sotr
            shet += 1
        summ = round(summ / shet, 1)
        ima_otd = vnsh.ima_otd(self,fio_ruc)
        sr_vn = 100
        vn = self.rasch_kpi_otd_vn(ima_otd)
        sr_vn = vn[0] / vn[1]
        return [summ,vn[0],vn[1],sr_vn]

    def tab_click1(self):
        self.ui.l_kpi_otd.setText(str(0))
        if self.windowTitle() == 'Расчет КПЭ':
            return
        spis_summ = self.rasch_kpi_otdela(self.windowTitle())
        summ = spis_summ[0]
        sr_vn = spis_summ[3]
        summ_vn = spis_summ[1]
        schet_vn = spis_summ[2]
        self.ui.l_kpi_otd.setText(f'{str(round((summ * 2 + sr_vn) / 3))} (сумм.КПЭсотр./Nсотр.:{str(summ)}, '
                                  f'сумм. КПЭ окр.:{str(summ_vn)}, Nотд-1:{str(schet_vn)})')
        kpi_proizv_t = ''
        kpi_proizv = 0
        schet = 0
        spis_otd = vnsh.spispok_otdelov(self,True)
        for i in spis_otd:
            summ_tmp = self.rasch_kpi_otdela(i)
            #print(summ_tmp)
            if summ_tmp == None:
                continue
            kpi_proizv += round(((summ_tmp[0] * 2 + summ_tmp[3]) / 3))
            kpi_proizv_t += str(round(((summ_tmp[0] * 2 + summ_tmp[3]) / 3))) + '  '
            schet+=1
        kpi_proizv = round(kpi_proizv/schet,1)
        self.ui.l_kpi_pr.setText(str(kpi_proizv) + "(" + kpi_proizv_t + ")")


    def fio(self, strok:str):
        return " ".join(strok.split(' ')[:3])

app = QtWidgets.QApplication([])

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))

S = F.scfg('Stile').split(",")
app.setStyle(S[1])

application = Mywindow()
application.show()

sys.exit(app.exec())
