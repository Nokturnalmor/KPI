import Cust_Functions as F
from PyQt5 import QtWidgets


def vibor_shablon_rabotn(self):
    if self.ui.comboBox_dolgn_red.currentText() == '':
        return
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep()):
        F.sozd_dir(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep())
    if not F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle'):
        F.zap_f(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle',
                self.shapka_shablonkpi, pickl=True)
    spis = F.otkr_f(
        F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle',
        pickl=True)
    spis.append(["" for i in range(len(spis[0]))])
    zapolit_tabl_shablon(self, spis)


def zapolit_tabl_shablon(self, spis):
    edit = {i for i in range(len(spis[0]))}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_red_kpi, 0, edit, (), (), 200, True, '')
    self.ui.tableWidget_red_kpi.setColumnWidth(1, 450)
    self.ui.tableWidget_red_kpi.setColumnWidth(0, 300)
    self.ui.tableWidget_red_kpi.setColumnWidth(7, 150)
    self.ui.tableWidget_red_kpi.setColumnWidth(8, 300)
    for i in range(1, self.ui.tableWidget_red_kpi.rowCount()):
        combo = QtWidgets.QComboBox()
        combo.addItem("")
        for item in self.KPITIPS:
            combo.addItem(item)
            if self.ui.tableWidget_red_kpi.item(i, 7).text() == item:
                combo.setCurrentText(item)
        combo.currentIndexChanged.connect((lambda: onStateChanged1(self)))
        self.ui.tableWidget_red_kpi.setCellWidget(i, 7, combo)

        combo2 = QtWidgets.QComboBox()
        combo2.addItem("")
        for item in self.PROC:
            combo2.addItem(item)
            if self.ui.tableWidget_red_kpi.item(i, 6).text() == item:
                combo2.setCurrentText(item)
        combo2.currentIndexChanged.connect((lambda: onStateChanged2(self)))
        self.ui.tableWidget_red_kpi.setCellWidget(i, 6, combo2)
    F.cvet_cell_wtabl(self.ui.tableWidget_red_kpi, '', '', '-')
    self.ui.tableWidget_red_kpi.resizeRowsToContents()


def onStateChanged1(self):
    ch = self.sender()
    ix = self.ui.tableWidget_red_kpi.indexAt(ch.pos())
    print(ix.row(), ix.column(), ch.currentText())
    self.ui.tableWidget_red_kpi.item(ix.row(), ix.column()).setText(ch.currentText())

    if self.ui.tableWidget_red_kpi.rowCount() - 1 == ix.row() and ch.currentText() != '':
        spis = F.spisok_iz_wtabl(self.ui.tableWidget_red_kpi, '', True)
        spis.append(["" for i in range(len(spis[0]))])
        zapolit_tabl_shablon(self, spis)


def onStateChanged2(self):
    ch = self.sender()
    ix = self.ui.tableWidget_red_kpi.indexAt(ch.pos())
    print(ix.row(), ix.column(), ch.currentText())
    self.ui.tableWidget_red_kpi.item(ix.row(), ix.column()).setText(ch.currentText())
    if self.ui.tableWidget_red_kpi.rowCount() - 1 == ix.row() and ch.currentText() != '':
        spis = F.spisok_iz_wtabl(self.ui.tableWidget_red_kpi, '', True)
        spis.append(["" for i in range(len(spis[0]))])
        zapolit_tabl_shablon(self, spis)


def proverka_red_kpi(self):
    for j in range(2):
        self.ui.tableWidget_red_kpi.item(0, j).setText('-')
    for j in range(6, self.ui.tableWidget_red_kpi.columnCount()):
        self.ui.tableWidget_red_kpi.item(0, j).setText('-')
    for j in range(3, 6):
        if F.is_numeric(self.ui.tableWidget_red_kpi.item(0, j).text()) == False:
            self.showdialog(f'{self.shapka_shablonkpi[0][j]} не является числом')
            F.migat(self, self.ui.tableWidget_red_kpi, 0, j)
            return False
    for i in range(1, self.ui.tableWidget_red_kpi.rowCount()):
        if proverka_stroki_zap(self, i) == False:
            return False

    spis_tmp = F.spisok_iz_wtabl(self.ui.tableWidget_red_kpi, '', True)
    spis = []
    nom_kol_y1 = F.nom_kol_po_im_v_shap(spis_tmp, self.shapka_shablonkpi[0][3])
    nom_kol_y2 = F.nom_kol_po_im_v_shap(spis_tmp, self.shapka_shablonkpi[0][4])
    nom_kol_y3 = F.nom_kol_po_im_v_shap(spis_tmp, self.shapka_shablonkpi[0][5])
    nom_kol_tip = F.nom_kol_po_im_v_shap(spis_tmp, self.shapka_shablonkpi[0][7])
    spis.append(spis_tmp[0])
    spis.append(spis_tmp[1])
    for i in range(2, len(spis_tmp)):
        flag_pust = True
        for j in range(len(spis_tmp[i])):
            if spis_tmp[i][j] != '':
                flag_pust = False
                break
        if flag_pust == False:
            for j in range(len(spis_tmp[i])):
                spis_tmp[i][j] = spis_tmp[i][j].strip()
            spis.append(spis_tmp[i])
        if spis_tmp[i][nom_kol_tip] != self.KPITIPS[0]:
            spis_tmp[i][nom_kol_y1] = '-'
            spis_tmp[i][nom_kol_y2] = '-'
            spis_tmp[i][nom_kol_y3] = '-'
    if len(spis) == 2:
        self.showdialog(f'Таблица не может быть пустой')
        return False
    if proverka_summ(self, spis) != 100:
        self.showdialog(
            f'Сумма {self.shapka_shablonkpi[0][6]} где {self.shapka_shablonkpi[0][7]} {self.KPITIPS[0]} '
            f'должна быть равна 100, сейчас {str(proverka_summ(self, spis))}')
        return False

    if proverka_summ_ponig(self, spis) > int(spis[1][nom_kol_y1]):
        self.showdialog(
            f'Сумма {self.shapka_shablonkpi[0][6]} где {self.shapka_shablonkpi[0][7]} {self.KPITIPS[1]} '
            f'должна не более {spis[1][nom_kol_y1]}, сейчас {str(proverka_summ_ponig(self, spis))}')
        return False
    return spis


def proverka_summ(self, spis):
    summ = 0
    for i in range(1, len(spis)):
        if spis[i][7] == self.KPITIPS[0]:
            summ += int(spis[i][6])
    return summ


def proverka_summ_ponig(self, spis):
    summ = 0
    for i in range(1, len(spis)):
        if spis[i][7] == self.KPITIPS[1]:
            summ += int(spis[i][6])
    return summ


def proverka_stroki_zap(self, i):
    spis_kol_numeric = [3, 4, 5, 6]
    flag_vse = True
    flag_nepr = self.ui.tableWidget_red_kpi.item(i, F.nom_kol_po_imen(self.ui.tableWidget_red_kpi,
                                                             self.shapka_shablonkpi[0][7])).text() == self.KPITIPS[
        0]
    for j in range(self.ui.tableWidget_red_kpi.columnCount() - 1):
        if flag_nepr and self.ui.tableWidget_red_kpi.item(i, j).text() != "":
            if flag_vse == True:
                for k in range(self.ui.tableWidget_red_kpi.columnCount() - 1):
                    if self.ui.tableWidget_red_kpi.item(i, k).text() == "":
                        self.showdialog(f'{self.shapka_shablonkpi[0][k]}, строка {i + 1} не заполнена')
                        F.migat(self, self.ui.tableWidget_red_kpi, i, k)
                        return False
            if j in spis_kol_numeric:
                if flag_nepr and F.is_numeric(self.ui.tableWidget_red_kpi.item(i, j).text()) == False:
                    self.showdialog(f'{self.shapka_shablonkpi[0][j]}, строка {i + 1} не число')
                    F.migat(self, self.ui.tableWidget_red_kpi, i, j)
                    return False
            flag_vse = False
    if flag_nepr and flag_vse == False:
        if int(self.ui.tableWidget_red_kpi.item(i, 4).text()) < int(self.ui.tableWidget_red_kpi.item(i, 5).text()) and \
                int(self.ui.tableWidget_red_kpi.item(i, 4).text()) > int(
            self.ui.tableWidget_red_kpi.item(i, 3).text()) or \
                int(self.ui.tableWidget_red_kpi.item(i, 4).text()) > int(
            self.ui.tableWidget_red_kpi.item(i, 5).text()) and \
                int(self.ui.tableWidget_red_kpi.item(i, 4).text()) < int(self.ui.tableWidget_red_kpi.item(i, 3).text()):
            pass
        else:
            self.showdialog(
                f'{self.shapka_shablonkpi[0][4]}, строка {i + 1} не может быть вне {self.shapka_shablonkpi[0][3]},{self.shapka_shablonkpi[0][5]} ')
            F.migat(self, self.ui.tableWidget_red_kpi, i, 4, 2)
            return False
    if flag_vse == True:
        return True
    else:
        return


def save_red_kpi(self):
    rez = proverka_red_kpi(self)
    if rez == False:
        return
    else:
        F.zap_f(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle',
                rez, pickl=True)
        self.showdialog(
            f'Шаблон КПЭ на {self.ui.comboBox_dolgn_red.currentText()} успешно сохранен')
        vibor_shablon_rabotn(self)
    return


def del_red_kpi(self):
    rez = self.showdialogYN(f'Будет сброшен шаблон для {self.ui.comboBox_dolgn_red.currentText()}')
    if rez == 1024:  #:no 4194304
        F.udal_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle')

        vibor_shablon_rabotn(self)
        self.showdialog(f'Шаблон для {self.ui.comboBox_dolgn_red.currentText()} успешно сброшен.\n'
                        f'его не вернуть.\n'
                        f'никак.')


def dell_line(self):
    if self.ui.tableWidget_red_kpi.currentIndex().row() <= 0:
        return
    if self.ui.tableWidget_red_kpi.currentIndex().row() == self.ui.tableWidget_red_kpi.rowCount() - 1:
        kol_ves = F.nom_kol_po_imen(self.ui.tableWidget_red_kpi, "Вес КПЭ")
        kol_tip = F.nom_kol_po_imen(self.ui.tableWidget_red_kpi, "Тип КПЭ")
        for k in range(self.ui.tableWidget_red_kpi.columnCount()):
            self.ui.tableWidget_red_kpi.item(self.ui.tableWidget_red_kpi.currentIndex().row(), k).setText('')
        self.ui.tableWidget_red_kpi.cellWidget(self.ui.tableWidget_red_kpi.currentIndex().row(),
                                               kol_ves).setCurrentText('')
        self.ui.tableWidget_red_kpi.cellWidget(self.ui.tableWidget_red_kpi.currentIndex().row(),
                                               kol_tip).setCurrentText('')
    else:
        self.ui.tableWidget_red_kpi.removeRow(self.ui.tableWidget_red_kpi.currentIndex().row())


def line_up(self):
    sel = self.ui.tableWidget_red_kpi.currentIndex().row() + 1
    if sel < 3:
        return
    kol = self.ui.tableWidget_red_kpi.currentIndex().column()
    spis_tmp = F.spisok_iz_wtabl(self.ui.tableWidget_red_kpi, '', True)
    spis_tmp[sel], spis_tmp[sel - 1] = spis_tmp[sel - 1], spis_tmp[sel]
    zapolit_tabl_shablon(self, spis_tmp)
    self.ui.tableWidget_red_kpi.setCurrentCell(sel - 2, kol)
