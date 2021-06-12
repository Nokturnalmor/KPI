import Cust_Functions as F
from PyQt5 import QtWidgets, QtGui, QtCore

def zapoln_vnsh_tabl(self):
    global nom_tek_otdel
    if self.windowTitle() == "Расчет КПЭ":
        return
    spis_otdelov = spispok_otdelov(self)
    tek_otdel = spis_otdelov[0]
    spis_otdelov.pop(0)
    spis = [['']]
    for k in spis_otdelov:
        tmps = ['' for _ in range(len(spis[0])-1)]
        spis.append([k]+tmps)
        spis[0].append(k)
        for i in range(1,len(spis)):
            spis[i].append("")
    for i in range(10):
        spis.append(['Замечание'] + ['' for _ in range(len(spis[0])-1)])
    for i in range(5):
        spis.append(['Поощрение'] + ['' for _ in range(len(spis[0])-1)])
    F.zapoln_wtabl(self,spis,self.ui.tableWidget_kpi_vnesh,0,0,(),(),200,False,"")
    F.ust_cvet_obj(self.ui.tableWidget_kpi_vnesh)
    for i in range(self.ui.tableWidget_kpi_vnesh.rowCount()):
        if self.ui.tableWidget_kpi_vnesh.item(i,0).text() == tek_otdel:
            nom_tek_otdel = i
            for j in range(self.ui.tableWidget_kpi_vnesh.columnCount()):
                F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh,i,j,235,235,235)
    for i in range(self.ui.tableWidget_kpi_vnesh.columnCount()):
        F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh, i, i, 200, 200, 200)
    for i in range(1,4):
        self.ui.tableWidget_kpi_vnesh.setColumnWidth(i, (self.ui.tableWidget_kpi_vnesh.width()-self.ui.tableWidget_kpi_vnesh.columnWidth(0)) / 3)
    for i in range(self.ui.tableWidget_kpi_vnesh.columnCount(), self.ui.tableWidget_kpi_vnesh.columnCount()+10):
        for j in range(1,self.ui.tableWidget_kpi_vnesh.columnCount()):
            if j != nom_tek_otdel:
                self.ui.tableWidget_kpi_vnesh.item(i,j).setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh, i, j, 255, 255, 255)
        F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh, i, 0, 255, 200, 200)
    for i in range(self.ui.tableWidget_kpi_vnesh.columnCount()+10, self.ui.tableWidget_kpi_vnesh.rowCount()):
        for j in range(1,self.ui.tableWidget_kpi_vnesh.columnCount()):
            if j != nom_tek_otdel:
                self.ui.tableWidget_kpi_vnesh.item(i,j).setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh, i, j, 255, 255, 255)
        F.ust_color_wtab(self.ui.tableWidget_kpi_vnesh, i, 0, 200, 255, 200)



def spispok_otdelov(self):
    spis_pap = F.spis_files(F.scfg('strukt') + F.sep())[0][1]
    spis_otdelov = []
    for i in spis_pap:
        if F.nalich_file(F.scfg('strukt') + F.sep() + i + F.sep() + 'strukt.pickle') == True:
            spis = F.otkr_f(F.scfg('strukt') + F.sep() + i + F.sep() + 'strukt.pickle',"","",True)
            spis_otdelov.append(spis[1][0])
            if spis[1][1] == self.windowTitle():
                tek_otd = spis[1][0]
    return [tek_otd] + spis_otdelov