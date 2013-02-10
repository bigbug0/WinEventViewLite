# coding: utf-8
# Copyright 2013, Valentin Novikov <lannor74@gmail.com>

import sys
import atexit
from PyQt4 import QtCore, QtGui
from UI.MainWindow_ui import Ui_MainWindow
from threadEvent import ThreadEvents

mutex = QtCore.QMutex()

class MainWindow(QtGui.QMainWindow):
    _tree_headers = (u'Дата', u'Пользователь', u'Событие')

    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(u'EventViewLite [x86-pre-alpha0]')
        self.ui.treeEvents.setAlternatingRowColors(True)
        self.ui.treeEvents.setSortingEnabled(True)

        self.clearTreeEvents()
        self.dateStampRefresh()
        self.clearComboUsers()

        self.ui.comboUser.setCurrentIndex(1)
        self.threadRefresh = ThreadEvents(self, mutex, self.ui.dateStamp.date())

        def db_event(server, journal, username, event_id, event_type, event_category, event_record,
                     event_source, event_time, event_hostname, event_message, *args):
            event_message = unicode(event_message)
            rootItem = QtGui.QTreeWidgetItem(self.ui.treeEvents)
            rootItem.setText(0, event_time)
            rootItem.setText(1, username)
            rootItem.setText(2, event_message.split('\n')[0].strip())
            rootItem.setToolTip(0, event_message)
        self.ui.actionRefresh.triggered.connect(self.refreshEvents)
        self.ui.actionExit.triggered.connect(lambda: sys.exit(0))
        QtCore.QObject.connect(self.threadRefresh,
            QtCore.SIGNAL('user(QString)'),
            self.ui.comboUser.addItem)
        QtCore.QObject.connect(self.threadRefresh,
            QtCore.SIGNAL('event(QString, QString, QString, int, int, int, int,'
                                'QString, QString, QString, QString)'),
            db_event)
        QtCore.QObject.connect(self.threadRefresh,
            QtCore.SIGNAL('finish(int, int, float)'),
            self.threadRefreshFinished)
        QtCore.QObject.connect(self.threadRefresh,
            QtCore.SIGNAL('error(QString)'),
            self.ui.statusbar.showMessage)

        self.ui.actionRefresh.trigger()

    def threadRefreshFinished(self, total_ok, total, delta, *args):
        day = self.threadRefresh.day.strftime('%d.%m.%Y')
        self.statusBar().showMessage(u'[%s] Получено %d событий от %s (за %.02f секунд)' %
                                     (self.threadRefresh.currentUser or u'Все', total_ok, day, delta))
        if total_ok < 1:
            item = QtGui.QTreeWidgetItem(self.ui.treeEvents)
            item.setText(0, day)
            item.setText(1, self.threadRefresh.currentUser or '')
            item.setText(2, u'Событий не найдено!')

    def refreshEvents(self):
        self.clearTreeEvents()
        if self.ui.comboUser.currentIndex() < 1:
            user = None
        else:
            user = self.ui.comboUser.currentText()
        self.clearComboUsers()
        self.threadRefresh.currentUser = user
        self.threadRefresh.day = self.ui.dateStamp.date()
        self.threadRefresh.start()

    def dateStampRefresh(self):
        self.ui.dateStamp.setDate(QtCore.QDate().currentDate())

    def clearTreeEvents(self):
        self.ui.treeEvents.clear()
        self.ui.treeEvents.setHeaderLabels(self._tree_headers)
        self.ui.dateStamp.setMaximumDate(QtCore.QDate.currentDate())

    def clearComboUsers(self):
        self.ui.comboUser.clear()
        self.ui.comboUser.addItems([u'Все', u'Администратор'])
        self.ui.comboUser.setCurrentIndex(1)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
