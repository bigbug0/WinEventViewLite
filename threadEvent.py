# coding: utf-8
# Copyright 2013, Valentin Novikov <lannor74@gmail.com>

__all__ = [ 'ThreadEvents' ]

import re
import winerror
import win32evtlog
import win32evtlogutil
from PyQt4 import QtCore
from datetime import datetime

re_username = re.compile(u'Имя учетной записи:[ \t](?P<name>.*)', re.IGNORECASE)

class ThreadEvents(QtCore.QThread):
    #d_events = {
    #    win32con.EVENTLOG_AUDIT_FAILURE: 'EVENTLOG_AUDIT_FAILURE',
    #    win32con.EVENTLOG_AUDIT_SUCCESS: 'EVENTLOG_AUDIT_SUCCESS',
    #    win32con.EVENTLOG_INFORMATION_TYPE: 'EVENTLOG_INFORMATION_TYPE',
    #    win32con.EVENTLOG_WARNING_TYPE: 'EVENTLOG_WARNING_TYPE',
    #    win32con.EVENTLOG_ERROR_TYPE: 'EVENTLOG_ERROR_TYPE',
    #}

    def __init__(self, parent, mutex, day, event_ids=[4624,4625], server='localhost', logtype='Security'):
        QtCore.QThread.__init__(self, parent)

        self.day = day
        self._mutex = mutex
        self.server = server
        self.logtype = logtype
        self.event_ids = set(event_ids)
        self.currentUser = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, d):
        if isinstance(d, (QtCore.QDate, QtCore.QDateTime)):
            d = d.toPyDate()
        self._day = d

    def fixdatetime(self, s, to_str=True):
        result = datetime.strptime(s, '%m/%d/%y %H:%M:%S')
        return result.strftime('%d.%m.%Y %H:%M:%S') if to_str else result

    def findUsername(self, s, default=None):
        result = re_username.finditer(s)
        if result:
            result = list(result)
            return result[1].group('name').strip()
        return default

    def run(self):
        self._mutex.lock()
        startTime = datetime.now()
        handler = win32evtlog.OpenEventLog(self.server, self.logtype)
        total = win32evtlog.GetNumberOfEventLogRecords(handler)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(handler, flags, 0)

        events = 1
        total_ok = 0

        _users = [u'Администратор']
        self.emit(QtCore.SIGNAL('start(int)'), total)

        try:
            while events:
                events = win32evtlog.ReadEventLog(handler, flags, 0)
                for ev_obj in events:
                    event_id = int(winerror.HRESULT_CODE(ev_obj.EventID))
                    if len(self.event_ids) > 0 and event_id not in self.event_ids:
                        continue

                    event_time=self.fixdatetime(ev_obj.TimeGenerated.Format(), to_str=False)
                    if self.day != event_time.date():
                        continue

                    event_message=unicode(win32evtlogutil.SafeFormatMessage(ev_obj, self.logtype))
                    event_username=self.findUsername(event_message)
                    if self.currentUser and self.currentUser != event_username:
                        continue

                    event_type=int(ev_obj.EventType)
                    event_category=int(ev_obj.EventCategory)
                    event_record=int(ev_obj.RecordNumber)
                    event_source=unicode(ev_obj.SourceName)
                    event_time = event_time.strftime('%d.%m.%Y %H:%M:%S')
                    event_hostname=unicode(ev_obj.ComputerName)

                    total_ok += 1
                    self.emit(QtCore.SIGNAL('event(QString, QString, QString, int, int, int, int, QString, QString, QString, QString)'),
                        self.server, self.logtype, event_username,
                        event_id, event_type, event_category, event_record,
                        event_source, event_time, event_hostname, event_message)
                    if event_username not in _users:
                        self.emit(QtCore.SIGNAL('user(QString)'), event_username)
                        _users.append(event_username)
        except Exception as err:
            self.emit(QtCore.SIGNAL('error(QString)'), repr(err))
            events = -1
        finally:
            stopTime = datetime.now()
            delta = (stopTime - startTime).total_seconds()
            self.emit(QtCore.SIGNAL('finish(int, int, float)'), total_ok, total, delta)
            self._mutex.unlock()
