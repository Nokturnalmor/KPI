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
        MainWindow.resize(1285, 898)
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
        self.groupBox.setMinimumSize(QtCore.QSize(0, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_empl = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_empl.sizePolicy().hasHeightForWidth())
        self.comboBox_empl.setSizePolicy(sizePolicy)
        self.comboBox_empl.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_empl.setFont(font)
        self.comboBox_empl.setAutoFillBackground(True)
        self.comboBox_empl.setObjectName("comboBox_empl")
        self.verticalLayout.addWidget(self.comboBox_empl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        self.pushButton_login.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.lineEdit_parol = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_parol.sizePolicy().hasHeightForWidth())
        self.lineEdit_parol.setSizePolicy(sizePolicy)
        self.lineEdit_parol.setMinimumSize(QtCore.QSize(0, 51))
        self.lineEdit_parol.setStatusTip("")
        self.lineEdit_parol.setWhatsThis("")
        self.lineEdit_parol.setInputMask("")
        self.lineEdit_parol.setText("")
        self.lineEdit_parol.setMaxLength(22)
        self.lineEdit_parol.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_parol.setObjectName("lineEdit_parol")
        self.horizontalLayout.addWidget(self.lineEdit_parol)
        self.lineEdit_3_nParol = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3_nParol.sizePolicy().hasHeightForWidth())
        self.lineEdit_3_nParol.setSizePolicy(sizePolicy)
        self.lineEdit_3_nParol.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3_nParol.setFont(font)
        self.lineEdit_3_nParol.setStatusTip("")
        self.lineEdit_3_nParol.setWhatsThis("")
        self.lineEdit_3_nParol.setInputMask("")
        self.lineEdit_3_nParol.setText("")
        self.lineEdit_3_nParol.setMaxLength(22)
        self.lineEdit_3_nParol.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3_nParol.setObjectName("lineEdit_3_nParol")
        self.horizontalLayout.addWidget(self.lineEdit_3_nParol)
        self.lineEdit_3_nParol_2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3_nParol_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_3_nParol_2.setSizePolicy(sizePolicy)
        self.lineEdit_3_nParol_2.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3_nParol_2.setFont(font)
        self.lineEdit_3_nParol_2.setStatusTip("")
        self.lineEdit_3_nParol_2.setWhatsThis("")
        self.lineEdit_3_nParol_2.setInputMask("")
        self.lineEdit_3_nParol_2.setText("")
        self.lineEdit_3_nParol_2.setMaxLength(22)
        self.lineEdit_3_nParol_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3_nParol_2.setObjectName("lineEdit_3_nParol_2")
        self.horizontalLayout.addWidget(self.lineEdit_3_nParol_2)
        self.pushButton_logout = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_logout.sizePolicy().hasHeightForWidth())
        self.pushButton_logout.setSizePolicy(sizePolicy)
        self.pushButton_logout.setMinimumSize(QtCore.QSize(122, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_img = QtWidgets.QLabel(self.tab_4)
        self.label_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.horizontalLayout_4.addWidget(self.label_img)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2020, 1, 14))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.LongDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_4.addWidget(self.calendarWidget)
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
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_kpi_otd = QtWidgets.QLabel(self.groupBox_2)
        self.label_kpi_otd.setObjectName("label_kpi_otd")
        self.horizontalLayout_2.addWidget(self.label_kpi_otd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_kpi_pr = QtWidgets.QLabel(self.groupBox_2)
        self.label_kpi_pr.setObjectName("label_kpi_pr")
        self.horizontalLayout_3.addWidget(self.label_kpi_pr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_rabotn = QtWidgets.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_rabotn.setFont(font)
        self.comboBox_rabotn.setObjectName("comboBox_rabotn")
        self.verticalLayout_8.addWidget(self.comboBox_rabotn)
        self.tableWidget_kpi = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_kpi.setFont(font)
        self.tableWidget_kpi.setObjectName("tableWidget_kpi")
        self.tableWidget_kpi.setColumnCount(0)
        self.tableWidget_kpi.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_kpi)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_save_sotr = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_sotr.sizePolicy().hasHeightForWidth())
        self.pushButton_save_sotr.setSizePolicy(sizePolicy)
        self.pushButton_save_sotr.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_save_sotr.setFont(font)
        self.pushButton_save_sotr.setObjectName("pushButton_save_sotr")
        self.horizontalLayout_7.addWidget(self.pushButton_save_sotr)
        self.pushButton_load_sotr = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load_sotr.sizePolicy().hasHeightForWidth())
        self.pushButton_load_sotr.setSizePolicy(sizePolicy)
        self.pushButton_load_sotr.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_load_sotr.setFont(font)
        self.pushButton_load_sotr.setObjectName("pushButton_load_sotr")
        self.horizontalLayout_7.addWidget(self.pushButton_load_sotr)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_save_vn = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_vn.sizePolicy().hasHeightForWidth())
        self.pushButton_save_vn.setSizePolicy(sizePolicy)
        self.pushButton_save_vn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_save_vn.setFont(font)
        self.pushButton_save_vn.setObjectName("pushButton_save_vn")
        self.horizontalLayout_6.addWidget(self.pushButton_save_vn)
        self.pushButton_load_vn = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load_vn.sizePolicy().hasHeightForWidth())
        self.pushButton_load_vn.setSizePolicy(sizePolicy)
        self.pushButton_load_vn.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_load_vn.setFont(font)
        self.pushButton_load_vn.setObjectName("pushButton_load_vn")
        self.horizontalLayout_6.addWidget(self.pushButton_load_vn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comboBox_dolgn_red = QtWidgets.QComboBox(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_dolgn_red.setFont(font)
        self.comboBox_dolgn_red.setObjectName("comboBox_dolgn_red")
        self.verticalLayout_6.addWidget(self.comboBox_dolgn_red)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.pushButton_save_red_kpi = QtWidgets.QPushButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_red_kpi.sizePolicy().hasHeightForWidth())
        self.pushButton_save_red_kpi.setSizePolicy(sizePolicy)
        self.pushButton_save_red_kpi.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_save_red_kpi.setFont(font)
        self.pushButton_save_red_kpi.setObjectName("pushButton_save_red_kpi")
        self.verticalLayout_6.addWidget(self.pushButton_save_red_kpi)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Пользователь"))
        self.pushButton_login.setText(_translate("MainWindow", "Вход"))
        self.lineEdit_parol.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.lineEdit_parol.setPlaceholderText(_translate("MainWindow", "Пароль..."))
        self.lineEdit_3_nParol.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.lineEdit_3_nParol.setPlaceholderText(_translate("MainWindow", "Новый пароль..."))
        self.lineEdit_3_nParol_2.setToolTip(_translate("MainWindow", "Для логина и смены пароля"))
        self.lineEdit_3_nParol_2.setPlaceholderText(_translate("MainWindow", "Повтор новый пароль..."))
        self.pushButton_logout.setText(_translate("MainWindow", "Выход"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Схема"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Показатели"))
        self.label.setText(_translate("MainWindow", "КПЭотд.:"))
        self.label_kpi_otd.setText(_translate("MainWindow", "КПЭотд."))
        self.label_3.setText(_translate("MainWindow", "КПЭпроизводство:"))
        self.label_kpi_pr.setText(_translate("MainWindow", "КПЭотд."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Дата"))
        self.pushButton_save_sotr.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_load_sotr.setText(_translate("MainWindow", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "КПЭсотр."))
        self.pushButton_save_vn.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_load_vn.setText(_translate("MainWindow", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "КПЭвнеш."))
        self.pushButton_save_red_kpi.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Редактор КПЭ"))
        self.menu.setTitle(_translate("MainWindow", "Опции"))
        self.action.setText(_translate("MainWindow", "Новый пользователь"))
        self.action_2.setText(_translate("MainWindow", "Сменить пароль"))
