# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\MainWindow.ui'
#
# Created: Sun Feb 10 18:38:32 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(609, 387)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboUser = QtGui.QComboBox(self.centralwidget)
        self.comboUser.setObjectName(_fromUtf8("comboUser"))
        self.horizontalLayout_2.addWidget(self.comboUser)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.dateStamp = QtGui.QDateEdit(self.centralwidget)
        self.dateStamp.setCalendarPopup(True)
        self.dateStamp.setObjectName(_fromUtf8("dateStamp"))
        self.horizontalLayout.addWidget(self.dateStamp)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.treeEvents = QtGui.QTreeWidget(self.centralwidget)
        self.treeEvents.setObjectName(_fromUtf8("treeEvents"))
        self.treeEvents.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.treeEvents, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHideColUser = QtGui.QAction(MainWindow)
        self.actionHideColUser.setObjectName(_fromUtf8("actionHideColUser"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.menu.addAction(self.actionExit)
        self.menu_3.addAction(self.actionRefresh)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EventViewLite", None))
        self.label.setText(_translate("MainWindow", "Пользователь:", None))
        self.label_2.setText(_translate("MainWindow", "Дата:", None))
        self.menu.setTitle(_translate("MainWindow", "Меню", None))
        self.menu_3.setTitle(_translate("MainWindow", "События", None))
        self.actionExit.setText(_translate("MainWindow", "Выход", None))
        self.actionHideColUser.setText(_translate("MainWindow", "Скрыть колонку Пользователь", None))
        self.actionRefresh.setText(_translate("MainWindow", "Обновить", None))
        self.actionRefresh.setShortcut(_translate("MainWindow", "F5", None))

