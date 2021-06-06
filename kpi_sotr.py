import Cust_Functions as F
def set_rabotn(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    dolgn =' '.join(self.ui.comboBox_rabotn.currentText().split(' ')[3:])
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + dolgn + '.pickle') == False:
        self.showdialog(f'Не найден шаблон {dolgn}')
        return
    spis = F.otkr_f(
        F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + dolgn + '.pickle',
        pickl=True)
    vstav_pol = 9
    spis[0].insert(vstav_pol,'Факт. вып.')
    spis[1].insert(vstav_pol,'-')
    for i in range(2,len(spis)):
        spis[i].insert(vstav_pol,'')
    zapolit_tabl_kpi(self, spis)


def zapolit_tabl_kpi(self, spis):
    edit = {F.nom_kol_po_im_v_shap(spis,'Факт. вып.')}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_kpi_sotr, 0, edit, (), (), 200, True, '')
    self.ui.tableWidget_kpi_sotr.setColumnWidth(1, 350)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(0, 200)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(7, 150)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(8, 300)
    self.ui.tableWidget_kpi_sotr.horizontalHeader().setStretchLastSection(True)
    F.cvet_cell_wtabl(self.ui.tableWidget_kpi_sotr,'Факт. вып.','','',inventir=True)


def save_sotr(self):
    if proverka_dannih(self) == False:
        return

    pass

def proverka_dannih(self):
    spis = F.spisok_iz_wtabl(self.ui.tableWidget_kpi_sotr,'',True)
    kol = F.nom_kol_po_im_v_shap(spis,'Факт. вып.')
    kol_vid = self.shapka_shablonkpi[0].index('Тип КПЭ')
    kol_pred1 = self.shapka_shablonkpi[0].index("Уров.вып.№1")
    kol_pred2 = self.shapka_shablonkpi[0].index("Уров.вып.№3")
    spis[1][kol] = "-"
    if len(spis) < 3:
        self.showdialog(f'Таблица не может быть не заполнена')
        return False
    for i in range(2,len(spis)):
        if spis[i][kol_vid] != self.KPITIPS[0]:
            if spis[i][kol] != '':
                spis[i][kol] = "1"
            else:
                spis[i][kol] = "0"
        if spis[i][kol] == "":
            self.showdialog(f'Факт. вып., строка {i} не заполнена')
            return False
        if F.is_numeric(spis[i][kol]) == False:
            self.showdialog(f'Факт. вып., строка {i} не число')
            return False
        if spis[i][kol_vid] == self.KPITIPS[0]:
            if int(spis[i][kol]) > int(spis[i][kol_pred2]) or int(spis[i][kol]) < int(spis[i][kol_pred1]):
                self.showdialog(f'Факт. вып., строка {i} не в пределах уров.вып.')
                return False
