# coding: utf-8

import sys
import sqlite3
from cx_Freeze import setup, Executable
assert sys.platform == "win32"

exe = Executable(
    script="evl.py",
    initScript=None,
    base="Win32GUI",
    compress=True,
    copyDependentFiles=True,
    icon=None
)

setup(
    name = "evl",
    version = "0.1",
    author = "Valentin Novikov",
    description = "Windows Events Viewer",
    executables = [exe],
    options = {
        'build_exe': {
            'includes': [],
            'excludes': [],
            'packages': [],
            'path': [],
            }
    },
)
