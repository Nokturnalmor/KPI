import Cust_Functions as F
from PyQt5 import QtCore

def ima_otd(self,fio_ruc):
    spis = F.otkr_f(F.scfg('strukt') + F.sep() + fio_ruc + F.sep() + 'strukt.pickle', "", "", True)
    if spis[1][1] == fio_ruc:
        return spis[1][0]
    return

def zapoln_vnsh_tabl(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    self.ui.l_tek_otd.setText(ima_otd(self,self.windowTitle()))
    name = self.ui.l_period.text() + "$" + self.ui.l_tek_otd.text()
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.l_period.text() + F.sep() + name + "$" +
                'vn.pickle') == True:
        spis = F.otkr_f(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.l_period.text() + F.sep() + name + "$" +
                'vn.pickle',False,"",True)
        spis.pop(0)
    else:
        spis_otdelov = spispok_otdelov(self)
        spis = [['']]
        for k in spis_otdelov:
            tmps = ['' for _ in range(len(spis[0])-1)]
            spis.append([k]+tmps)
            spis[0].append(k)
            for i in range(1, len(spis)):
                spis[i].append("")
        for i in range(10):
            spis.append(['Замечание'] + ['' for _ in range(len(spis[0])-1)])
        for i in range(5):
            spis.append(['Поощрение'] + ['' for _ in range(len(spis[0])-1)])

    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.ui.l_period.text() + '$vn.pickle'):
        spis_vn = F.otkr_f(F.scfg(
            'strukt') + F.sep() + self.ui.l_period.text() + '$vn.pickle', False, "", True)
        for i in range(1,len(spis)-15):
            for x in range(len(spis_vn)):
                if list(spis_vn[x].keys())[0] == spis[i][0]:
                    for j in range(1,len(spis[0])):
                        for y in spis_vn[x][spis[i][0]]:
                            if spis[0][j] == y:
                                spis[i][j] = spis_vn[x][spis[i][0]][y][0]
    nom_tek_otdel = 0
    F.zapoln_wtabl(self, spis, self.ui.tbl_kpi_vnesh, 0, 0, (), (), 200, False, "")
    F.ust_cvet_obj(self.ui.tbl_kpi_vnesh)
    for i in range(self.ui.tbl_kpi_vnesh.rowCount()):# ткущий отдел
        if self.ui.tbl_kpi_vnesh.item(i, 0).text() == self.ui.l_tek_otd.text():
            nom_tek_otdel = i
            for j in range(self.ui.tbl_kpi_vnesh.columnCount()):
                F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, j, 255, 235, 255)
    for i in range(self.ui.tbl_kpi_vnesh.columnCount()):# диагональ
        F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, i, 200, 200, 200)
    for i in range(1, 4):# ширина стоблбов
        self.ui.tbl_kpi_vnesh.setColumnWidth(i,
                                             (self.ui.tbl_kpi_vnesh.width()-self.ui.tbl_kpi_vnesh.columnWidth(0)) / 3)
    for i in range(self.ui.tbl_kpi_vnesh.columnCount(), self.ui.tbl_kpi_vnesh.columnCount()+10):# редакатир столбцы зам
        for j in range(1, self.ui.tbl_kpi_vnesh.columnCount()):
            if j != nom_tek_otdel:
                self.ui.tbl_kpi_vnesh.item(i, j).setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, j, 255, 255, 255)
        F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, 0, 255, 200, 200)
    for i in range(self.ui.tbl_kpi_vnesh.columnCount()+10, self.ui.tbl_kpi_vnesh.rowCount()):# редакатир столбцы поощ
        for j in range(1, self.ui.tbl_kpi_vnesh.columnCount()):
            if j != nom_tek_otdel:
                self.ui.tbl_kpi_vnesh.item(i, j).setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, j, 255, 255, 255)
        F.ust_color_wtab(self.ui.tbl_kpi_vnesh, i, 0, 200, 255, 200)



def spispok_otdelov(self, ruc = False):
    spis_pap = F.spis_files(F.scfg('strukt') + F.sep())[0][1]
    spis_otdelov = []
    tek_otd = ""
    for i in spis_pap:
        if F.nalich_file(F.scfg('strukt') + F.sep() + i + F.sep() + 'strukt.pickle'):
            spis = F.otkr_f(F.scfg('strukt') + F.sep() + i + F.sep() + 'strukt.pickle', "", "", True)
            if ruc == True:
                spis_otdelov.append(spis[1][1])
            else:
                spis_otdelov.append(spis[1][0])
    return spis_otdelov


def proverka_dannih(self):
    tbl = self.ui.tbl_kpi_vnesh
    for i in range(tbl.rowCount()-1,tbl.rowCount()-16,-1):
        for j in range(1,tbl.columnCount()):
            tbl.item(i,j).setText(tbl.item(i,j).text().strip())
    return True


def save_vn(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    if not proverka_dannih(self):
        return
    spis = F.spisok_iz_wtabl(self.ui.tbl_kpi_vnesh, '', True)
    name = self.ui.l_period.text() + "$" + self.ui.l_tek_otd.text()
    if not F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.l_period.text()):
        F.sozd_dir(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.l_period.text())
    F.zap_f(F.scfg(
        'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.l_period.text() + F.sep() + name + "$" +
            'vn.pickle',
            spis, pickl=True)
    zapisvbd(self)
    self.showdialog(
        f'Ведомость на {self.ui.l_period.text()} успешно сохранена')
    zapoln_vnsh_tabl(self)

def zapisvbd(self):
    period = self.ui.l_period.text()
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + period + '$vn.pickle') == False:
        spis = []
    else:
        spis = F.otkr_f(F.scfg(
            'strukt') + F.sep() + period + '$vn.pickle', False, "", True)
    tbl = self.ui.tbl_kpi_vnesh
    slov = {}
    for j in range(1, tbl.columnCount()):
        ball= 100
        if tbl.item(0, j).text() == self.ui.l_tek_otd.text():
            continue
        poosh = []
        for i in range(tbl.rowCount() - 1, tbl.rowCount() - 6, -1):
            if tbl.item(i, j).text() != '':
                poosh.append(tbl.item(i, j).text())
        zam = []
        for i in range(tbl.rowCount() - 6, tbl.rowCount() - 16, -1):
            if tbl.item(i, j).text() != '':
                zam.append(tbl.item(i, j).text())
        for i in range(tbl.rowCount() - 16, -1, -1):
            if tbl.item(i, 0).text() == self.ui.l_tek_otd.text():
                ball = tbl.item(i, j).text()
                break
        slov[tbl.item(0, j).text()] = [ball,zam,poosh]
    slov_podr = {self.ui.l_tek_otd.text():slov}
    flag_naid = False
    for i in range(0,len(spis)):
        if list(spis[i].keys())[0] == self.ui.l_tek_otd.text():
            spis[i] = slov_podr
            flag_naid = True
            break
    if flag_naid == False:
        spis.append(slov_podr)
    F.zap_f(F.scfg(
            'strukt') + F.sep() + period + '$vn.pickle',spis,"",True)




def podschet(self):
    tbl = self.ui.tbl_kpi_vnesh
    if tbl.hasFocus() == False:
        return
    if self.ui.tabWidget.currentIndex() != 3:
        return
    for j in range(1, tbl.columnCount()):
        if tbl.item(0, j) == None:
            return
        if tbl.item(0, j).text() == self.ui.l_tek_otd.text():
            continue
        summ_poosh = 0
        for i in range(tbl.rowCount() - 1, tbl.rowCount() - 6, -1):
            if tbl.item(i, j) == None:
                return
            if tbl.item(i, j).text().strip() != '':
                summ_poosh += 1
        summ_zam = 0
        for i in range(tbl.rowCount() - 6, tbl.rowCount() - 16, -1):
            if tbl.item(i, j).text().strip() != '':
                summ_zam += 1
        for i in range(tbl.rowCount() - 16, -1, -1):
            if tbl.item(i, 0).text() == self.ui.l_tek_otd.text():
                tbl.item(i, j).setText(str(100 - summ_zam*5 + summ_poosh*10))
                break