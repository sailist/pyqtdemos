#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Desc    : 描述
# @Author  : zwy
# @File    : tesseractTest.py
# @Time    : 2019/8/21 9:44
# @Software: PyCharm
import datetime
import os
import sys
import time
import traceback
from test import myUI

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from test.tesseractUI import Ui_MainWindow


class MyTesseract(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)

        # 设置控件属性
        self.ocrResultTableView.horizontalHeader().setSectionsMovable(True)

        # 绑定事件
        self.openFilePushButton.clicked.connect(self.openFilePushButtonClick)
        self.ocrPushButton.clicked.connect(self.ocrPushButtonClick)
        self.hidePushButton.clicked.connect(self.hidePushButtonClick)
        self.screenOCRPushButton.clicked.connect(self.screeenOCRPushButtonClick)

        self.ocrResultTableView.clicked.connect(self.ocrResultTableViewEvent)

    def ocrResultTableViewEvent(self, arg):
        try:
            modelIndex = self.ocrResultTableView.currentIndex()
            self.statusbar.showMessage("单击表格[行%s：列%s]" % (modelIndex.row(), modelIndex.column()))

            # 清除之前选中项
            # self.scene.clearSelection()
            # 清除之前明矩形填充框
            if hasattr(self, "pixMapItem"):
                self.scene.removeItem(self.pixMapItem)
            # 设置选中项
            rectItem: QGraphicsRectItem = self.boxItems[modelIndex.row()]["item"]
            # rectItem.setSelected(True)
            # 生成透明矩形标识选中项
            pixMap = QPixmap(rectItem.rect().width(), rectItem.rect().height())
            pixMap.fill(QColor(170, 85, 255, 100))
            self.pixMapItem = QGraphicsPixmapItem(pixMap)
            self.pixMapItem.setPos(rectItem.rect().left(), rectItem.rect().top())
            self.scene.addItem(self.pixMapItem)

        except Exception as e:
            traceback.print_exc()

    def openFilePushButtonClick(self):
        self.statusbar.showMessage("单击 [%s]" % self.openFilePushButton.text())
        try:
            filePath, fileType = QFileDialog.getOpenFileName(self, "选择图片", "./capture", "imges (*.bmp;*.jpg;*.png)")
            if os.path.exists(filePath):
                self.statusbar.showMessage("打开文件：" + filePath)
                self.filePath = filePath
                self.imgTtem = QGraphicsPixmapItem(QPixmap(filePath))
                self.scene = QGraphicsScene()
                self.scene.addItem(self.imgTtem)
                self.showGraphicsView.setScene(self.scene)
        except Exception as e:
            traceback.print_exc()

    def ocrPushButtonClick(self):
        pass
        # self.statusbar.showMessage("单击 [%s]" % self.ocrPushButton.text())
        # try:
        #     if hasattr(self, "filePath") and os.path.exists(self.filePath):
        #         print("识别开始：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #         # resultDate = pytesseract.image_to_data(Image.open(self.filePath), lang="chi_sim",
        #         #                                        output_type=Output.DICT)
        #         print("识别结束：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #         # 新建box数组:left,top,width,height,text,conf,world_num,line_num,block_num,page_num,level
        #         self.boxItems = []
        #         for k, v in resultDate.items():
        #             for i, x in enumerate(v):
        #                 if len(self.boxItems) > i:
        #                     if k == "left":
        #                         self.boxItems[i]["rect"].setLeft(x)
        #                     elif k == "top":
        #                         self.boxItems[i]["rect"].setTop(x)
        #                     elif k == "width":
        #                         self.boxItems[i]["rect"].setWidth(x)
        #                     elif k == "height":
        #                         self.boxItems[i]["rect"].setHeight(x)
        #                     else:
        #                         self.boxItems[i][k] = x
        #                 else:
        #                     item = {}
        #                     rect = QRectF()
        #                     if k == "left":
        #                         rect.setLeft(x)
        #                         item["rect"] = rect
        #                     elif k == "top":
        #                         rect.setTop(x)
        #                         item["rect"] = rect
        #                     elif k == "width":
        #                         rect.setWidth(x)
        #                         item["rect"] = rect
        #                     elif k == "height":
        #                         rect.setHeight(x)
        #                         item["rect"] = rect
        #                     else:
        #                         item[k] = x
        #                         item["rect"] = rect
        #                     self.boxItems.append(item)
        #
        #         print("数据过滤开始：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #         self.boxItems = [x for x in self.boxItems if x["conf"] != "-1"]
        #         print("数据过滤结束：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #         # [print(x) for x in self.boxItems]
        #
        #         if len(self.boxItems) <= 0:
        #             QMessageBox.information(self, "提示消息", "未识别到任何有效文本！", QMessageBox.Ok)
        #             return
        #
        #             # table设置model
        #         standardItemModel = QStandardItemModel()
        #         standardItemModel.setHorizontalHeaderLabels(list(self.boxItems[0].keys()))
        #         for r, rv in enumerate(self.boxItems):
        #             for c, cv in enumerate(rv.values()):
        #                 if isinstance(cv, QRectF):
        #                     cv = str(int(cv.left())) + ", " + str(int(cv.top())) + ", " + str(
        #                         int(cv.width())) + ", " + str(int(cv.height()))
        #                 standardItemModel.setItem(r, c, QStandardItem(str(cv)))
        #         self.ocrResultTableView.setModel(standardItemModel)
        #         self.ocrResultTableView.resizeColumnsToContents()
        #
        #         # 显示rect
        #         for i, rect in enumerate(self.boxItems):
        #             item = QGraphicsRectItem(rect["rect"])
        #             item.setFlag(QGraphicsItem.ItemIsSelectable)
        #             item.setPen(QColor("red"))
        #             self.boxItems[i]["item"] = item
        #             self.scene.addItem(item)
        #     else:
        #         QMessageBox.information(self, "提示消息", "未打开有效图片，图片路径无效！", QMessageBox.Ok)
        # except Exception as e:
        #     traceback.print_exc()

    def hidePushButtonClick(self):
        self.statusbar.showMessage("单击 [%s]" % self.hidePushButton.text())
        try:
            if hasattr(self, "boxItems"):
                # 隐藏边框
                if self.hidePushButton.text() == "隐藏边框":
                    self.hidePushButton.setText("显示边框")
                    for item in self.boxItems:
                        item["item"].setVisible(False)
                else:
                    self.hidePushButton.setText("隐藏边框")
                    for item in self.boxItems:
                        item["item"].setVisible(True)

        except Exception as e:
            traceback.print_exc()

    def screeenOCRPushButtonClick(self):
        try:
            # 隐藏父窗口
            self.showMinimized()
            # 窗口隐藏延迟，睡眠0.2秒
            time.sleep(0.2)
            # 屏幕截图
            backImg = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId()).toImage()
            # 创建屏幕截图窗口
            self.screenCaptureFrame = myUI.ScreenCaptureFrame(self, backImg)
            # 子窗口全屏显示
            self.screenCaptureFrame.showFullScreen()
        except Exception as e:
            traceback.print_exc()

    def childWinCallBack(self, image: QImage):
        """
        子窗口传值回调
        :return:
        """
        try:
            # 设置图片显示
            self.filePath = ""
            self.imgTtem = QGraphicsPixmapItem(QPixmap.fromImage(image))
            self.scene = QGraphicsScene()
            self.scene.addItem(self.imgTtem)
            self.showGraphicsView.setScene(self.scene)

            print("识别开始：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        except:
            pass
        #     resultDate = pytesseract.image_to_data(ImageQt.fromqimage(image), lang="chi_sim", output_type=Output.DICT)
        #     print("识别结束：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #     # 新建box数组:left,top,width,height,text,conf,world_num,line_num,block_num,page_num,level
        #     self.boxItems = []
        #     for k, v in resultDate.items():
        #         for i, x in enumerate(v):
        #             if len(self.boxItems) > i:
        #                 if k == "left":
        #                     self.boxItems[i]["rect"].setLeft(x)
        #                 elif k == "top":
        #                     self.boxItems[i]["rect"].setTop(x)
        #                 elif k == "width":
        #                     self.boxItems[i]["rect"].setWidth(x)
        #                 elif k == "height":
        #                     self.boxItems[i]["rect"].setHeight(x)
        #                 else:
        #                     self.boxItems[i][k] = x
        #             else:
        #                 item = {}
        #                 rect = QRectF()
        #                 if k == "left":
        #                     rect.setLeft(x)
        #                     item["rect"] = rect
        #                 elif k == "top":
        #                     rect.setTop(x)
        #                     item["rect"] = rect
        #                 elif k == "width":
        #                     rect.setWidth(x)
        #                     item["rect"] = rect
        #                 elif k == "height":
        #                     rect.setHeight(x)
        #                     item["rect"] = rect
        #                 else:
        #                     item[k] = x
        #                     item["rect"] = rect
        #                 self.boxItems.append(item)
        #
        #     print("数据过滤开始：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #     self.boxItems = [x for x in self.boxItems if x["conf"] != "-1"]
        #     print("数据过滤结束：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),))
        #     # [print(x) for x in self.boxItems]
        #
        #     if len(self.boxItems) <= 0:
        #         QMessageBox.information(self, "提示消息", "未识别到任何有效文本！", QMessageBox.Ok)
        #         return
        #
        #     # table设置model
        #     standardItemModel = QStandardItemModel()
        #     standardItemModel.setHorizontalHeaderLabels(list(self.boxItems[0].keys()))
        #     for r, rv in enumerate(self.boxItems):
        #         for c, cv in enumerate(rv.values()):
        #             if isinstance(cv, QRectF):
        #                 cv = str(int(cv.left())) + ", " + str(int(cv.top())) + ", " + str(
        #                     int(cv.width())) + ", " + str(int(cv.height()))
        #             standardItemModel.setItem(r, c, QStandardItem(str(cv)))
        #     self.ocrResultTableView.setModel(standardItemModel)
        #     self.ocrResultTableView.resizeColumnsToContents()
        #
        #     # 显示rect
        #     for i, rect in enumerate(self.boxItems):
        #         item = QGraphicsRectItem(rect["rect"])
        #         item.setFlag(QGraphicsItem.ItemIsSelectable)
        #         item.setPen(QColor("red"))
        #         self.boxItems[i]["item"] = item
        #         self.scene.addItem(item)
        # except Exception as e:
        #     traceback.print_exc()

    @staticmethod
    def tesseract():
        app = QApplication(sys.argv)
        myWin = MyTesseract()
        myWin.show()
        app.exec_()
