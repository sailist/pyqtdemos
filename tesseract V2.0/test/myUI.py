#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Desc    : 描述
# @Author  : zwy
# @File    : myUI.py
# @Time    : 2019/8/31 14:25
# @Software: PyCharm

import traceback

from PyQt5.QtCore import QSize, QRect, QRectF, QPoint
from PyQt5.QtGui import QKeyEvent, QImage, QPainter, QPaintEvent, QPalette, QBrush, QColor, QMouseEvent, QPainterPath, \
    QPen
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt


class ScreenCaptureFrame(QWidget):
    def __init__(self, parent, img: QImage = None):
        super(ScreenCaptureFrame, self).__init__()

        # 保存父窗口
        self.parentWin = parent
        # 设置窗口无标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 设置模态窗口
        # self.setWindowModality(Qt.ApplicationModal)

        if img != None:
            self.backImg = img
            self.setFixedSize(img.width(), img.height())
            # 设置控件背影图片
            # palette = QPalette()
            # palette.setBrush(QPalette.Background, QBrush(img))
            # self.setPalette(palette)
            self.show()
        else:
            self.setFixedSize(500, 500)
            self.show()
            # QMessageBox.information(parent, "消息提示", "屏幕截图失败", QMessageBox.Ok)

    def keyReleaseEvent(self, event: QKeyEvent):
        """
        重写按键事件
        :param event:
        :return:
        """
        try:
            # esc键关闭窗口
            if event.key() == Qt.Key_Escape:
                self.close()
                # 父窗口恢复显示
                self.parentWin.showNormal()
            # enter键(数字键盘为Key_Enter)返回主窗口识图
            elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                if not (self.startPoint.x() == self.endPoint.x() and self.startPoint.y() == self.endPoint.y()):
                    image = self.backImg.copy(QRect(self.startPoint, self.endPoint))
                    self.close()
                    # 父窗口恢复显示
                    self.parentWin.showNormal()
                    self.parentWin.childWinCallBack(image)
            # space键保存选择区域为图片
            elif event.key() == Qt.Key_Space:
                if not (self.startPoint.x() == self.endPoint.x() and self.startPoint.y() == self.endPoint.y()):
                    filePath, fileType = QFileDialog.getSaveFileName(self, "保存截图", "./",
                                                                     "jpg图片 (*.jpg);;bmp图片(*.bmp);;png图片(*.png)")
                    if filePath.strip() != "":
                        image = self.backImg.copy(QRect(self.startPoint, self.endPoint))
                        image.save(filePath)
                        self.close()
                        # 父窗口恢复显示
                        self.parentWin.showNormal()


        except Exception as e:
            traceback.print_exc()

    def mousePressEvent(self, event: QMouseEvent):
        """
        重写鼠标按下事件
        :param event:
        :return:
        """
        try:
            # 鼠标左键按下记录矩形开始点
            if event.button() == Qt.LeftButton:
                self.startPoint = event.pos()
                self.isLeftPress = True
            else:
                self.isLeftPress = False
        except Exception as e:
            traceback.print_exc()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        重写鼠标松开事件
        :param event:
        :return:
        """
        try:
            # 鼠标左键按下记录矩形结束点
            if event.button() == Qt.LeftButton:
                self.endPoint = event.pos()
                self.isLeftPress = False
                self.repaint()
        except Exception as e:
            traceback.print_exc()

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        重写鼠标移动事件
        :param event:
        :return:
        """
        try:
            # 鼠标左键按下记录矩形结束点
            if hasattr(self, "isLeftPress") and self.isLeftPress:
                self.endPoint = event.pos()
                self.repaint()
        except Exception as e:
            traceback.print_exc()

    def paintEvent(self, event: QPaintEvent):
        """
        重写绘图事件
        :param event:
        :return:
        """
        try:
            backPath = QPainterPath()
            backPath.addRect(0, 0, self.width(), self.height())
            fillPath = QPainterPath()
            if hasattr(self, "startPoint") and hasattr(self, "endPoint"):
                movePath = QPainterPath()
                movePath.addRect(QRectF(self.startPoint, self.endPoint))
                fillPath = backPath.subtracted(movePath)
            else:
                fillPath = backPath
            # 创建绘图设备
            painter = QPainter(self)
            # 绘制背景图
            painter.drawImage(QPoint(0, 0), self.backImg)
            painter.setPen(QPen(QColor(87, 170, 255), 5, Qt.SolidLine))
            # painter.drawPath(fillPath)
            # 填充非选择区域
            painter.fillPath(fillPath, QColor(0, 0, 0, 100))

        except Exception as e:
            traceback.print_exc()
