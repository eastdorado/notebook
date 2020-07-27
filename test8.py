#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os
from PIL import Image, ImageQt
from utilities import ImageConvert, Utils

import cgitb  # 相当管用

cgitb.enable(format='text')  # 解决 pyqt5 异常只要进入事件循环,程序就崩溃,而没有任何提示


class MainWin(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # self.use_palette()
        self.lb_bg = QLabel(self)
        # Utils.set_effect(self.lb_bg, 0, 10, QGraphicsBlurEffect.QualityHint)
        # self.lb_bg.resize(600, 500)
        # pix = self.get_center_image(self.lb_bg.width(), self.lb_bg.height())
        # print('here',type(pix))
        # self.lb_bg.setPixmap(pix)

        # Utils.bg_trans('./tmp.png', 200, 200, (22, 33, 233, 123))
        # lb.setPixmap(Utils.bg_trans(''))
        # pix = self.get_center_image(lb, './res/background/bk1.jpg')
        # pix = QPixmap('./res/background/bk1.jpg')
        # pix = pix.scaled(lb.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # lb.setPixmap(pix)
        # lb.setAlignment(Qt.AlignCenter)
        self.setObjectName('w')
        # self.setStyleSheet('#w{background-image:url(./res/background/bk1.jpg);} /*  */')
        lv = QVBoxLayout(self)
        pb = QPushButton('试看天下')
        lv.addWidget(pb)

    def __str__(self):
        return '1'

    __repr__ = __str__

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super(MainWin, self).resizeEvent(a0)
        # Utils.setBg(self, self.lb_bg, './res/background/bk2.jpg')
        self.lb_bg.setAlignment(Qt.AlignCenter)
        self.lb_bg.resize(self.width(), self.height())
        pix = Utils.img_center(self.lb_bg.width(), self.lb_bg.height(),
                              './res/background/bk1.jpg')
        # print('here',type(pix))
        self.lb_bg.setPixmap(pix)

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
    sys.exit(app.exec_())
