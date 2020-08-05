#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ctypes import *
# from ctypes import cdll, Structure
from ctypes.wintypes import HWND, DWORD

import win32api
from enum import IntEnum, unique, Enum
import sys, os
from PIL import Image, ImageQt
from utilities import ImageConvert, Utils, CustomBG

import cgitb  # 相当管用

cgitb.enable(format='text')  # 解决 pyqt5 异常只要进入事件循环,程序就崩溃,而没有任何提示


class WINDOWCOMPOSITIONATTRIB(IntEnum):
    WCA_UNDEFINED = 0
    WCA_NCRENDERING_ENABLED = 1
    WCA_NCRENDERING_POLICY = 2
    WCA_TRANSITIONS_FORCEDISABLED = 3
    WCA_ALLOW_NCPAINT = 4
    WCA_CAPTION_BUTTON_BOUNDS = 5
    WCA_NONCLIENT_RTL_LAYOUT = 6
    WCA_FORCE_ICONIC_REPRESENTATION = 7
    WCA_EXTENDED_FRAME_BOUNDS = 8
    WCA_HAS_ICONIC_BITMAP = 9
    WCA_THEME_ATTRIBUTES = 10
    WCA_NCRENDERING_EXILED = 11
    WCA_NCADORNMENTINFO = 12
    WCA_EXCLUDED_FROM_LIVEPREVIEW = 13
    WCA_VIDEO_OVERLAY_ACTIVE = 14
    WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15
    WCA_DISALLOW_PEEK = 16
    WCA_CLOAK = 17
    WCA_CLOAKED = 18
    WCA_ACCENT_POLICY = 19
    WCA_FREEZE_REPRESENTATION = 20
    WCA_EVER_UNCLOAKED = 21
    WCA_VISUAL_OWNER = 22
    WCA_LAST = 23


class WINDOWCOMPOSITIONATTRIBDATA(Structure):
    _fields_ = [('Attrib', WINDOWCOMPOSITIONATTRIB),
                ('pvData', c_void_p),  # PVOID
                ('cbData', c_ulong), ]  # SIZE_T


class ACCENT_STATE(IntEnum):
    ACCENT_DISABLED = 0
    ACCENT_ENABLE_GRADIENT = 1
    ACCENT_ENABLE_TRANSPARENTGRADIENT = 2
    ACCENT_ENABLE_BLURBEHIND = 3
    ACCENT_INVALID_STATE = 4


class ACCENT_POLICY(Structure):
    _fields_ = [('AccentState', ACCENT_STATE),
                ('AccentFlags', DWORD * 1),
                ('GradientColor', c_ulong),
                ('AnimationId', c_ulong), ]


# typedef BOOL(WINAPI*pfnSetWindowCompositionAttribute)(HWND, struct WINDOWCOMPOSITIONATTRIBDATA*)

def get_com(self, hWnd):
    # Utils.call_dll(self)
    hUser = win32api.GetModuleHandle("user32.dll")
    if hUser:
        print('user32.dll')
        setWindowCompositionAttribute = win32api.GetProcAddress(hUser, "SetWindowCompositionAttribute")
        # setWindowCompositionAttribute = (pfnSetWindowCompositionAttribute)setWindowCompositionAttribute
        print(type(setWindowCompositionAttribute))

        if setWindowCompositionAttribute:
            accent = ACCENT_POLICY(ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND, 0, 0, 0)
            data = WINDOWCOMPOSITIONATTRIBDATA()
            data.dwAttrib = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY
            data.pvData = accent
            data.cbData = sizeof(accent)
            setWindowCompositionAttribute(hWnd, data)


class MyEffect(QtWidgets.QGraphicsEffect):
    def __init__(self, *args, **kwargs):
        super(MyEffect, self).__init__(*args, **kwargs)

        self.item = QGraphicsItem()


# 带小三角的窗口
class ArrowWidget(QtWidgets.QWidget):
    SHADOW_WIDTH = 15  # 窗口阴影宽度
    BORDER_RADIUS = 5  # 窗口边角的弧度
    TRIANGLE_WIDTH = 15  # 小三角的宽度
    TRIANGLE_HEIGHT = 10  # 小三角的高度

    def __init__(self, *args, **kwargs):
        super(ArrowWidget, self).__init__(*args, **kwargs)

        self.start_pos = 0
        self.triangle_width = 0
        self.triangle_height = 0

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框窗口
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 设置阴影边框
        Utils.set_effect(self, 1, self.SHADOW_WIDTH, 0, 0, QtCore.Qt.gray)

        self.setFixedSize(150, 200)

    # 设置小三角起始位置;
    def set_start_pos(self, start_pox):
        self.start_pos = start_pox

    # 设置小三角宽和高
    def set_triangle(self, width, height):
        self.triangle_width = width
        self.triangle_height = height

    # 设置中间区域widget
    def set_center_widget(self, widget):
        lh = QtWidgets.QHBoxLayout(self)
        lh.addWidget(widget)
        lh.setSpacing(0)
        lh.setContentsMargins(self.SHADOW_WIDTH, self.SHADOW_WIDTH + self.TRIANGLE_HEIGHT,
                              self.SHADOW_WIDTH, self.SHADOW_WIDTH)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255))

        #  小三角区域
        trianglePolygon = QPolygon()
        trianglePolygon.setPoint(0, QPoint(self.start_pos, self.triangle_height + self.SHADOW_WIDTH))
        trianglePolygon.setPoint(1, QPoint(self.start_pos + self.triangle_width // 2, self.SHADOW_WIDTH))
        trianglePolygon.setPoint(2, QPoint(self.start_pos + self.triangle_width,
                                           self.triangle_height + self.SHADOW_WIDTH))
        # 小三角区域
        rect = QRect(self.SHADOW_WIDTH,
                     self.triangle_height + self.SHADOW_WIDTH,
                     self.width() - self.SHADOW_WIDTH * 2,
                     self.height() - self.SHADOW_WIDTH * 2 - self.triangle_height)

        drawPath = QPainterPath()
        drawPath.addRoundedRect(rect, self.BORDER_RADIUS, self.BORDER_RADIUS)

        # Rect + Triangle
        drawPath.addPolygon(trianglePolygon)
        painter.drawPath(drawPath)


class MainWin(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # self.use_palette()
        self.lb_bg = QtWidgets.QLabel()
        e1 = QtWidgets.QGraphicsBlurEffect()
        e1.setBlurRadius(20)
        e1.setBlurHints(QtWidgets.QGraphicsBlurEffect.QualityHint)
        self.lb_bg.setGraphicsEffect(e1)

        e2 = QtWidgets.QGraphicsDropShadowEffect()
        e2.setBlurRadius(20)  # 阴影半径，虚化程度，不能大于圆角半径
        e2.setOffset(5, 5)  # 阴影宽度
        e2.setColor(QtGui.QColor(0, 0, 0, 200))  # 阴影颜色
        self.lb_bg.setGraphicsEffect(e2)
        # self.lb_bg.setScaledContents(True)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框窗口
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setStyleSheet('background: rgba(255, 255, 255, 0);  /*半透明*/')

        self.setObjectName('w')

        self.pb = QPushButton('试看天下')
        self.pb.setFixedHeight(100)
        qss = '''
            QPushButton{/*默认显示*/
                border-radius:40px;/*圆角弧度(为正方形边长一半时就是圆形)*/
                background-color:rgba(0,255,0,255);/*背景色*/
            }
            QPushButton:hover{/*鼠标悬停*/
                background-color:rgba(0,0,255,255);
            }
            QPushButton:pressed{/*鼠标按下*/
                background-color:rgba(255,0,0,255);
            }
        '''
        self.pb.setStyleSheet(qss)
        # self.pb.setStyleSheet('background-image:url(./res/background/bk3.jpg); /*  */'
        #                       'border-radius:15px;     /*画出圆角*/')

        # w = ArrowWidget()
        # w.set_start_pos(60)
        # w.set_triangle(20, 12)
        # w.setFixedSize(QSize(150, 80))
        # textLabel = QLabel("ArrowWidget")
        # textLabel.setAlignment(Qt.AlignCenter)
        # w.set_center_widget(textLabel)
        # w.show()

        lv = QVBoxLayout(self)
        lv.addWidget(self.lb_bg)
        lv.addWidget(self.pb)

        self.get_com()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super(MainWin, self).resizeEvent(a0)
        # self.lb_bg.update()
        self.lb_bg.resize(self.width() - 300, self.height() - 200)
        self.lb_bg.setPixmap(Utils.img_center(self.lb_bg.width(),
                                              self.lb_bg.height(),
                                              './res/background/bk5.jpg'))
        # Utils.setBg(self, self.lb_bg, './res/background/bk2.jpg')
        # self.lb_bg.setAlignment(Qt.AlignCenter)
        # self.lb_bg.resize(self.width() // 2, self.height() // 2)
        # pix = Utils.img_center(self.lb_bg.width(), self.lb_bg.height(),
        #                        './res/background/bk1.jpg')
        # print('here',type(pix))
        # self.lb_bg.setPixmap(pix)
        # self.lb_bg.setPixmap(QPixmap('./res/background/bk1.jpg'))

        # self.pb.resize(200, 800)
        # self.pb.setStyleSheet('border-radius:15px;     /*画出圆角*/')

    def use_palette(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(),
                             QBrush(QPixmap("./res/background/bk1.jpg")))
        self.setPalette(window_pale)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()

    # w = ArrowWidget()
    # w.set_start_pos(60)
    # w.set_triangle(20, 12)
    # # w.setFixedSize(QSize(150, 80))
    # textLabel = QLabel("ArrowWidget")
    # textLabel.setAlignment(Qt.AlignCenter)
    # w.set_center_widget(textLabel)
    # w.show()

    sys.exit(app.exec_())
