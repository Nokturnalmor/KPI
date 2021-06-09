import Cust_Functions as F


def set_rabotn(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    dolgn = ' '.join(self.ui.comboBox_rabotn.currentText().split(' ')[3:])
    name = self.ui.label_period.text()
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" + self.ui.comboBox_rabotn.currentText() + '.pickle') == True:
        spis = F.otkr_f(
            F.scfg(
                'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" + self.ui.comboBox_rabotn.currentText() + '.pickle',
            pickl=True)
    else:
        if F.nalich_file(F.scfg(
                'strukt') + F.sep() + self.windowTitle() + F.sep() + dolgn + '.pickle') == False:
            self.showdialog(f'Не найден шаблон {dolgn}')
            return
        spis = F.otkr_f(
            F.scfg(
                'strukt') + F.sep() + self.windowTitle() + F.sep() + dolgn + '.pickle',
            pickl=True)
        vstav_pol = 8
        spis[0].insert(vstav_pol, 'Факт. вып.')
        spis[1].insert(vstav_pol, '-')
        for i in range(2, len(spis)):
            spis[i].insert(vstav_pol, '')
        vstav_pol = 9
        spis[0].insert(vstav_pol, 'Подытог,%')
        spis[1].insert(vstav_pol, '-')
        for i in range(2, len(spis)):
            spis[i].insert(vstav_pol, '')
    zapolit_tabl_kpi(self, spis)


def zapolit_tabl_kpi(self, spis):
    edit = {F.nom_kol_po_im_v_shap(spis, 'Факт. вып.')}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_kpi_sotr, 0, edit, (), (), 200, True, '')
    self.ui.tableWidget_kpi_sotr.setColumnWidth(1, 350)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(0, 200)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(7, 150)
    self.ui.tableWidget_kpi_sotr.setColumnWidth(9, 100)
    self.ui.tableWidget_kpi_sotr.horizontalHeader().setStretchLastSection(True)
    F.cvet_cell_wtabl(self.ui.tableWidget_kpi_sotr, 'Факт. вып.', '*', '', inventir=True)
    F.ust_color_wtab(self.ui.tableWidget_kpi_sotr, 0, F.nom_kol_po_im_v_shap(spis,'Факт. вып.'), 220, 220, 220)


def save_sotr(self):
    if proverka_dannih(self) == False:
        return
    spis = F.spisok_iz_wtabl(self.ui.tableWidget_kpi_sotr, '', True)
    name = self.ui.label_period.text()
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name) == False:
        F.sozd_dir(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name)
    F.zap_f(F.scfg(
        'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" + self.ui.comboBox_rabotn.currentText() + '.pickle',
            spis, pickl=True)
    self.showdialog(
        f'КПЭ на {self.ui.comboBox_rabotn.currentText()} успешно сохранен')
    pass


def proverka_dannih(self):
    spis = F.spisok_iz_wtabl(self.ui.tableWidget_kpi_sotr, '', True)
    kol = F.nom_kol_po_im_v_shap(spis, 'Факт. вып.')
    kol_vid = self.shapka_shablonkpi[0].index('Тип КПЭ')
    kol_pred1 = self.shapka_shablonkpi[0].index("Уров.вып.№1")
    kol_pred2 = self.shapka_shablonkpi[0].index("Уров.вып.№3")
    spis[1][kol] = "-"
    if len(spis) < 3:
        self.showdialog(f'Таблица не может быть не заполнена')
        return False
    for i in range(2, len(spis)):
        if spis[i][kol_vid] != self.KPITIPS[0]:
            if spis[i][kol] != '' and spis[i][kol] != '0':
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
        if int(spis[i][kol]) < 0:
            self.showdialog(f'Факт. вып., строка {i} не может быть меньше 0')
            return False
    return spis


def rasschet_sotr(self):
    if proverka_dannih(self) == False:
        return
    spis = proverka_dannih(self)
    summ = 0
    kol_fact = F.nom_kol_po_im_v_shap(spis, 'Факт. вып.')
    kol_tip = F.nom_kol_po_im_v_shap(spis, "Тип КПЭ")
    kol_z1 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№1")
    kol_z2 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№2")
    kol_z3 = F.nom_kol_po_im_v_shap(spis, "Уров.вып.№3")
    kol_ves = F.nom_kol_po_im_v_shap(spis, "Вес КПЭ")
    kol_podit = F.nom_kol_po_im_v_shap(spis, "Подытог,%")
    for i in range(2, len(spis)):
        if spis[i][kol_tip] == self.KPITIPS[0]:
            summ += rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3) * int(spis[i][kol_ves]) / 100
            spis[i][kol_podit] = str(
                round(rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3) * int(spis[i][kol_ves]) / 100, 1))
        if spis[i][kol_tip] == self.KPITIPS[1]:
            summ -= int(spis[i][kol_fact]) * int(spis[i][kol_ves])
            spis[i][kol_podit] = str(int(spis[i][kol_fact]) * int(spis[i][kol_ves]))
        if spis[i][kol_tip] == self.KPITIPS[2]:
            summ -= summ * int(spis[i][kol_fact])
            spis[i][kol_podit] = str(int(spis[i][kol_fact]))
    self.ui.label_raschet.setText(f"Итог:{str(round(summ, 1))}")
    zapolit_tabl_kpi(self, spis)


def rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3):
    fact = int(spis[i][kol_fact])
    z1 = int(spis[i][kol_z1])
    z2 = int(spis[i][kol_z2])
    z3 = int(spis[i][kol_z3])
    y1 = int(spis[1][kol_z1])
    y2 = int(spis[1][kol_z2])
    y3 = int(spis[1][kol_z3])
    if fact < z1:
        return 0
    if fact < z2:
        proc = (fact - z1) / (z2 - z1)
        return (y2 - y1) * proc + y1
    else:
        proc = (fact - z2) / (z3 - z2)
        return (y3 - y2) * proc + y2
