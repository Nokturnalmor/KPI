import Cust_Functions as F
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QStyle

def log_in(self):
    flag_log_in = False
    if self.windowTitle() != "Расчет КПЭ":
        self.showdialog(f'Необходимо предварительно выйти {self.windowTitle()}')
        return
    if self.ui.lineEdit_parol.text() == "":
        return
    if admin(self):
        flag_log_in = True
    if not flag_log_in:
        rez_challenge = True#check_pass(self.ui.comboBox_empl.currentText(), self.ui.lineEdit_parol.text())
        if rez_challenge is False:
            # F.msgbox('Не верный пароль')
            self.showdialog('Не верный пароль')
            self.ui.lineEdit_parol.setText('')
            return
        elif rez_challenge is None:
            F.msgbox('Не зарегистрирован')
            return
        flag_log_in = True
    if flag_log_in:
        self.setWindowTitle(self.ui.comboBox_empl.currentText())
        self.ui.lineEdit_parol.setText('')
        self.spis_dolg_filtr = []
        #load_all(self)


def load_all(self):
    load_strukt(self)
    load_filtr(self)
    self.load_combo()
    load_combo_sotr(self)

def load_combo_sotr(self,ind = 0):
    self.ui.comboBox_rabotn.clear()
    spis_tmp = F.otkr_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'strukt.pickle', pickl=True)
    spis_filtr = F.otkr_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle', pickl=True)
    spis = []
    for i in range(len(spis_tmp)):
        spis.append(spis_tmp[i][2])
    spis = set(spis)
    filtr = []
    for i in range(1,len(spis_filtr)):
        filtr.append(spis_filtr[i][0])
    filtr = set(filtr)
    shet = 0
    name = self.ui.label_period.text()
    for i in range(len(self.spis_emploe)):
        if ' '.join(self.spis_emploe[i][3:]) in spis and ' '.join(self.spis_emploe[i]) not in filtr:
            ima = ' '.join(self.spis_emploe[i])
            self.ui.comboBox_rabotn.addItem(ima)
            if F.nalich_file(F.scfg(
                    'strukt') + F.sep() + self.windowTitle() + F.sep() + name + F.sep() + name + "$" + ima + '.pickle') == True:
                self.ui.comboBox_rabotn.setItemIcon(shet, QApplication.style().standardIcon(QStyle.SP_DialogYesButton))
            else:
                self.ui.comboBox_rabotn.setItemIcon(shet, QApplication.style().standardIcon(QStyle.SP_DialogNoButton))
            shet+=1
    self.ui.comboBox_rabotn.setCurrentIndex(ind)


def save_strukt(self):
    if self.ui.tableWidget_struktura.item(0, 0).text() == "":
        self.showdialog('Не введен отдел')
        return
    otdel = self.ui.tableWidget_struktura.item(0, 0).text()
    if self.ui.tableWidget_struktura.item(0, 1).text() == "":
        self.showdialog('Не выбран руководитель')
        return
    if self.ui.tableWidget_struktura.item(0, 2).text() == "":
        self.showdialog('Не выбрана должность работника')
        return

    tmp_spis = F.spisok_iz_wtabl(self.ui.tableWidget_struktura, '', True)
    spis = [tmp_spis[0]]
    for i in range(1, len(tmp_spis)):
        if tmp_spis[i][0] == '' and tmp_spis[i][1] == '' and tmp_spis[i][2] == '':
            pass
        else:
            spis.append(tmp_spis[i])
    F.zap_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'strukt.pickle', spis, pickl=True)
    spis_filtr = F.spisok_iz_wtabl(self.ui.tableWidget_filtr,'',False)
    spis_filtr.pop()
    spis_filtr_tmp = set()
    for i in spis_filtr:
        spis_filtr_tmp.add(i[0])
    spis_filtr_tmp.discard('')
    spis_filtr_tmp = list(spis_filtr_tmp)
    spis_filtr_tmp.sort()
    spis_filtr = []
    for i in spis_filtr_tmp:
        spis_filtr.append([i])
    spis_filtr.insert(0,["Сотрудники"])
    F.zap_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle', spis_filtr, pickl=True)

    self.showdialog(f'Структура отдела {otdel} успешно сохранена')


def load_filtr(self):
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep()):
        F.sozd_dir(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep())
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle'):
        spis = [["Сотрудники"]]
        F.zap_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle', spis, pickl=True)
    spis = F.otkr_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle', pickl=True)
    spis.append([''])
    zapoln_filtr(self, spis)


def zapoln_filtr(self, spis):
    edit = {}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_filtr, 0, edit, (), (), 200, True, '')
    #self.ui.tableWidget_filtr.setColumnWidth(0, 400)
    spis_tmp = F.otkr_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'filtr.pickle', pickl=True)
    spis_tmp_tek = F.spisok_iz_wtabl(self.ui.tableWidget_struktura)
    spis_tmp_tek2 = []
    for i in range(len(spis_tmp_tek)-1):
        spis_tmp_tek2.append(spis_tmp_tek[i][2])

    spis_tmp2 = []
    for i in range(len(self.spis_emploe)) :
        if ' '.join(self.spis_emploe[i][3:]) in spis_tmp_tek2:
            spis_tmp2.append(' '.join(self.spis_emploe[i]))

    spis_filtr = set()
    for i in range(1,len(spis_tmp)):
        spis_filtr.add(spis_tmp[i][0])
    for i in range(len(spis_tmp2)):
        spis_filtr.add(spis_tmp2[i])
    spis_filtr = list(spis_filtr)
    spis_filtr.sort()

    for i in range(self.ui.tableWidget_filtr.rowCount()):
        combo = QtWidgets.QComboBox()
        combo.addItem("")
        for item in spis_filtr:
            combo.addItem(item)
            if self.ui.tableWidget_filtr.item(i, 0).text() == item:
                combo.setCurrentText(item)
        combo.currentIndexChanged.connect((lambda: onStateChanged2(self)))
        self.ui.tableWidget_filtr.setCellWidget(i, 0, combo)

def onStateChanged2(self):
    ch = self.sender()
    ix = self.ui.tableWidget_filtr.indexAt(ch.pos())
    print(ix.row(), ix.column(), ch.currentText())
    self.ui.tableWidget_filtr.item(ix.row(), ix.column()).setText(ch.currentText())
    if self.ui.tableWidget_filtr.rowCount() - 1 == ix.row() and ch.currentText() != '':
        spis = F.spisok_iz_wtabl(self.ui.tableWidget_filtr, '', True)
        spis.append([""])
        zapoln_filtr(self, spis)


def load_strukt(self):
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep()):
        F.sozd_dir(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep())
    if not F.nalich_file(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'strukt.pickle'):
        shapka = [['Отдел', 'Руководитель', 'Должности']]
        F.zap_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'strukt.pickle', shapka, pickl=True)
    spis = F.otkr_f(F.scfg('strukt') + F.sep() + self.windowTitle() + F.sep() + 'strukt.pickle', pickl=True)
    spis.append(['', '', ''])
    zapoln_red_tab(self, spis)

    return


def zapoln_red_tab(self, spis):
    edit = {0, 1, 2}
    F.zapoln_wtabl(self, spis, self.ui.tableWidget_struktura, 0, edit, (), (), 200, True, '')
    self.ui.tableWidget_struktura.setColumnWidth(1, 400)
    self.spis_dolg_filtr = []
    for i in range(self.ui.tableWidget_struktura.rowCount()):
        combo = QtWidgets.QComboBox()
        combo.addItem("")
        for item in self.spis_str_emploee:
            combo.addItem(item)
            if self.ui.tableWidget_struktura.item(i, 1).text() == item:
                combo.setCurrentText(item)
        combo.currentIndexChanged.connect((lambda: onStateChanged1(self)))

        combo2 = QtWidgets.QComboBox()
        combo2.addItem("")
        for item in self.spis_dolg:
            combo2.addItem(item)
            if self.ui.tableWidget_struktura.item(i, 2).text() == item:
                combo2.setCurrentText(item)
                self.spis_dolg_filtr.append(item)
        combo2.currentIndexChanged.connect((lambda: onStateChanged(self)))
        if i == 0:
            self.ui.tableWidget_struktura.setCellWidget(i, 1, combo)
        self.ui.tableWidget_struktura.setCellWidget(i, 2, combo2)
    for i in range(1,self.ui.tableWidget_struktura.rowCount()):
        F.ust_color_wtab(self.ui.tableWidget_struktura, i, 0, 220, 220, 220)
        F.ust_color_wtab(self.ui.tableWidget_struktura, i, 1, 220, 220, 220)

def onStateChanged1(self):
    ch = self.sender()
    ix = self.ui.tableWidget_struktura.indexAt(ch.pos())
    print(ix.row(), ix.column(), ch.currentText())
    self.ui.tableWidget_struktura.item(ix.row(), ix.column()).setText(ch.currentText())


def onStateChanged(self):
    ch = self.sender()
    ix = self.ui.tableWidget_struktura.indexAt(ch.pos())
    print(ix.row(), ix.column(), ch.currentText())
    self.ui.tableWidget_struktura.item(ix.row(), ix.column()).setText(ch.currentText())
    if self.ui.tableWidget_struktura.rowCount() - 1 == ix.row() and ch.currentText() != '':
        spis = F.spisok_iz_wtabl(self.ui.tableWidget_struktura, '', True)
        spis.append(["", "", ""])
        zapoln_red_tab(self, spis)
        load_filtr(self)


def new_user(self):
    spis_parol = F.otkr_f(F.tcfg('Riba'), False, '|')
    fio = self.ui.comboBox_empl.currentText()
    for i in range(len(spis_parol)):
        if F.shifr(fio.strip()) == spis_parol[i][0]:
            F.msgbox(f'{self.ui.comboBox_empl.currentText()} уже зарегистрирован')
            return
    spis_parol.append([F.shifr(fio.strip()), F.shifr(F.date(vid='yyyy'))])
    F.zap_f(F.tcfg('Riba'), spis_parol, '|')
    F.msgbox(f'{self.ui.comboBox_empl.currentText()} успешно зарегистрирован {F.shifr(fio.strip())}')


def smena_parol(self):
    if self.windowTitle() == "Расчет КПЭ":
        return
    self.ui.lineEdit_3_nParol.setVisible(True)
    self.ui.lineEdit_3_nParol_2.setVisible(True)
    self.ui.pushButton_logout.setText("Сменить и выйти")
    self.regim_new_parol = True


def log_out(self):
    if self.regim_new_parol:
        rez_challenge = check_pass(self.windowTitle(), self.ui.lineEdit_parol.text())
        if not rez_challenge:
            self.showdialog(f'Не верный пароль')
            return
        if self.ui.lineEdit_3_nParol.text() != self.ui.lineEdit_3_nParol_2.text():
            self.showdialog(f'Пароли не совпадают')
            return
        if self.ui.lineEdit_3_nParol.text() == "":
            self.showdialog(f'пароль не может быть пустым')
            return

        spis_parol = F.otkr_f(F.tcfg('Riba'), False, '|')

        for i in range(len(spis_parol)):
            if F.shifr(self.windowTitle().strip()) == spis_parol[i][0]:
                spis_parol[i][1] = F.shifr(self.ui.lineEdit_3_nParol.text().strip())
        F.zap_f(F.tcfg('Riba'), spis_parol, '|')
        F.msgbox(f'{self.windowTitle()} пароль успешно изменен {F.shifr(self.ui.lineEdit_3_nParol.text().strip())}')
        self.ui.lineEdit_parol.setText('')
        self.ui.lineEdit_3_nParol.setText('')
        self.ui.lineEdit_3_nParol_2.clear()
        self.ui.lineEdit_3_nParol.setVisible(False)
        self.ui.lineEdit_3_nParol_2.setVisible(False)
        self.ui.pushButton_logout.setText("Выход")
        self.regim_new_parol = False
        self.setWindowTitle("Расчет КПЭ")
        unload(self)
    else:
        self.setWindowTitle("Расчет КПЭ")
        unload(self)


def admin(self):
    if self.ui.lineEdit_parol.text() == "Hyilolo74587458" and 'Беляков Антон' in self.ui.comboBox_empl.currentText():
        return True
    return False


def check_pass(fio, parol):
    spis_parol = F.otkr_f(F.tcfg('Riba'), False, '|')
    flag_naid = None
    for i in range(len(spis_parol)):
        if F.shifr(fio.strip()) == spis_parol[i][0]:
            flag_naid = False
            if F.shifr(parol.strip()) == spis_parol[i][1]:
                flag_naid = True
                return flag_naid
            else:
                return flag_naid
    return flag_naid


def unload(self):
    self.ui.tableWidget_struktura.clear()
    self.ui.comboBox_dolgn_red.clear()
    self.ui.tableWidget_red_kpi.clear()
    self.ui.tableWidget_kpi_sotr.clear()
    self.ui.comboBox_rabotn.clear()
