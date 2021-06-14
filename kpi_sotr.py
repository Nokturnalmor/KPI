import Cust_Functions as F
import autorization as aut
#import comtypes.client
from docxtpl import DocxTemplate
import os

def set_rabotn(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    if self.ui.cmb_rabotn.currentText() == "":
        return
    dolgn = ' '.join(self.ui.cmb_rabotn.currentText().split(' ')[3:])
    name = self.ui.l_period.text()
    if F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$"
                     + self.ui.cmb_rabotn.currentText() + '.pickle'):
        spis = F.otkr_f(
            F.scfg(
                'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" +
            self.ui.cmb_rabotn.currentText() + '.pickle',
            pickl=True)
    else:
        if not F.nalich_file(F.scfg(
                'strukt') + F.sep() + self.windowTitle() + F.sep() + dolgn + '.pickle'):
            self.showdialog(f'Не найден шаблон {dolgn}')
            self.ui.tbl_kpi_sotr.clear()
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
    F.zapoln_wtabl(self, spis, self.ui.tbl_kpi_sotr, 0, edit, (), (), 200, True, '')
    self.ui.tbl_kpi_sotr.setColumnWidth(1, 350)
    self.ui.tbl_kpi_sotr.setColumnWidth(0, 200)
    self.ui.tbl_kpi_sotr.setColumnWidth(7, 150)
    self.ui.tbl_kpi_sotr.setColumnWidth(9, 100)
    self.ui.tbl_kpi_sotr.horizontalHeader().setStretchLastSection(True)
    F.cvet_cell_wtabl(self.ui.tbl_kpi_sotr, 'Факт. вып.', '*', '', inventir=True)
    F.dob_color_wtab(self.ui.tbl_kpi_sotr, 0, F.nom_kol_po_im_v_shap(spis, 'Факт. вып.'), 20, 20, 20)
    for i in range(0, self.ui.tbl_kpi_sotr.columnCount()):
        F.dob_color_wtab(self.ui.tbl_kpi_sotr, 0, i, 30, 30, 30)

    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Цель'), 12)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Наименование КПЭ'), 10)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Методика расчета'), 10)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Примечание'), 10)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Уров.вып.№1'), 18)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Уров.вып.№2'), 18)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Уров.вып.№3'), 18)
    F.font_size(self.ui.tbl_kpi_sotr, F.nom_kol_po_im_v_shap(spis, 'Факт. вып.'), 20)
    self.ui.tbl_kpi_sotr.resizeRowsToContents()


def save_sotr(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    if not proverka_dannih(self):
        return
    spis = F.spisok_iz_wtabl(self.ui.tbl_kpi_sotr, '', True)
    name = self.ui.l_period.text()
    if not F.nalich_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name):
        F.sozd_dir(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name)
    F.zap_f(F.scfg(
        'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" +
            self.ui.cmb_rabotn.currentText() + '.pickle',
            spis, pickl=True)
    self.showdialog(
        f'КПЭ на {self.ui.cmb_rabotn.currentText()} успешно сохранен')
    aut.load_combo_sotr(self, self.ui.cmb_rabotn.currentIndex())


def proverka_dannih(self, spis=()):
    if spis == ():
        spis = F.spisok_iz_wtabl(self.ui.tbl_kpi_sotr, '', True)
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
            F.migat(self, self.ui.tbl_kpi_sotr, i - 1, kol)
            return False
        if spis[i][kol_vid] == self.KPITIPS[0] and not F.is_numeric(spis[i][kol]):
            self.showdialog(f'Факт. вып., строка {i} не число')
            F.migat(self, self.ui.tbl_kpi_sotr, i - 1, kol)
            return False

        if spis[i][kol_vid] == self.KPITIPS[0]:
            if int(spis[i][kol_pred2]) > int(spis[i][kol_pred1]):
                if int(spis[i][kol]) < int(spis[i][kol_pred1]) or int(spis[i][kol]) > int(spis[i][kol_pred2]):
                    self.showdialog(f'Факт. вып., строка {i} не в пределах уров.вып.')
                    F.migat(self, self.ui.tbl_kpi_sotr, i - 1, kol)
                    return False
            if int(spis[i][kol_pred2]) < int(spis[i][kol_pred1]):
                if int(spis[i][kol]) > int(spis[i][kol_pred1]) or int(spis[i][kol]) < int(spis[i][kol_pred2]):
                    self.showdialog(f'Факт. вып., строка {i} не в пределах уров.вып.')
                    F.migat(self, self.ui.tbl_kpi_sotr, i - 1, kol)
                    return False
        if int(spis[i][kol]) < 0:
            self.showdialog(f'Факт. вып., строка {i} не может быть меньше 0')
            F.migat(self, self.ui.tbl_kpi_sotr, i - 1, kol)
            return False
    return spis


def rasschet_sotr(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    if not proverka_dannih(self):
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
    flag_otsek = False
    for i in range(2, len(spis)):
        if spis[i][kol_tip] == self.KPITIPS[0]:
            summ += rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3) * int(spis[i][kol_ves]) / 100
            spis[i][kol_podit] = str(
                round(rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3) * int(spis[i][kol_ves]) / 100, 1))
        if spis[i][kol_tip] == self.KPITIPS[1]:
            summ -= int(spis[i][kol_fact]) * int(spis[i][kol_ves])
            spis[i][kol_podit] = str(int(spis[i][kol_fact]) * int(spis[i][kol_ves]) * -1)
        if spis[i][kol_tip] == self.KPITIPS[2]:
            if spis[i][kol_fact] == '1':
                spis[i][kol_podit] = '*0'
                # summ -= summ * int(spis[i][kol_fact])
                flag_otsek = True
            else:
                spis[i][kol_podit] = '0'
    if flag_otsek:
        summ = 0
    self.ui.l_raschet.setText(f"Итого: {str(round(summ, 1))}")
    zapolit_tabl_kpi(self, spis)


def rassch_nepr(spis, i, kol_fact, kol_z1, kol_z2, kol_z3):
    fact = int(spis[i][kol_fact])
    z1 = int(spis[i][kol_z1])
    z2 = int(spis[i][kol_z2])
    z3 = int(spis[i][kol_z3])
    y1 = int(spis[1][kol_z1])
    y2 = int(spis[1][kol_z2])
    y3 = int(spis[1][kol_z3])
    if z3 > z1:
        if fact < z2:
            proc = (fact - z1) / (z2 - z1)
            return (y2 - y1) * proc + y1
        else:
            proc = (fact - z2) / (z3 - z2)
            return (y3 - y2) * proc + y2
    else:
        if fact > z2:
            proc = (z1 - fact) / (z1 - z2)
            return (y2 - y1) * proc + y1
        else:
            proc = (z2 - fact) / (z2 - z3)
            return (y3 - y2) * proc + y2


# no 4194304
def del_kpi_sotr(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    rez = self.showdialogYN(f'Будет удален КПЭ для {self.ui.cmb_rabotn.currentText()} на {self.ui.l_period.text()}')
    if rez == 1024:
        name = self.ui.l_period.text()
        F.udal_file(F.scfg(
            'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" +
                    self.ui.cmb_rabotn.currentText() + '.pickle')
        set_rabotn(self)
        self.showdialog(f'КПЭ для {self.ui.cmb_rabotn.currentText()} успешно удален.\n'
                        f'его не вернуть.\n'
                        f'никак.')
        aut.load_combo_sotr(self, self.ui.cmb_rabotn.currentIndex())

def export(self):
    if F.nalich_file(os.path.join("icons", "шаблон.docx")) == False:
        self.showdialog("шаблон не найден")
        return
    if self.ui.l_raschet.text() == "":
        rasschet_sotr(self)
    msg = ""
    sch= 0
    spis = F.spisok_iz_wtabl(self.ui.tbl_kpi_sotr, '', True)
    kol_cel = F.nom_kol_po_im_v_shap(spis,"Цель")
    kol_naim = F.nom_kol_po_im_v_shap(spis, "Наименование КПЭ")
    kol_ed = F.nom_kol_po_im_v_shap(spis, "Ед. изм.")
    kol_fact = F.nom_kol_po_im_v_shap(spis, 'Факт. вып.')
    i = 0
    msg += f'{vpisat("№",3)}|{vpisat(spis[i][kol_cel],25)}|{vpisat(spis[i][kol_naim],45)}|{vpisat(spis[i][kol_ed],15)}|{vpisat(spis[i][kol_fact],10)}\n'
    msg += f'{vpisat("-", 3,znac= "-")}|{vpisat("-", 25,znac= "-")}|' \
           f'{vpisat("-", 45,znac= "-")}|{vpisat("-", 15,znac= "-")}|' \
           f'{vpisat("-", 10,znac= "-")}\n'

    for i in range(2, len(spis)):
        sch +=1
        msg += f'{vpisat(str(sch)+".",3)}|{vpisat(spis[i][kol_cel],25)}|{vpisat(spis[i][kol_naim],45)}|{vpisat(spis[i][kol_ed],15)}|{vpisat(spis[i][kol_fact],10)}\n'

    doc = DocxTemplate(os.path.join("icons", "шаблон.docx"))
    context = {'emploe': self.ui.cmb_rabotn.currentText(), 'period': self.ui.l_period.text(), 'kpi': msg,
               'itog': self.ui.l_raschet.text(), 'now': F.now()}


    doc.render(context)
    if F.nalich_file(F.put_po_umolch() + os.sep + 'КПЭ' + os.sep) == False:
        F.sozd_dir(F.put_po_umolch() + os.sep + 'КПЭ' + os.sep)
    putf = f'{F.put_po_umolch()}{os.sep}КПЭ{os.sep}{self.fio(self.ui.cmb_rabotn.currentText())}${self.ui.l_period.text()}.docx'
    doc.save(putf)
    F.zapyst_file(putf)
    return
    #wdFormatPDF = 17
    #
    #in_file = os.path.abspath("final.docx")
    #out_file = os.path.abspath("final.pdf")
    #
    #word = comtypes.client.CreateObject('Word.Application')
    #doc = word.Documents.Open(in_file)
    #doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    #doc.Close()
    #word.Quit()

def vpisat(text,dl,orient=0,znac = " "):
    text = str(text)
    text = text.strip().replace('\n','')
    text = text[:dl]

    if orient == 1:
        if (dl - len(text))%2 > 0:
            itog = f'{znac*(((dl - len(text))//2)+1)}{text}{znac*((dl - len(text))//2)}'
        else:
            itog = f'{znac * (((dl - len(text)) / 2) + 1)}{text}{znac * ((dl - len(text)) / 2)}'
    if orient == 0:
        itog = f'{text}{znac * (dl - len(text))}'
    if orient == 2:
        itog = f'{znac * (dl - len(text))}{text}'
    return itog