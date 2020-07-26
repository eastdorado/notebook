#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Project: PyCharm
# @File    : mahjong.py
# @Author  : tiger
# @Email   : shdorado@126.com
# @Time    : 2020/5/22 0:14

# from gevent import monkey
#
# monkey.patch_all()  # 必须放到被打补丁者的前面，如time，socket模块之前# 必须写在最上面，这句话后面的所有阻塞全部能够识别了
# import gevent#协程
# from gevent.pool import Pool
# from functools import partial
# from multiprocessing import Process#进程
import threading  # 线程

import sys
import os
import random
from utilities import Utils
import win32api

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PIL import Image, ImageQt
# from PIL.ImageQt import ImageQt
import numpy as np
import time
from custTitle import FrameLessWindow


# 多进程+协程。4个玩家的智能算法用4个进程，充分利用多cpu，
# 杠碰、吃胡等用多协程实现。
# COROUTINE_NUMBER = 2000  # 协程池数量
# pool = Pool(COROUTINE_NUMBER)  # 使用协程池


class DataMj(object):
    LINE = str(sys._getframe().f_lineno)

    # self.tiles_dot = []  # 饼子
    # self.tiles_bamboo = []  # 条子
    # self.tiles_character = []  # 万子
    # self.tiles_wind = ['东风', '南风', '西风', '北风']    # 番子： the honor tiles (dragon+wind)
    # self.tiles_dragon = ['红中', '发财', '白板']  # 中发白：red dragon、green dragon、white dragon
    # self.tiles = (11, 12, 13, 14, 15, 16, 17, 18, 19,  # 万 各4张
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,  # 饼 各4张
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,  # 条 各4张
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               41, 42, 43, 44, 45, 46, 47,  # 东南西北 中发白 各4张
    #               41, 42, 43, 44, 45, 46, 47,
    #               41, 42, 43, 44, 45, 46, 47,
    #               41, 42, 43, 44, 45, 46, 47,
    #               51, 52, 53, 54, 55, 56, 57, 58)  # 春夏秋冬，梅兰菊竹 各1张
    # 数据格式:类型=value/10, 数值=value%10
    # self.majmap = {"0": "一万", "1": "二万", "2": "三万", "3": "四万", "4": "五万",
    #                "5": "六万", "6": "七万", "7": "八万", "8": "九万",
    #                "10": "一饼", "11": "二饼", "12": "三饼", "13": "四饼", "14": "五饼",
    #                "15": "六饼", "16": "七饼", "17": "八饼", "18": "九饼",
    #                "20": "一条", "21": "二条", "22": "三条", "23": "四条", "24": "五条",
    #                "25": "六条", "26": "七条", "27": "八条", "28": "九条",
    #                "30": "东风", "31": "南风", "32": "西风", "33": "北风", "34": "红中",
    #                "35": "发财", "36": "白板",
    #                "40": "春", "41": "夏", "42": "秋", "43": "冬", "44": "梅",
    #                "45": "兰", "46": "菊", "47": "竹"}
    g_tiles_ID = (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,  # 万
                  0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                  0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                  0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,  # 筒
                  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
                  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
                  0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
                  0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,  # 条
                  0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
                  0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
                  0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
                  0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,  # 东南西北，中发白
                  0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,
                  0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,
                  0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,
                  0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47)  # 春夏秋冬，梅兰菊竹
    g_tiles_name = ("一万", "二万", "三万", "四万", "五万", "六万", "七万", "八万", "九万",
                    "一饼", "二饼", "三饼", "四饼", "五饼", "六饼", "七饼", "八饼", "九饼",
                    "一条", "二条", "三条", "四条", "五条", "六条", "七条", "八条", "九条",
                    "东风", "南风", "西风", "北风", "红中", "发财", "白板", None, None,
                    "春", "夏", "秋", "冬", "梅", "兰", "菊", "竹")

    _g_pic_path = 'E:/python/games/res/img_match'
    g_tiles_pic = ('character1.png', 'character2.png', 'character3.png', 'character4.png', 'character5.png',
                   'character6.png', 'character7.png', 'character8.png', 'character9.png',
                   'dot1.png', 'dot2.png', 'dot3.png', 'dot4.png', 'dot5.png',
                   'dot6.png', 'dot7.png', 'dot8.png', 'dot9.png',
                   'bamboo1.png', 'bamboo2.png', 'bamboo3.png', 'bamboo4.png', 'bamboo5.png',
                   'bamboo6.png', 'bamboo7.png', 'bamboo8.png', 'bamboo9.png',
                   'windEast.png', 'windSouth.png', 'windWest.png', 'windNorth.png',
                   'dragonRed.png', 'dragonGreen.png', 'dragonWhite.png', ' ', ' ',
                   'flower1', 'flower2', 'flower3', 'flower4', 'flower5', 'flower6', 'flower7', 'flower8')

    # _g_pic_path = 'E:/python/games/res/ma_yellow'
    # g_tiles_pic = ('man1.png', 'man2.png', 'man3.png', 'man4.png', 'man5.png',
    #                'man6.png', 'man7.png', 'man8.png', 'man9.png',
    #                'dot1.png', 'dot2.png', 'dot3.png', 'dot4.png', 'dot5.png',
    #                'dot6.png', 'dot7.png', 'dot8.png', 'dot9.png',
    #                'pin1.png', 'pin2.png', 'pin3.png', 'pin4.png', 'pin5.png',
    #                'pin6.png', 'pin7.png', 'pin8.png', 'pin9.png',
    #                'wind-east.png', 'wind-south.png', 'wind-west.png', 'wind-north.png',
    #                'dragon-chun.png', 'dragon-green.png', 'dragon-haku.png', ' ', ' ',
    #                'season-spring.png', 'season-summer.png', 'season-autumn.png', 'season-winter.png',
    #                'flower-plum.png', 'flower-orchid.png', 'flower-chrysanthemum.png', 'flower-bamboo.png')

    # _g_pic_path = 'E:/python/games/res/ma_gray'
    # g_tiles_pic = ('character_1.png', 'character_2.png', 'character_3.png', 'character_4.png', 'character_5.png',
    #                'character_6.png', 'character_7.png', 'character_8.png', 'character_9.png',
    #                'circle_1.png', 'circle_2.png', 'circle_3.png', 'circle_4.png', 'circle_5.png',
    #                'circle_6.png', 'circle_7.png', 'circle_8.png', 'circle_9.png',
    #                'bamboo_1.png', 'bamboo_2.png', 'bamboo_3.png', 'bamboo_4.png', 'bamboo_5.png',
    #                'bamboo_6.png', 'bamboo_7.png', 'bamboo_8.png', 'bamboo_9.png',
    #                'wind_east.png', 'wind_south.png', 'wind_west.png', 'wind_north.png',
    #                'dragon_red.png', 'dragon_green.png', 'dragon_white.png', ' ', ' ',
    #                'season_spring.png', 'season_summer.png', 'season_autumn.png', 'season_winter.png',
    #                'flower_plum.png', 'flower_orchid.png', 'flower_chrysanthemum.png', 'flower_bamboo.png')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 项目根目录

    @staticmethod
    def write_log(content, colour='white', skip=False):
        """
        写入日志文件
        :param content: 写入内容
        :param colour: 颜色
        :param skip: 是否跳过打印时间
        :return:
        """
        # 颜色代码
        colour_dict = {
            'red': 31,  # 红色
            'green': 32,  # 绿色
            'yellow': 33,  # 黄色
            'blue': 34,  # 蓝色
            'purple_red': 35,  # 紫红色
            'bluish_blue': 36,  # 浅蓝色
            'white': 37,  # 白色
        }
        choice = colour_dict.get(colour)  # 选择颜色

        path = os.path.join(DataMj.BASE_DIR, "/res/output_1.log")  # 日志文件
        print(DataMj.BASE_DIR, path)
        with open(path, mode='a+', encoding='utf-8') as f:
            if skip is False:  # 不跳过打印时间时
                content = time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + content

            info = "\033[1;{};1m{}\033[0m".format(choice, content)
            print(info)
            f.write(content + "\n")

    @staticmethod
    def bubble_sort(arr, left=None, right=None):  # 冒泡排序
        if not isinstance(arr, list):
            return

        lenth = len(arr)
        if lenth < 2:
            print(str(sys._getframe().f_lineno), 'error')
            return

        left = 0 if not isinstance(left, (int, float)) else left
        right = lenth if not isinstance(right, (int, float)) else right

        left = 0 if left < 0 else (lenth if left > lenth else left)
        right = 0 if right < 0 else (lenth if right > lenth else right)

        if left == right:
            return

        if left > right:
            left, right = right, left

        # print(left, right)

        for i in range(left + 1, right):
            for j in range(left, right - i):
                if arr[j].ID > arr[j + 1].ID:
                    arr[j].index, arr[j + 1].index = arr[j + 1].index, arr[j].index
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    # sys.setrecursionlimit(100000)  # 例如这里设置递归深度为十万
    @staticmethod
    def quick_sort_card(arr, left=None, right=None):
        if not isinstance(arr, list):
            return

        lenth = len(arr)
        if lenth < 2:
            print(str(sys._getframe().f_lineno), 'error')
            return

        left = 0 if not isinstance(left, (int, float)) else left
        right = lenth - 1 if not isinstance(right, (int, float)) else right

        left = 0 if left < 0 else (lenth - 1 if left >= lenth else left)
        right = 0 if right < 0 else (lenth - 1 if right >= lenth else right)

        if left == right:
            return

        if left > right:
            left, right = right, left

        partitionIndex = DataMj.partition(arr, left, right)
        DataMj.quick_sort_card(arr, left, partitionIndex - 1)
        DataMj.quick_sort_card(arr, partitionIndex + 1, right)

        return arr

    @staticmethod
    def partition(arr, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if arr[i].ID < arr[pivot].ID:
                DataMj.swap_it(arr, i, index)
                index += 1
            i += 1
        DataMj.swap_it(arr, pivot, index - 1)

        return index - 1

    @staticmethod
    def swap_it(arr, i, j):
        arr[i].index, arr[j].index = arr[j].index, arr[i].index
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def get_name_pic(ID):
        """
        根据ID获得麻将牌的名称与图片文件名称
        :param ID:
        :return: [名称，文件名]
        """

        ret = None
        index = DataMj.value2index(ID)

        if 0 <= index < 44:
            if index == 34 or index == 35:  # 补位的不算
                return ret, ret

            name = DataMj.g_tiles_name[index]
            file = None
            kind = (index // 9)
            value = (index % 9) + 1
            if kind == 0:
                file = ''.join(['character', str(value), '.png'])
            elif kind == 1:
                file = ''.join(['dot', str(value), '.png'])
            elif kind == 2:
                file = ''.join(['bamboo', str(value), '.png'])
            elif kind == 3:
                tmp = ('windEast.png', 'windSouth.png', 'windWest.png', 'windNorth.png',
                       'dragonRed.png', 'dragonGreen.png', 'dragonWhite.png')
                file = tmp[value - 1]
            else:  # 春、夏、秋、冬、梅、兰、竹、菊
                file = ''.join(['flower', str(value), '.png'])

            file = os.path.join(DataMj._g_pic_path, file)
            file = file.replace('\\', '/')

            return name, file

        else:
            return ret, ret

    # 判断是否有效
    @staticmethod
    def is_valid(ID):
        itype = ID >> 4
        value = ID & 0x0F
        # print(itype, value)
        if itype == 0 or itype == 1 or itype == 2:
            if 0 <= value < 9:
                return True
            else:
                return False
        elif itype == 3:
            if 0 <= value < 7:
                return True
            else:
                return False
        elif itype == 4:
            if 0 <= value < 8:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def value2index(ID):
        """
        牌 ID变成 name和 pic的索引
        :param ID:
        :return:
        """
        index = -1
        value = ID & 0x0F

        if ID < 0x31:
            color = ID >> 4
            index = color * 9 + value  # * 9
            # index = (color << 3) + color + value  # * 9
        elif ID < 0x41:
            index = 27 + value
        elif ID < 0x47:
            index = 34 + value

        # print(ID, index)
        return index

    @staticmethod
    def index2value(index):
        ID = ((index // 9) << 4) | (index % 9)
        return ID

    @staticmethod
    def sortArray(arr):
        if not isinstance(arr, list) or len(arr) == 0:
            return
        arr.sort(key=(lambda x: x[0]))  # 对二维列表进行排序,按第一项

    # QPixmap格式转PIL格式
    @staticmethod
    def pixmap2pil(self, pixmap):
        # print("QPixmap格式转PIL格式")
        return ImageQt.fromqpixmap(pixmap)

    # PIL格式转QPixmap格式
    @staticmethod
    def pil2pixmap(pil_img):
        # print("PIL格式转QPixmap格式")
        return ImageQt.toqpixmap(pil_img)
        # return QtGui.QPixmap.fromImage(ImageQt(pil_img))

    # PIL格式转QPixmap格式
    # @staticmethod
    # def pil2_pixmap(pil_img):
    #     # print("PIL格式转QPixmap格式")
    #     return ImageQt.toqpixmap(pil_img)

    @staticmethod
    def alpha2white_opencv2(imgfile):
        """
        将图片透明背景转换成白色背景-opencv2实现
        :return:
        """
        try:
            img = cv2.imread(imgfile, -1)
            img_copy = img.copy()  # 注意：这里copy()，避免覆盖原img

            sp = img_copy.shape
            width = sp[0]
            height = sp[1]
            for yh in range(height):
                for xw in range(width):
                    color_d = img[xw, yh]
                    if color_d[3] == 0:
                        img[xw, yh] = [229, 229, 229, 255]

            cv2.imwrite("./res/img_match/Mask.png", img)
            # cv2.imshow("after", img)
            # cv2.waitKey(0)
            return img
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def alphabg2white_PIL(imgfile):
        """
        将图片透明背景转换成白色背景-PIL实现
        :param imgfile:
        :return:
        """
        try:
            img = Image.open(imgfile)
            img = img.convert('RGBA')
            sp = img.size
            width = sp[0]
            height = sp[1]
            # print(sp)
            for yh in range(height):
                for xw in range(width):
                    dot = (xw, yh)
                    color_d = img.getpixel(dot)
                    if color_d[3] == 0:
                        color_d = (255, 255, 255, 255)
                        img.putpixel(dot, color_d)
            # img.show()
            return img
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def qtpixmap_to_cvimg(qtpixmap):
        """
        QPixmap转opencv
        :param qtpixmap:
        :return:
        """
        qimg = qtpixmap.toImage()
        temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
        temp_shape += (4,)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
        result = result[..., :3]

        return result

    @staticmethod
    def cvimg_to_qtimg(cvimg):
        """
        opencv转QImage
        :param cvimg:
        :return:
        """
        imgDown = np.float32(cvimg)
        height, width, depth = imgDown.shape
        bytesPerLine = 3 * width
        cvimg = cv2.cvtColor(imgDown, cv2.COLOR_BGR2RGB)
        tempImage = QtGui.QImage(cvimg.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        # print(type(tempImage))
        # tempImage = QtGui.QPixmap.toImage()  # QPixmap->QImage
        tempPixmap = QtGui.QPixmap.fromImage(tempImage)  # QImage->QPixmap
        # tempPixmap = QtGui.QPixmap(tempImage)
        # print(type(tempPixmap))

        return tempPixmap


class Tile(QtWidgets.QFrame):
    _W, _H = 30, 40
    _s1, _s2, _s3 = 2.3, 2.1, 2
    g_W, g_H = _W * _s1, _H * _s1  # 普通牌的width, height
    g_W_d, g_H_d = _W * _s2, _H * _s2  # 叫牌的宽高
    g_W_s, g_H_s = _W * _s3, _H * _s3  # 废牌的宽高

    def __init__(self, parent=None, ID=0, kind=1, index=-1):
        """
        卡牌
        :param parent:
        :param ID: 牌号
        :param kind: 每家的正牌 —— 0：东方牌 1:南方牌、影子牌 2:西方牌 3:北方牌
                     每家的叫牌(第14张牌) —— 4:东 5 6 7北
                    每家的明牌 ——   8:东方 9:南方卧牌 10 11
                    每家的死牌 —— 12:东方 13:南方 14:西方 15:北方
        :param index: 牌的槽位，在牌面中的位置，回传用
        """
        # 加一个suppress规则:
        # noinspection PyArgumentList
        super(Tile, self).__init__(parent)

        self.parent = parent
        self.ID = ID
        self.kind = kind
        self.index = index
        self.is_ejected = False  # 弹出标志
        self.lb = QtWidgets.QLabel(self)

        self._create()
        self.setVisible(False)

    def _create(self):
        self.lb.setScaledContents(True)  # 让图片自适应label大小
        name, pic_file = DataMj.get_name_pic(self.ID)

        if self.kind == 0:
            self.setFixedSize(30, 80)
            pic_file = './res/images/tile_right.png'
            self.lb.setGeometry(0, 0, self.width(), self.height())
            self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)  # 事件穿透，鼠标不起作用

            # tmp = self.alphabg2white_PIL(self.pic_file)
            # bg = self.pil2pixmap(tmp)
            # bg = QtGui.QPixmap.fromImage(bg1)

            # bg = Image.open(pic_file).transpose(Image.ROTATE_270)
            # # DataMj.pil2_pixmap(bg)
            # lb.setPixmap(bg.scaled(width+10, height+60, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 1:
            self.setMouseTracking(True)  # 跟踪鼠标移动
            self.setFixedSize(Tile.g_W, Tile.g_H)
            self.lb.setGeometry(7, 25, int(Tile.g_W * 0.8), int(Tile.g_H * 0.7))
            self.lb.setMouseTracking(True)  # 跟踪鼠标移动
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 2:
            self.setFixedSize(30, 80)
            pic_file = './res/images/tile_left.png'
            self.lb.setGeometry(0, 0, self.width(), self.height())
            self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)  # 事件穿透，鼠标不起作用
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 3:
            self.setFixedSize(65, 85)
            pic_file = './res/images/tile_top.png'
            # self.setFixedSize(80, 85)
            # pic_file = r'E:\python\games\res\ma_yellow\face-down-128px.png'
            self.lb.setGeometry(0, 0, self.width(), self.height())
            self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)  # 事件穿透，鼠标不起作用
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 4:  # 东方叫牌
            self.setFixedSize(Tile.g_H_d * 0.9, Tile.g_W_d * 1.1)
            self.lb.setGeometry(6, 5, int(Tile.g_H_d * 0.9 * 0.8), int(Tile.g_W_d * 0.7))

            if pic_file:
                im = Image.open(pic_file)
                out = im.transpose(Image.ROTATE_90)  # 逆时针旋转 90
                # img = im.resize(100, 100)  # 将图片重新设置尺寸
                # out.save('./tmp.png')
                self.lb.setPixmap(DataMj.pil2pixmap(out))

        elif self.kind == 5:  # 南方叫牌
            self.setFixedSize(Tile.g_W_d, Tile.g_H_d)
            self.lb.setGeometry(7, 7, int(Tile.g_W_d * 0.8), int(Tile.g_H_d * 0.65))

            if pic_file:
                # im = Image.open(pic_file)
                # out = im.transpose(Image.FLIP_TOP_BOTTOM)  # 进行上下颠倒
                self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 6:  # 西方叫牌
            self.setFixedSize(Tile.g_H_d * 0.9, Tile.g_W_d * 1.1)
            self.lb.setGeometry(6, 5, int(Tile.g_H_d * 0.9 * 0.8), int(Tile.g_W_d * 0.7))

            if pic_file:
                im = Image.open(pic_file)
                out = im.transpose(Image.ROTATE_270)  # 逆时针旋转 270
                self.lb.setPixmap(DataMj.pil2pixmap(out))

        elif self.kind == 7:  # 北方叫牌 即正打出的第14张牌
            self.setFixedSize(Tile.g_W_d, Tile.g_H_d)
            self.lb.setGeometry(7, 7, int(Tile.g_W_d * 0.8), int(Tile.g_H_d * 0.65))

            if pic_file:
                im = Image.open(pic_file)
                out = im.transpose(Image.FLIP_TOP_BOTTOM)  # 进行上下颠倒
                self.lb.setPixmap(DataMj.pil2pixmap(out))

        elif self.kind == 8:
            self.setFixedSize(Tile.g_W_s * 0.75, Tile.g_H_s * 0.75)
            pic_width, pic_height = int(Tile.g_W_s * 0.75 * 0.8), int(Tile.g_H_s * 0.75 * 0.7)
            self.lb.setGeometry(5, 5, pic_width, pic_height)
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

        elif self.kind == 9:
            self.setFixedSize(Tile.g_tile_height * 0.75, Tile.g_tile_width * 0.75)
            pic_width, pic_height = int(Tile.g_width * 0.75 * 0.8), int(Tile.g_height * 0.75 * 0.7)
            self.lb.setGeometry(5, 5, pic_height, pic_width)
            self.lb.setPixmap(QtGui.QPixmap(pic_file))

    def resurfacing(self, ID, kind=5):
        """
        相当于摸了一张牌到热牌位置
        更换皮肤和牌号，槽位不变。仅针对热牌和影子牌，其他牌建议用互换法
        :param kind:
        :param ID: 要复制的牌卡牌号
        :return:
        """

        if DataMj.is_valid(ID):
            pic_file = DataMj.get_name_pic(ID)[1]
            if pic_file:
                if kind == 4:  # 东方叫牌
                    im = Image.open(pic_file)
                    out = im.transpose(Image.ROTATE_90)  # 逆时针旋转 90
                    self.lb.setPixmap(DataMj.pil2pixmap(out))
                # elif kind == 5:
                #     self.lb.setPixmap(QtGui.QPixmap(pic_file))
                elif kind == 6:
                    im = Image.open(pic_file)
                    out = im.transpose(Image.ROTATE_270)  # 逆时针旋转 270
                    self.lb.setPixmap(DataMj.pil2pixmap(out))
                elif kind == 7:
                    im = Image.open(pic_file)
                    out = im.transpose(Image.FLIP_TOP_BOTTOM)  # 进行上下颠倒
                    self.lb.setPixmap(DataMj.pil2pixmap(out))
                else:
                    self.lb.setPixmap(QtGui.QPixmap(pic_file))

                self.lb.repaint()
                self.ID = ID

    def release_me(self):
        self.lb.deleteLater()
        self.deleteLater()

    def mousePressEvent(self, e):
        # print('mousePress')
        if not self.parent.can_discard:  # 禁止打牌
            return

        if not self.is_ejected:  # 弹起来，提示预计要打的牌
            name = DataMj.get_name_pic(self.ID)[0]
            # print(str(sys._getframe().f_lineno), name, self.index)

            tile = self.parent.tile_ejected  # 原来弹起的要归位
            if tile:
                tile.move(tile.x(), tile.y() + 50)
                tile.is_ejected = False
            self.parent.tile_ejected = self  # 当下的要弹起
            self.move(self.x(), self.y() - 50)
            self.is_ejected = True
        else:  # 弹起时点击，就出牌了
            self.move(self.x(), self.y() + 50)
            self.is_ejected = False
            self.parent.tile_ejected = None

            self.parent.discard(self)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        pic = None

        if self.kind == 1:
            pic = './res/images/tile_bottom.png'
        elif self.kind == 4 or self.kind == 6:
            pic = './res/images/tile_hot_h.png'
        elif self.kind == 5 or self.kind == 7:
            pic = './res/images/tile_hot_v.png'

        qp.begin(self)
        # qp.drawPixmap(self.rect(), QtGui.QPixmap(self.pic_file), QtCore.QRect())
        qp.drawPixmap(self.rect(), QtGui.QPixmap(pic), QtCore.QRect())
        # qp.setBrush(QtGui.QColor(10, 10, 10))

        qp.end()

    def __str__(self):
        return f'牌{self.index}: {DataMj.get_name_pic(self.ID)}'

    __repr__ = __str__
    '''
    __repr__ = __str__ 使用时可保证在控制台>>> m 时 任然输出
    Information: name:wang,number:3000
    '''


class Mahjong(QtWidgets.QFrame):
    def __init__(self, parent=None):
        # noinspection PyArgumentList
        super(Mahjong, self).__init__(parent)
        self.parent = parent

        # 牌桌的设置参数
        self.w_border = 5
        self.w_middle = 5
        self.margin = self.w_border * 2 + self.w_middle

        # 牌局的总体参数
        self.tiles_count = 136  # 麻将牌的总数 144, 136, 108
        self.delay = 10  # 叫牌后的停顿时间
        self.players = ('东方', '南方', '西方', '北方')
        self.dealer = 1  # 庄家方位 0：东 1：南，1始终是本家，
        self.dice = 99  # 骰子  points 点数    cheat 抽老千
        self.lots = 0  # 出牌的手数，可以判断各人打出的牌数
        self.speaker = self.dealer  # 目前的出牌者

        self.oker = None  # 鬼牌，钻石牌
        self.tile_ejected = None  # 弹起的牌
        self.tile_shadow = None  # 本家叫/热牌的影子牌

        self.begin = True
        self.isWin = False  # 已胡牌
        self.can_discard = False  # 本家可以出牌否

        # self.id_discarded = 0  # 打出的牌在队列中的序号

        # 数据区
        self.round = []  # 一圈/一局的暗牌, 仅有牌号和标志位(0:正常 1:明牌 2:牌卡弹出)
        self.card_players = [[0] * 14 for i in range(4)]  # 四家的牌面，每张牌含牌号、翻牌等标志、控件
        self.card_ground = [[0], [0], [0], [0]]  # 四家落地牌，各家桌上废牌

        self.para = [10, 2, 1]  # 计算每张牌的分值
        self.scale = 50

        # 功能区
        self.event_discarded = threading.Event()  # 出牌信号
        self.event_can_draw = threading.Event()  # 摸牌信号
        """
        Event用法：
        event = threading.Event()  # 设置一个事件实例
        event.set()  # 设置标志位     放开通道
        event.clear()  # 清空标志位      关闭通道
        event.wait()  # 等待设置标志位    if event.is_set()开通 …… else …… 阻塞了：通道被关，等待开启
        """

        self.init_board()
        self.shuffling()
        self.deal()
        tmp = []
        # for i in range(4, -10, -1):
        #     tmp.append((i, i % 4))
        # print(tmp)

    def init_board(self):
        # 仅设置桌面
        # self.resize(self.parent.width(), self.parent.height())
        self.setLineWidth(self.w_border)
        self.setMidLineWidth(self.w_middle)
        self.setFrameStyle(QtWidgets.QFrame.Raised | QtWidgets.QFrame.Box)
        # self.setFrameRect(QtCore.QRect(10, 10, 80, 80))

        # self.setMouseTracking(True)  # 跟踪鼠标移动
        # self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.setStyleSheet('background-image:url(./res/images/mahjongdesk2.jpg)')
        # self.setStyleSheet('background-color:#CC6600')  # Tan
        self.setStyleSheet('background-color:blue')  # Tan

        lb = QtWidgets.QLabel(self)
        # lb.setPixmap(QtGui.QPixmap('./res/images/mahjongdesk.jpg'))
        lb.setScaledContents(True)  # 让图片自适应label大小

        ml = QtWidgets.QVBoxLayout(self)
        ml.setContentsMargins(0, 0, 0, 0)
        # noinspection PyArgumentList
        ml.addWidget(lb)

    # 洗牌，砌牌，全部 ID
    def shuffling(self):
        self.round.clear()

        for i in range(self.tiles_count):
            index = Utils.rand_int(0, self.tiles_count - 1)
            self.round.append(DataMj.g_tiles_ID[index])

        # self.round.extend(DataMj.g_tiles_ID[0:self.tiles_count])
        # print(self.round)
        # print(len(DataMahjong.g_tiles_ID), len(self.round))
        # i = 3
        # while i > 0:
        #     random.shuffle(self.round)
        #     i = i - 1
        # print(self.round)

    # 起牌
    # def deal(self):
    #     if self.tiles_count < 53:  # 不够起牌的
    #         return
    #
    #     self.dealer %= 4  # 4人麻将轮流坐庄
    #
    #     # 庄家掷骰子找到二次掷骰人，并确定开门方向
    #     # die1 = random.randint(1, 12)
    #     die1 = Utils.rand_int(1, 12)
    #     door = (self.dealer + die1 - 1) % 4  # 开门方向
    #     # 二次掷骰子
    #     # die2 = random.randint(1, 12)
    #     die2 = Utils.rand_int(1, 12)
    #     dice = (door + 1) * 34 - die2 * 2
    #     # zero = dice % self.tiles_count      # 开始摸牌的位置
    #     new_round = self.round[dice:]
    #     new_round.extend(self.round[:dice])
    #     self.round = new_round  # 重新起算
    #     # print(len(self.round))
    #
    #     self.lots = 0
    #     # 给玩家发牌
    #     for k in range(3):  # 发三次牌，每人每次拿连续的4张
    #         for i in range(4):
    #             player_id = (i + self.dealer) % 4  # 循环坐庄
    #             for j in range(4):
    #                 # 牌号、牌卡控件、翻牌等标志
    #                 ID = self.round[self.lots]  # 牌号，兼做排序用
    #                 index = j + 4 * k  # 槽位
    #                 # player_id 也代表卡牌类型
    #                 self.card_players[player_id][index] = Tile(self, ID, player_id, index)
    #                 self.lots += 1
    #                 # print(DataMj.get_name_pic(ID)[0], index)
    #
    #     # 每人再模一张，叫牌空置
    #     for i in range(4):
    #         player_id = (i + self.dealer) % 4  # 从庄家的下家开始
    #         self.card_players[player_id][12] = Tile(self, self.round[self.lots], player_id, 12)
    #         self.lots += 1
    #         self.card_players[player_id][13] = Tile(self, 999, 4 + player_id, 13)  # 叫牌，确保排在最后，每台不用清零
    #
    #     self.tile_shadow = Tile(self, 999, 1, 13)  # 把影子牌实例化
    #
    #     # self.print_card(1)
    #     for i in range(4):
    #         # DataMj.bubble_sort(self.card_players[i])  # 每家牌卡都排序好
    #         DataMj.quick_sort_card(self.card_players[i])  # 每家牌卡都排序好
    #     # self.print_card(1)
    #     # print(self.card_players[self.dealer][-1])
    #
    #     self.startover()

    # 开启打牌的各种线程了
    def startover(self):
        self.event_can_draw.set()
        self.event_discarded.clear()
        drawing = threading.Thread(target=self.draw, )  # 进程1，等待进程2完成
        drawing.start()

        checking = threading.Thread(target=self.Win_Pung_Kong_Chow, )  #
        checking.start()

    # 摸牌
    def draw(self):
        """
            检测到哪家摸牌了，接着叫牌，也就是出牌
            :return:
            """

        while True:
            if self.lots >= self.tiles_count or self.isWin:  # 荒牌或胡牌
                break

            if not self.event_can_draw.is_set():
                self.event_can_draw.wait()
            else:
                ground_tiles = self.lots - 52  # 已经打出的落地牌的数量，包括当前的叫牌
                print(f'{self.speaker}摸牌, 地牌数:{ground_tiles}')
                # DataMj.write_log(string, 'red')

                if self.speaker == 1:  # 显示本家的影子牌
                    self.card_players[1][13].resurfacing(self.round[self.lots], 5)  # 真身进张
                    self.lots += 1  # 进张了
                    self.tile_shadow.resurfacing(self.card_players[1][13].ID, 5)  # 影子深拷贝一份
                    self.tile_shadow.setVisible(True)
                    self.can_discard = True  # 可以出牌了，等待本家脑袋算法选择后，鼠标触发 出牌
                    self.event_can_draw.clear()
                else:  # 其他家智能出牌
                    self.card_players[self.speaker][13].resurfacing(self.round[self.lots], 4 + self.speaker)
                    self.lots += 1  # 进张了

                    self.collect_melds()  # 这里要经过算法处理，看是否听、胡，或者出牌，打出的应该是废张，而非简单的进牌

                    self.card_players[self.dealer][13].setVisible(True)  # 亮 13牌即等于出13牌
                    self.event_discarded.set()  # 叫醒 胡对杠吃 程序

    # 本家出牌
    def discard(self, tile):
        if not tile or not self.can_discard:
            print(str(sys._getframe().f_lineno), "discard error")
            return
        # print(tile)
        ID_src, index_src = tile.ID, tile.index

        if index_src < 13:  # 叫牌摸到即扔，不插入排序
            hot_ID = self.card_players[1][13].ID  # 叫牌的
            # tile.resurfacing(hot_ID)
            self.swap_tiles(tile, self.tile_shadow)  # 先把影子牌置换掉,影子代替叫牌，不影响热牌
            # 再重新排序
            if tile.ID == hot_ID:
                pass
            elif tile.ID > hot_ID:  # 左边插入
                if index_src == 0:  # 边缘的直接替换
                    pass
                else:
                    for i in range(index_src, 0, -1):
                        if self.card_players[1][i].ID < self.card_players[1][i - 1].ID:
                            self.swap_tiles(self.card_players[1][i], self.card_players[1][i - 1])
                        else:
                            break
            else:  # 右边插入
                if index_src == 12:  # 边缘的直接替换
                    pass
                else:
                    for i in range(index_src, 12):
                        if self.card_players[1][i].ID > self.card_players[1][i + 1].ID:
                            self.swap_tiles(self.card_players[1][i], self.card_players[1][i + 1])
                        else:  # 就地扎根
                            break

        self.tile_shadow.setVisible(False)  # 藏影子
        self.card_players[1][13].setVisible(True)  # 现真身 亮牌即出牌
        self.can_discard = False  # 不能再出牌了

        self.event_discarded.set()  # 叫醒点炮检测程序

    # 凑牌成组 把各家牌整成顺子、刻子或杠子
    def collect_melds(self):
        pass

    # 上家叫牌后, 胡？碰？杠？吃？
    def Win_Pung_Kong_Chow(self):
        """
        这里要找到上家出的叫牌，然后逐一经过算法处理，杠、碰、吃、胡等
        :return:
        """

        while True:
            if self.lots >= self.tiles_count or self.isWin:  # 荒牌或胡牌
                break

            if not self.event_discarded.is_set():
                self.event_discarded.wait()
            else:
                # 先轮流看另外3家要不要这张牌
                print(self.lots, 'lots')
                # discarder = (self.dealer - self.lots) % 4  # 即将出牌者  负数取模也正好符合 逆时针转
                left_speaker = (self.speaker + 1) % 4  # 上家 opponent on the left  顺时针前进一位
                hot = self.card_players[left_speaker][13]  # 上家的出牌
                print(f'现在轮到{self.players[self.speaker]}({self.speaker})摸牌。'
                      f'上家{self.players[left_speaker]}({left_speaker})出牌:{DataMj.get_name_pic(hot.ID)[0]}')

                hot.setVisible(False)  # 隐藏上家的叫牌

                if self.Win(hot.ID):  # 胡？
                    # 结束
                    # self.begin = False
                    self.isWin = True
                    self.event_can_draw.clear()
                    self.event_discarded.clear()

                ret = self.Pung(hot.ID)
                if ret[0]:  # 碰？
                    # 明牌，并接着发牌
                    self.speaker = ret[1]
                else:
                    ret = self.Kong(hot.ID)
                    if ret[0]:  # 杠？
                        self.speaker = ret[1]
                    else:
                        ret = self.Kong(hot.ID)
                        if ret[0]:  # 吃？
                            self.speaker = ret[1]
                        else:  # 都不要则是废牌，扔到地上
                            # self.killer(hot.ID, self.speaker + 12)
                            # print('hhhh')
                            self.speaker = (self.speaker + 3) % 4  # 该下一家出牌了

                            self.event_can_draw.set()  # 设置摸牌信号
                            self.event_discarded.clear()  # 清除已出牌信号

                # time.sleep(1)  # 每秒扫描一次
                # 检测天胡的存在
                # self.can_discard = True  # 14张，可以出牌了

    # 和、胡
    def Win(self, hot_ID):
        # print("胡")

        "TO DO 线程进行算法"
        return False

    # # 胡牌，cardList: 是手上的牌，需要从小到大排列
    # def match(self, cardList, majiang=False):
    #     # 递归算法：配对成功的弹出，一直到手上牌都弹出为止
    #     if len(cardList) == 0 and majiang:
    #         return True
    #
    #     rst = False
    #     # AA
    #     if not majiang and len(cardList) >= 2 and cardList[0] == cardList[1]:
    #         list1 = [] + cardList
    #         list1.pop(0)
    #         list1.pop(0)
    #         rst = self.match(list1, True)
    #
    #     # AAA
    #     if not rst and len(cardList) >= 3 and cardList[0] == cardList[1] == cardList[2]:
    #         list1 = [] + cardList
    #         list1.pop(0)
    #         list1.pop(0)
    #         list1.pop(0)
    #         rst = self.match(list1, majiang)
    #
    #     # AAAA
    #     if not rst and len(cardList) >= 4 and cardList[0] == cardList[1] == cardList[2] == cardList[3]:
    #         list1 = [] + cardList
    #         list1.pop(0)
    #         list1.pop(0)
    #         list1.pop(0)
    #         list1.pop(0)
    #         rst = self.match(list1, majiang)
    #
    #     # ABC
    #     if not rst and len(cardList) >= 3:
    #         list1 = []
    #         a = cardList[0]
    #         b = False
    #         c = False
    #         for i in range(1, len(cardList)):
    #             if not b and cardList[i] == a + 1:
    #                 b = True
    #             elif not c and cardList[i] == a + 2:
    #                 c = True
    #             else:
    #                 list1.append(cardList[i])
    #
    #         if b and c:
    #             rst = self.match(list1, majiang)
    #
    #     return rst
    #
    # # x+/-3:0   x+/-2:10   x+/-1:20   x:100
    # # xxxx:400   xxx:300   xx:200   x x+1 x+2:130   x x+1:120   x x+2:110
    # def cardsScore(self, cards, dark):
    #     # cards：手上的牌
    #     # dark：未出现过的牌
    #     scores = []
    #
    #     for c in cards:
    #         score = 0
    #         for cc in cards:
    #             gap = abs(cc - c)
    #             if gap < 3:
    #                 score += self.para[gap] * self.scale
    #
    #         for cc in dark:  # 未出现的牌中还有比较多的A，B,那么凑出AAA或ABC牌的几率加大了
    #             gap = abs(cc - c)
    #             if gap < 3:
    #                 score += self.para[gap]
    #
    #         scores.append(score)
    #
    #     return scores

    # 碰
    def Pung(self, hot_ID):
        # print("碰")
        result = False
        next_player = self.speaker

        # for i in range(self.speaker, self.speaker-3, -1):
        #     self.print_card(i)  # self.card_players[i]
        # if # i家碰了，则返回这家的下家和True，以便从新下家开始检测，两个信号不变，继续
        # next_player = (i+3)%4
        # result = True
        ID = None  # 计算出的废牌

        return result, next_player  # 打出的废牌

    # 杠
    def Kong(self, hot_ID):
        # print("杠")
        result = False
        next_player = self.speaker

        # for i in range(self.speaker, self.speaker - 3, -1):
        #     self.print_card(i)  # self.card_players[i]
        #     # next_player = i
        # ID = None  # 计算出的废牌

        return result, next_player  # 打出的废牌

    # 吃
    def Chow(self, hot_ID):
        # print("吃")
        result = False
        next_player = self.speaker

        # for i in range(self.speaker, self.speaker - 3, -1):
        #     self.print_card(i)  # self.card_players[i]
        #     # next_player = i
        # ID = None  # 计算出的废牌

        return result, next_player  # 打出的废牌

    # 显示所有玩家的牌面
    def show_cards(self):
        for i in range(13):
            tile = self.card_players[0][i]
            if tile:
                tile.setVisible(True)
                tile.move(self.x()+self.width()-100, self.margin + 160 + i * 40)
                # tile.setGeometry(, self.margin + 40 + i * 40, tile.width(), tile.height())

            tile = self.card_players[1][i]
            if tile:
                tile.setVisible(True)
                tile.move(90 + self.margin + i * Tile.g_W, self.height() - 30 - Tile.g_H - self.margin)

            tile = self.card_players[2][i]
            if tile:
                tile.setVisible(True)
                tile.move(self.x() + 70, self.margin + 160 + i * 40)
                # tile.setGeometry(self.x() + 70, self.margin + 160 + i * 40, tile.width(), tile.height())

            tile = self.card_players[3][i]
            if tile:
                tile.setVisible(True)
                tile.move(180 + self.margin + i * 62, 30)

        # 设置各家热牌的位置和形状。
        hot = self.card_players[0][13]
        # hot.setVisible(True)
        # hot.move(940, 160)
        hot.move(self.x() + self.width() - 200, self.margin + 160)

        hot = self.card_players[1][13]
        # hot.setVisible(True)
        # hot.move(self.x()+self.width() -140, 580)
        hot.move(90 + self.margin + 13 * Tile.g_W, self.height() - 140 - Tile.g_H - self.margin)

        hot = self.card_players[2][13]
        # hot.setVisible(True)
        hot.move(self.x() + 120, self.margin + 130 + 13 * 40)

        hot = self.card_players[3][13]
        # hot.setVisible(True)
        hot.move(180 + self.margin, 125)

        # self.card_scrap.setVisible(True)
        self.tile_shadow.move(115 + self.margin + 13 * Tile.g_W, self.height() - 30 - Tile.g_H - self.margin)

    # 废牌到地上
    def killer(self, ID, kind):
        tile = Tile(self, ID, kind, 13)
        if self.speaker == 0:  # 东方
            pass
        elif self.speaker == 1:  # 南方
            # num = (self.lots - 53) // 4  # 出牌的第几圈，等于打出牌的数量轮回
            num = (self.lots - 53)  # 出牌的第几圈，等于打出牌的数量轮回 这不准确
            x, y = num % 8, num // 8
            # 移到出牌区
            tile.setGeometry(380 + x * tile.width(), 450 + y * (tile.height() - 13), tile.width(),
                             tile.height())
            tile.setVisible(True)
        # else:
        #     self.can_discard = True

    # 打印牌面
    def print_card(self, player_ID):
        if self.card_players[player_ID]:
            temp = []
            temp1 = []
            for each in self.card_players[player_ID]:
                if DataMj.is_valid(each.ID):
                    temp.append(DataMj.g_tiles_name[DataMj.value2index(each.ID)])
                    temp1.append(each.index)
            print(temp)
            print(temp1)

    def swap_tiles(self, tile_src, tile_dst):
        if not tile_dst or not tile_src:
            return

        # 先换槽位
        self.card_players[1][tile_src.index], self.card_players[1][tile_dst.index] = \
            self.card_players[1][tile_dst.index], self.card_players[1][tile_src.index]

        # 再换牌卡
        tile_src.index, tile_dst.index = tile_dst.index, tile_src.index
        sx, sy = tile_src.x(), tile_src.y()
        tile_src.move(tile_dst.x(), tile_dst.y())
        tile_dst.move(sx, sy)

    def resizeEvent(self, event):
        if not self.begin:
            return
        # self.show_owner()
        self.show_cards()
        # self.discard(self.players[1])


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # TODO(tiger) Change this to use relations
        self._setup_ui()

        # 总体框架
        hl_main = QtWidgets.QHBoxLayout(self)
        self.setLayout(hl_main)
        hl_main.setContentsMargins(0, 0, 0, 0)
        self.mahjong = Mahjong(self)
        # wg_right = QtWidgets.QWidget()
        # # wg_right.setFixedWidth(200)
        # # vl_right = QtWidgets.QVBoxLayout(wg_right)
        hl_main.addWidget(self.mahjong)
        # hl_main.addWidget(wg_right)

    def _setup_ui(self):
        self.setWindowTitle('窗口')

        self.move(self.width() * (-2), 0)  # 先将窗口放到屏幕外，可避免移动窗口时的闪烁现象。
        self.show()

        height_title = self.frameGeometry().height() - self.geometry().height()

        # # 获取显示器分辨率大小
        desktop = QtWidgets.QApplication.desktop()
        height = desktop.availableGeometry().height()
        # screenRect = desktop.screenGeometry()

        # self.setFixedSize(1200, height-100)
        self.resize(1200, height - height_title)
        # self.setGeometry(10, 0, 1200, height-title_height)

        # self.center()
        Utils.center(self)

    # def resizeEvent(self, event):
    #     palette = QtGui.QPalette()
    #     pix = QtGui.QPixmap('./res/images/background.jpg')
    #     pix = pix.scaled(self.width(), self.height())
    #     palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
    #     self.setPalette(palette)


if __name__ == '__main__':
    # 字体大小自适应分辨率
    app = None
    v_compare = QtCore.QVersionNumber(5, 6, 0)
    v_current, _ = QtCore.QVersionNumber.fromString(QtCore.QT_VERSION_STR)  # 获取当前Qt版本
    if QtCore.QVersionNumber.compare(v_current, v_compare) >= 0:
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication(sys.argv)
        font = QtGui.QFont("宋体")
        pointsize = font.pointSize()
        font.setPixelSize(pointsize * 90 // 72)
        app.setFont(font)

    # mainWnd = FrameLessWindow()
    # mainWnd.setWindowTitle('测试标题栏')
    # mainWnd.setWindowIcon(QtGui.QIcon('./res/images/tu.png'))
    #
    # height = app.desktop().screenGeometry().height()
    # screenRect = desktop.screenGeometry()
    # desktopRect = desktop.availableGeometry()
    # print(screenRect, desktopRect)

    # height = QtWidgets.QDesktopWidget().screenGeometry().height()
    # mainWnd.resize(QtCore.QSize(1200, height))
    #
    # mainWnd.setWidget(MainWindow())  # 把自己的窗口添加进来
    # mainWnd.show()
    # mainWnd.center()

    win = MainWindow()
    # win = Tile(None, 9)
    sys.exit(app.exec_())
