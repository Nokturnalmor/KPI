# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\Python\GUI\mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cmb_empl = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_empl.sizePolicy().hasHeightForWidth())
        self.cmb_empl.setSizePolicy(sizePolicy)
        self.cmb_empl.setMinimumSize(QtCore.QSize(0, 44))
        self.cmb_empl.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cmb_empl.setFont(font)
        self.cmb_empl.setAutoFillBackground(True)
        self.cmb_empl.setObjectName("cmb_empl")
        self.verticalLayout.addWidget(self.cmb_empl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 44))
        self.btn_login.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.le_parol = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_parol.sizePolicy().hasHeightForWidth())
        self.le_parol.setSizePolicy(sizePolicy)
        self.le_parol.setMinimumSize(QtCore.QSize(0, 44))
        self.le_parol.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.le_parol.setFont(font)
        self.le_parol.setStatusTip("")
        self.le_parol.setWhatsThis("")
        self.le_parol.setInputMask("")
        self.le_parol.setText("")
        self.le_parol.setMaxLength(22)
        self.le_parol.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_parol.setObjectName("le_parol")
        self.horizontalLayout.addWidget(self.le_parol)
        self.le_3_nParol = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_3_nParol.sizePolicy().hasHeightForWidth())
        self.le_3_nParol.setSizePolicy(sizePolicy)
        self.le_3_nParol.setMinimumSize(QtCore.QSize(0, 44))
        self.le_3_nParol.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.le_3_nParol.setFont(font)
        self.le_3_nParol.setStatusTip("")
        self.le_3_nParol.setWhatsThis("")
        self.le_3_nParol.setInputMask("")
        self.le_3_nParol.setText("")
        self.le_3_nParol.setMaxLength(22)
        self.le_3_nParol.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_3_nParol.setObjectName("le_3_nParol")
        self.horizontalLayout.addWidget(self.le_3_nParol)
        self.le_3_nParol_2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_3_nParol_2.sizePolicy().hasHeightForWidth())
        self.le_3_nParol_2.setSizePolicy(sizePolicy)
        self.le_3_nParol_2.setMinimumSize(QtCore.QSize(0, 44))
        self.le_3_nParol_2.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.le_3_nParol_2.setFont(font)
        self.le_3_nParol_2.setStatusTip("")
        self.le_3_nParol_2.setWhatsThis("")
        self.le_3_nParol_2.setInputMask("")
        self.le_3_nParol_2.setText("")
        self.le_3_nParol_2.setMaxLength(22)
        self.le_3_nParol_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_3_nParol_2.setObjectName("le_3_nParol_2")
        self.horizontalLayout.addWidget(self.le_3_nParol_2)
        self.btn_logout = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(122, 44))
        self.btn_logout.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout.addWidget(self.btn_logout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.l_period = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_period.setFont(font)
        self.l_period.setFrameShape(QtWidgets.QFrame.Panel)
        self.l_period.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_period.setAlignment(QtCore.Qt.AlignCenter)
        self.l_period.setObjectName("l_period")
        self.verticalLayout_5.addWidget(self.l_period)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_img = QtWidgets.QLabel(self.tab_4)
        self.l_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_img.setText("")
        self.l_img.setAlignment(QtCore.Qt.AlignCenter)
        self.l_img.setObjectName("l_img")
        self.horizontalLayout_4.addWidget(self.l_img)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.clnd = QtWidgets.QCalendarWidget(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clnd.setFont(font)
        self.clnd.setMinimumDate(QtCore.QDate(2020, 1, 14))
        self.clnd.setGridVisible(True)
        self.clnd.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.LongDayNames)
        self.clnd.setNavigationBarVisible(True)
        self.clnd.setDateEditEnabled(True)
        self.clnd.setObjectName("clnd")
        self.verticalLayout_4.addWidget(self.clnd)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l = QtWidgets.QLabel(self.groupBox_2)
        self.l.setObjectName("l")
        self.horizontalLayout_2.addWidget(self.l)
        self.l_kpi_otd = QtWidgets.QLabel(self.groupBox_2)
        self.l_kpi_otd.setObjectName("l_kpi_otd")
        self.horizontalLayout_2.addWidget(self.l_kpi_otd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.l_3 = QtWidgets.QLabel(self.groupBox_2)
        self.l_3.setObjectName("l_3")
        self.horizontalLayout_3.addWidget(self.l_3)
        self.l_kpi_pr = QtWidgets.QLabel(self.groupBox_2)
        self.l_kpi_pr.setObjectName("l_kpi_pr")
        self.horizontalLayout_3.addWidget(self.l_kpi_pr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cmb_rabotn = QtWidgets.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cmb_rabotn.setFont(font)
        self.cmb_rabotn.setObjectName("cmb_rabotn")
        self.verticalLayout_10.addWidget(self.cmb_rabotn)
        self.tbl_kpi_sotr = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbl_kpi_sotr.setFont(font)
        self.tbl_kpi_sotr.setObjectName("tbl_kpi_sotr")
        self.tbl_kpi_sotr.setColumnCount(0)
        self.tbl_kpi_sotr.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tbl_kpi_sotr)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_save_sotr = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_sotr.sizePolicy().hasHeightForWidth())
        self.btn_save_sotr.setSizePolicy(sizePolicy)
        self.btn_save_sotr.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_save_sotr.setFont(font)
        self.btn_save_sotr.setText("")
        self.btn_save_sotr.setIconSize(QtCore.QSize(32, 32))
        self.btn_save_sotr.setObjectName("btn_save_sotr")
        self.horizontalLayout_7.addWidget(self.btn_save_sotr)
        self.btn_rasschet = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rasschet.sizePolicy().hasHeightForWidth())
        self.btn_rasschet.setSizePolicy(sizePolicy)
        self.btn_rasschet.setMinimumSize(QtCore.QSize(0, 51))
        self.btn_rasschet.setMaximumSize(QtCore.QSize(2222, 55))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.btn_rasschet.setFont(font)
        self.btn_rasschet.setText("")
        self.btn_rasschet.setIconSize(QtCore.QSize(32, 32))
        self.btn_rasschet.setObjectName("btn_rasschet")
        self.horizontalLayout_7.addWidget(self.btn_rasschet)
        self.l_raschet = QtWidgets.QLabel(self.tab)
        self.l_raschet.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_raschet.setFont(font)
        self.l_raschet.setFrameShape(QtWidgets.QFrame.Panel)
        self.l_raschet.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l_raschet.setLineWidth(1)
        self.l_raschet.setMidLineWidth(1)
        self.l_raschet.setText("")
        self.l_raschet.setObjectName("l_raschet")
        self.horizontalLayout_7.addWidget(self.l_raschet)
        self.btn_del_kpi_sotr = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del_kpi_sotr.sizePolicy().hasHeightForWidth())
        self.btn_del_kpi_sotr.setSizePolicy(sizePolicy)
        self.btn_del_kpi_sotr.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_del_kpi_sotr.setFont(font)
        self.btn_del_kpi_sotr.setText("")
        self.btn_del_kpi_sotr.setIconSize(QtCore.QSize(32, 32))
        self.btn_del_kpi_sotr.setObjectName("btn_del_kpi_sotr")
        self.horizontalLayout_7.addWidget(self.btn_del_kpi_sotr)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.l_tek_otd = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_tek_otd.setFont(font)
        self.l_tek_otd.setFrameShape(QtWidgets.QFrame.Panel)
        self.l_tek_otd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_tek_otd.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tek_otd.setObjectName("l_tek_otd")
        self.verticalLayout_7.addWidget(self.l_tek_otd)
        self.tbl_kpi_vnesh = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbl_kpi_vnesh.setFont(font)
        self.tbl_kpi_vnesh.setObjectName("tbl_kpi_vnesh")
        self.tbl_kpi_vnesh.setColumnCount(0)
        self.tbl_kpi_vnesh.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tbl_kpi_vnesh)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_save_vn = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_vn.sizePolicy().hasHeightForWidth())
        self.btn_save_vn.setSizePolicy(sizePolicy)
        self.btn_save_vn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_save_vn.setFont(font)
        self.btn_save_vn.setStatusTip("")
        self.btn_save_vn.setText("")
        self.btn_save_vn.setIconSize(QtCore.QSize(32, 32))
        self.btn_save_vn.setObjectName("btn_save_vn")
        self.horizontalLayout_6.addWidget(self.btn_save_vn)
        self.btn_load_vn = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_vn.sizePolicy().hasHeightForWidth())
        self.btn_load_vn.setSizePolicy(sizePolicy)
        self.btn_load_vn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_load_vn.setFont(font)
        self.btn_load_vn.setStatusTip("")
        self.btn_load_vn.setText("")
        self.btn_load_vn.setIconSize(QtCore.QSize(32, 32))
        self.btn_load_vn.setObjectName("btn_load_vn")
        self.horizontalLayout_6.addWidget(self.btn_load_vn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cmb_dolgn_red = QtWidgets.QComboBox(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cmb_dolgn_red.setFont(font)
        self.cmb_dolgn_red.setObjectName("cmb_dolgn_red")
        self.verticalLayout_6.addWidget(self.cmb_dolgn_red)
        self.tbl_red_kpi = QtWidgets.QTableWidget(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_red_kpi.sizePolicy().hasHeightForWidth())
        self.tbl_red_kpi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbl_red_kpi.setFont(font)
        self.tbl_red_kpi.setObjectName("tbl_red_kpi")
        self.tbl_red_kpi.setColumnCount(0)
        self.tbl_red_kpi.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tbl_red_kpi)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_save_red_kpi = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_red_kpi.sizePolicy().hasHeightForWidth())
        self.btn_save_red_kpi.setSizePolicy(sizePolicy)
        self.btn_save_red_kpi.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_save_red_kpi.setFont(font)
        self.btn_save_red_kpi.setText("")
        self.btn_save_red_kpi.setIconSize(QtCore.QSize(32, 32))
        self.btn_save_red_kpi.setObjectName("btn_save_red_kpi")
        self.horizontalLayout_8.addWidget(self.btn_save_red_kpi)
        self.btn_del_red_kpi = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del_red_kpi.sizePolicy().hasHeightForWidth())
        self.btn_del_red_kpi.setSizePolicy(sizePolicy)
        self.btn_del_red_kpi.setMinimumSize(QtCore.QSize(0, 51))
        self.btn_del_red_kpi.setMaximumSize(QtCore.QSize(55, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_del_red_kpi.setFont(font)
        self.btn_del_red_kpi.setText("")
        self.btn_del_red_kpi.setIconSize(QtCore.QSize(32, 32))
        self.btn_del_red_kpi.setObjectName("btn_del_red_kpi")
        self.horizontalLayout_8.addWidget(self.btn_del_red_kpi)
        self.btn_line_up = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_line_up.sizePolicy().hasHeightForWidth())
        self.btn_line_up.setSizePolicy(sizePolicy)
        self.btn_line_up.setMinimumSize(QtCore.QSize(0, 51))
        self.btn_line_up.setMaximumSize(QtCore.QSize(55, 55))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(14)
        self.btn_line_up.setFont(font)
        self.btn_line_up.setText("")
        self.btn_line_up.setIconSize(QtCore.QSize(32, 32))
        self.btn_line_up.setObjectName("btn_line_up")
        self.horizontalLayout_8.addWidget(self.btn_line_up)
        self.btn_dell_line = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dell_line.sizePolicy().hasHeightForWidth())
        self.btn_dell_line.setSizePolicy(sizePolicy)
        self.btn_dell_line.setMinimumSize(QtCore.QSize(0, 51))
        self.btn_dell_line.setMaximumSize(QtCore.QSize(55, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_dell_line.setFont(font)
        self.btn_dell_line.setText("")
        self.btn_dell_line.setIconSize(QtCore.QSize(32, 32))
        self.btn_dell_line.setObjectName("btn_dell_line")
        self.horizontalLayout_8.addWidget(self.btn_dell_line)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tbl_struktura = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_struktura.sizePolicy().hasHeightForWidth())
        self.tbl_struktura.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbl_struktura.setFont(font)
        self.tbl_struktura.setObjectName("tbl_struktura")
        self.tbl_struktura.setColumnCount(0)
        self.tbl_struktura.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tbl_struktura)
        self.verticalLayout_12.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tbl_filtr = QtWidgets.QTableWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_filtr.sizePolicy().hasHeightForWidth())
        self.tbl_filtr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbl_filtr.setFont(font)
        self.tbl_filtr.setObjectName("tbl_filtr")
        self.tbl_filtr.setColumnCount(0)
        self.tbl_filtr.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tbl_filtr)
        self.verticalLayout_12.addWidget(self.groupBox_4)
        self.btn_save_struktura = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_struktura.sizePolicy().hasHeightForWidth())
        self.btn_save_struktura.setSizePolicy(sizePolicy)
        self.btn_save_struktura.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_save_struktura.setFont(font)
        self.btn_save_struktura.setText("")
        self.btn_save_struktura.setIconSize(QtCore.QSize(32, 32))
        self.btn_save_struktura.setObjectName("btn_save_struktura")
        self.verticalLayout_12.addWidget(self.btn_save_struktura)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new_user = QtWidgets.QAction(MainWindow)
        self.action_new_user.setObjectName("action_new_user")
        self.action_chnge_pass = QtWidgets.QAction(MainWindow)
        self.action_chnge_pass.setObjectName("action_chnge_pass")
        self.menu.addAction(self.action_new_user)
        self.menu.addAction(self.action_chnge_pass)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Пользователь"))
        self.btn_login.setText(_translate("MainWindow", "Вход"))
        self.le_parol.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.le_parol.setPlaceholderText(_translate("MainWindow", "Пароль..."))
        self.le_3_nParol.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.le_3_nParol.setPlaceholderText(_translate("MainWindow", "Новый пароль..."))
        self.le_3_nParol_2.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.le_3_nParol_2.setPlaceholderText(_translate("MainWindow", "Повтор новый пароль..."))
        self.btn_logout.setText(_translate("MainWindow", "Выход"))
        self.l_period.setText(_translate("MainWindow", "Период"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Схема"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Показатели"))
        self.l.setText(_translate("MainWindow", "КПЭотд.:"))
        self.l_kpi_otd.setText(_translate("MainWindow", "КПЭотд."))
        self.l_3.setText(_translate("MainWindow", "КПЭпроизводство:"))
        self.l_kpi_pr.setText(_translate("MainWindow", "КПЭотд."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Дата"))
        self.btn_save_sotr.setToolTip(_translate("MainWindow", "Сохранить КПЭ"))
        self.btn_rasschet.setToolTip(_translate("MainWindow", "Рассчет КПЭ"))
        self.btn_del_kpi_sotr.setToolTip(_translate("MainWindow", "Удалить КПЭ сотрудника на выбранный период."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "КПЭсотр."))
        self.l_tek_otd.setText(_translate("MainWindow", "Отдел"))
        self.btn_save_vn.setToolTip(_translate("MainWindow", "Сохранить"))
        self.btn_load_vn.setToolTip(_translate("MainWindow", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "КПЭвнеш."))
        self.btn_save_red_kpi.setToolTip(_translate("MainWindow", "Сохранить"))
        self.btn_del_red_kpi.setToolTip(_translate("MainWindow", "Удалить"))
        self.btn_line_up.setToolTip(_translate("MainWindow", "Поднять строку на уровень вверх"))
        self.btn_dell_line.setToolTip(_translate("MainWindow", "Удалить строку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Редактор КПЭ"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Подразделение"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Фильтр не оцениваемых сотрудников"))
        self.btn_save_struktura.setToolTip(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Структура"))
        self.menu.setTitle(_translate("MainWindow", "Опции"))
        self.action_new_user.setText(_translate("MainWindow", "Новый пользователь"))
        self.action_chnge_pass.setText(_translate("MainWindow", "Сменить пароль"))
