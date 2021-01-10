# -*- coding: utf-8 -*-
# @Author  : zwy
# @File    : main.py
# @Time    : 2019/8/14 22:34
# @Software: PyCharm

import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import traceback
from test import tesseractTest

if __name__ == '__main__':
    try:
        # tesseractTest类调用
        tesseractTest.MyTesseract.tesseract()
        pass
    except Exception as e:
        traceback.print_exc()
