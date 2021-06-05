import Cust_Functions as F
from PyQt5 import QtWidgets

def vibor_shablon_rabotn(self):
    if self.ui.comboBox_dolgn_red.currentText() == '':
        return
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep()):
        F.sozd_dir(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep())
    if not F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle'):
        shapka = [["Цель", "Наименование КПЭ", "Ед. изм.", "Уров.вып.№1", "Уров.вып.№1", "Уров.вып.№1", "Вес КПЭ", "Тип КПЭ",
                   "Методика расчета", "Примечание"],
                  [ "-", "-", "-", "50", "100", "150", "-", "-",
                   "-", "-"]]
        F.zap_f(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle',
                shapka, pickl=True)
    spis = F.otkr_f(
        F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + self.ui.comboBox_dolgn_red.currentText() + '.pickle',
        pickl=True)
    spis.append(["" for i in range(len(spis[0]))])
    zapolit_tabl_shablon(self,spis)


def zapolit_tabl_shablon(self,spis):
    edit = {i for i in range(len(spis[0]))}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_red_kpi, 0, edit, (), (), 200, True, '')
    self.ui.tableWidget_red_kpi.setColumnWidth(1, 400)
    self.ui.tableWidget_red_kpi.setColumnWidth(0, 200)
    self.ui.tableWidget_red_kpi.setColumnWidth(7, 150)
    self.ui.tableWidget_red_kpi.setColumnWidth(8, 300)
    for i in range(1,self.ui.tableWidget_red_kpi.rowCount()):
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
    F.cvet_cell_wtabl(self.ui.tableWidget_red_kpi,'','','-')



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