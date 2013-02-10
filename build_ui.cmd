@echo off

C:\Python27\python.exe C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py UI\MainWindow.ui > UI\MainWindow_ui.py
C:\Python27\python.exe setup.py build
