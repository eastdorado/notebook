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
        Utils.set_effect(self.lb_bg, 0, 10, QGraphicsBlurEffect.QualityHint)
        # lb.resize(800, 600)
        # self.effect(lb)

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

    # 把图片按比例全部显示出来，不遮蔽，且居中，最大化
    @staticmethod
    def show_center_img(win, label, file):
            img = QImage(file)
            sw, sh = win.width(), win.height()
            ratio_w = img.width() / sw
            ratio_h = img.height() / sh

            is_w = True if ratio_w > ratio_h else False
            # print(sw, sh, is_w)

            img_new = img.scaledToWidth(sh) if is_w else img.scaledToHeight(sw)
            # img_new = img.scaled(sw, sh, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # print(img_new.size(), img.size())

            label.setPixmap(QPixmap.fromImage(img_new))
            # label.setAlignment(Qt.AlignCenter)

    @staticmethod
    def get_center_image(w_win, h_win, img_file='./res/background/bk1.jpg'):
        img = Image.open(img_file)

        h_img = img.size[1]  # 图片高度
        w_img = img.size[0]  # 图片宽度

        ratio_w = w_img / w_win
        ratio_h = h_img / h_win

        # 开始截取
        region = None
        if ratio_w < ratio_h:
            # img.thumbnail(int(w_img * ratio_w), int(h_img * ratio_w))  # 只能缩小自身
            new_img = img.resize((int(w_img * ratio_w), int(h_img * ratio_w)))
            # region = new_img.crop([0, (h_img * ratio_w - h_win) // 2, w_win, h_win])
        else:
            new_img = img.resize((int(w_img * ratio_h), int(h_img * ratio_h)))  # 缩放
            # region = new_img.crop([(w_img * ratio_h - w_win) // 2, 0, w_win, h_win])
        # print(type(region))
        pix = ImageConvert.get_QPixmap_Image(new_img)
        print(type(pix))
        # 保存图片
        # region.save("test.jpg")
        return pix

    def __str__(self):
        return '1'

    __repr__ = __str__

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super(MainWin, self).resizeEvent(a0)
        Utils.setBg(self, self.lb_bg, './res/background/bk2.jpg')

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
