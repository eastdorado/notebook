#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @项目名称: python
# @File    : Utilities.py
# @Time    : 2019/12/30 23:22
# @Author  : big
# @Email   : shdorado@126.com

import os
import sys
import re
import psutil
# from PIL import Image, ImageStat, ImageEnhance
import win32api
import win32com
from win32com.client import constants, gencache, Dispatch
import docx
import json
import random
import string
import time
import uuid
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import functools


# from PyQt5 import object


class AllData(object):
    def __init__(self, parent=None):
        self.users_name = ['cyh', 'ganmin']
        self.users_pwd = {'cyh': ['pwd1=agcg', 'pwd2=gwtsd'], 'ganmin': ['dddd']}
        '''库数据-类别-网站-账户-细节'''
        self.vault_data = []
        self.data_unit = [[0, 'res/cross.png', '默认/登录'],
                          [1, 'res/flower.png', '默认/信任卡'],
                          [2, 'res/flower.png', '默认/身份'],
                          [3, 'res/flower.png', '默认/备注'],
                          [4, 'res/flower.png', '默认/密码'],
                          [5, 'res/flower.png', '默认/许可证'],
                          [6, 'res/flower.png', '默认/财务'],
                          [7, 'res/flower.png', '默认/旅游'],
                          [8, 'res/flower.png', '默认/电脑'],
                          [9, 'res/flower.png', '默认/杂项'],
                          [10, ['', '百度网盘', -1, False, 'res/cross.png'], ['账户', '', 2, False, ''],
                           ['密码', '', 0, True, ''],
                           ['邮箱', None, 2, False, ''], ['手机', None, 3, False, ''],
                           ['url', 'https://www.baidu.com', 2, False, '']],
                          [11, 'res/cross.png', '网易邮箱'],
                          [12, 'res/cross.png', '微博'],
                          [13, 'res/cross.png', '工行'],
                          [14, 'res/cross.png', 'QQ'],
                          [15, 'res/cross.png', '微信']]  # 模板，常用网站的信息
        """ mold: 0=标题 1=普通3个控件 2=分段 3=密码复合区 4=密码保护复合区 5=底部复合区
        """
        self.data_family = [['res/flower.png', '登录', [0, 10, 14]],  # 模板序号
                            ['res/flower.png', '信任卡', [1, 12]],
                            ['res/flower.png', '身份', [2]],
                            ['res/flower.png', '备注', [3]],
                            ['res/flower.png', '密码', [4]],
                            ['res/flower.png', '许可证', [5]],
                            ['res/flower.png', '财务', [6]],
                            ['res/flower.png', '旅游', [7]],
                            ['res/flower.png', '电脑', [8]],
                            ['res/flower.png', '杂项', [9]]]  # 类别
        self.field_style = ['密码', '支付密码', '文字', '用户名', 'URL', '电话', '电邮', 'PIN码', '数字', '日期', 'TOTP', '多行',
                            '持卡人姓名', '卡号', 'CVC', '卡PIN码', '有效日期', '银行名称', '卡类型', '有效自']
        self.data_cards = [
            [[1, '百度网盘', -1, None, 'res/cross.png'], ['账户', '', 2, False, None], ['密码', '', 0, True, None],
             ['邮箱', None, 6, False, None], ['手机', None, 5, False, None],
             ['其他详细信息', None, -2, None, None], ['标签', '', -3, '备注', '']],
            [[4, '工行', -1, None, 'res/cross.png'], ['账户', '', 2, False, None], ['密码', '', 0, True, None],
             ['邮箱', None, 6, False, None], ['手机', None, 5, False, ''], ['标签', '', -3, '备注', '']],
            [[1, '网易邮箱', -1, None, 'res/cross.png'], ['账户', '', 2, False, None], ['密码', '', 0, True, None],
             ['标签', '', -3, '备注', '']],  # 第一个数字是家庭/类别的代号，最后一项必须是标签和备注的混合体
            [[1, '微信', -1, None, 'res/cross.png'], ['账户', '', 2, False, None], ['密码', '', 0, True, None],
             ['邮箱', None, 6, False, None], ['标签', '', -3, '备注', '']]]  # 详情卡片
        self.cur_card = 0
        self.favorites = []  # 保存收藏夹各项在cards里的序号


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        只要检查到了是bytes等特殊类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        from datetime import date, datetime, time
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        elif isinstance(obj, bytes):
            # return str(obj, encoding='utf-8')
            return str(obj, encoding='ISO-8859-1')
        elif isinstance(obj, time):
            return obj.__str__()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class Utils(object):
    def __init__(self):
        pass

    # 语言国际化
    @staticmethod
    def tr(msg):
        return QtCore.QCoreApplication.translate("@default", msg)

    # 获取大小写字母、数字、特殊字符等可见字符的列表
    @staticmethod
    def get_chars(mold=5):
        """
        # 0～31及127(共33个)是控制字符或通信专用字符（其余为可显示字符）
        # 32～126(共95个)是字符(32是空格），
        # 其中48～57为0到9十个阿拉伯数字。
        # 65～90为26个大写英文字母，
        # 97～122号为26个小写英文字母。
        # 其他为特殊字符，33个 special_
        mold:类型，1：大小字母集 2：小写字母集 3：大小写字母集 4：数字集
                    5：字母+数字 6：特殊字符集 7：所有可见字符集(前6项)
        """

        char_list = []
        if mold == 1:
            char_list = string.ascii_uppercase
        elif mold == 2:
            char_list = string.ascii_lowercase
        elif mold == 3:
            char_list = string.ascii_letters
        elif mold == 4:
            char_list = string.digits
        elif mold == 5:
            char_list = string.ascii_letters + string.digits
        else:
            for i in range(32, 48):
                char_list.append(chr(i))
            for i in range(58, 65):
                char_list.append(chr(i))
            for i in range(91, 97):
                char_list.append(chr(i))
            for i in range(123, 127):
                char_list.append(chr(i))

            if mold != 6:  # not special only
                char_list.extend(string.ascii_letters + string.digits)

        # print(len(char_list), char_list)
        return char_list

    @staticmethod
    def swaps(a, b):
        a ^= b
        b ^= a
        a ^= b
        return a, b

    @staticmethod
    def rand_int(num_min, num_max):
        seed = time.time()
        sr = random.SystemRandom(seed)
        # print(type(sr))

        ret = sr.randint(num_min, num_max)
        # print(ret)

        return ret

    @staticmethod
    # 字符串是否合法的PIN码
    def validate_pin(pin):
        return len(pin) in (4, 6) and pin.isdigit()
        # return len(pin) in (4, 6) and pin.isnumeric()

    @staticmethod
    def get_pin(arr=[1, 2, 3, 5, 4, 6], mold=1):
        if mold == 1:  # 数字
            # 方法baidu1用数学方法计算出结果
            return functools.reduce(lambda x, y: x * 10 + y, arr)
            # 方法2用字符串合并出zhi结果
            # return int(functools.reduce(lambda x, y: str(x) + str(y), arr))
        else:  # 下面是字符串
            return str(arr).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")

    @staticmethod
    def rand_float(num_min, num_max, n=2):
        # 小数位数
        seed = time.time()
        sr = random.SystemRandom(seed)
        # print(type(sr))

        ret = sr.uniform(num_min, num_max)
        # ret = sr.random()

        ret = round(ret, n)  # n位小数，碰到.5，前一位小数是奇数，则直接舍弃，如果偶数则向上取舍
        # print('{:04.2f}'.format(sr.random()))

        return ret

    # 生成随机字符串 密码学意义上更加安全的版本
    @staticmethod
    def rand_str(char_set=string.ascii_letters + string.digits, size=10):
        print(char_set)  # 将大/小写的ASCII字符列表和数字组合起来

        seed = time.time()
        sr = random.SystemRandom(seed)
        # print(type(sr), sr.choice(char_set))
        # print(type(sr.choice(char_set) for _ in range(size)))
        # return
        random_string = ''.join(sr.choice(char_set) for _ in range(size))

        # 首字母不能是数字
        random_string = Utils.rand_str(size) if random_string[0].isdigit() else random_string
        # print(random_string)

        return random_string

    # 使用Python内置的uuid库 生成随机字符串
    @staticmethod
    def rand_str2(size=10):
        random_string = str(uuid.uuid4()).replace("-", "")  # Remove the UUID '-'
        size = len(random_string) if size > len(random_string) else size
        random_string = random_string[0:size]
        print(type(random_string))

        # 首字母不能是数字
        random_string = Utils.rand_str2(size) if random_string[0].isdigit() else random_string
        print(random_string)

        return random_string

    @staticmethod
    def readQss(style_file):
        """读取qss文件"""
        with open(style_file, 'r') as f:
            return f.read()

    @staticmethod
    def elideText(strInfo, width, font):
        """长字符串省略表示法"""
        """font: 显示的字体
           width: 显示的长度限制
           strInfo: 原始的长字符串
           return: 带省略号的字符串
        """
        try:
            fontMetrics = QtGui.QFontMetrics(font)
            # 如果当前字体下，字符串长度大于指定宽度
            if fontMetrics.width(strInfo) > width:
                strInfo = fontMetrics.elidedText(strInfo, QtCore.Qt.ElideRight, width)
        except Exception as e:
            print(e)
        finally:
            return strInfo

    @staticmethod
    def getSubStr(longStr, max_width=15, font=QtGui.QFont('微软雅黑', 12)):
        """截取字符串中间用省略号显示"""
        try:
            assert isinstance(longStr, str)

            fontMetrics = QtGui.QFontMetrics(font)
            char_width = fontMetrics.width('a')
            max_len = int(max_width / char_width)
            # 如果当前字体下，字符串长度大于指定宽度
            # if fontMetrics.width(longStr) > max_width:
            if len(longStr) > max_len:
                # subStr1 = longStr[0:10]
                # subStr2 = longStr[-5:]
                subStr1 = longStr[0:int(max_len / 2) - 3 * char_width]
                subStr2 = longStr[-int(max_len / 2) + 3 * char_width:]
                subStr = subStr1 + "..." + subStr2
                return subStr
            else:
                return longStr
        except Exception as e:
            print(e)
            return longStr

    @staticmethod
    def getSubStr1(longStr):
        """截取字符串中间用省略号显示"""
        assert isinstance(longStr, str)

        if len(longStr) > 15:
            subStr1 = longStr[0:10]
            subStr2 = longStr[-5:]
            subStr = subStr1 + "..." + subStr2
            return subStr
        else:
            return longStr

    @staticmethod
    def doAnim(widget, started=True):
        """窗体移动/缩放动画"""
        if widget:
            animation = QtCore.QPropertyAnimation(widget, b"geometry", widget)
            animation.setDuration(300)
            sp = widget.geometry()
            if started:
                ep = QtCore.QRect(sp.x() - sp.width(), sp.y(), sp.width(), sp.height())
            else:
                ep = QtCore.QRect(sp.x() + sp.width(), sp.y(), sp.width(), sp.height())
            animation.setStartValue(sp)
            animation.setEndValue(ep)
            animation.start()
        # ani = QtCore.QPropertyAnimation(self)  # 创建动画对象
        # ani.setTargetObject(self)     # 设置动画目标对象
        # ani.setPropertyName(b'pos')  # 设置动画属性
        # # 注意：字节类型
        # # pos---位置动画---QPoint
        # # size---大小动画---QSize
        # # geometry----位置+大小动画----QRect
        # # windowOpacity---窗口的透明度(0.0是透明的    1.0是不透明)---好像只适合顶层窗口
        # ani.setStartValue(QtCore.QPoint(self.x(), self.y()))  # 设置开始位置---按钮的左上角位置
        # ani.setEndValue(QtCore.QPoint(300, 300))  # 设置结束位置
        # # ani.setStartValue(QSize(0, 0))  # 设置开始大小
        # # ani.setEndValue(QSize(300, 300))  # 设置结束大小
        # # ani.setStartValue(QRect(0, 0,100,100))  # 设置开始位置和大小
        # # ani.setEndValue(QRect(100,100,300, 300))  # 设置结束位置和大小
        # # ani.setStartValue(1)  # 设置开始不透明
        # # ani.setKeyValueAt(0.5,0.2)#在动画的某时间点插入一个值
        # # 参数1 0.0到1.0  0.0表示开始点，1.0表示结束点
        # # 在动画的中间插入透明度0.2
        # # ani.setKeyValueAt(1, 1)  #在动画的结束点是不透明的
        # # ani.setEndValue(0)  # 设置结束透明
        #
        # ani.setDuration(5000)  # 设置动画单次时长---单位毫秒
        # ani.setEasingCurve(QtCore.QEasingCurve.InQuad)  # 设置动画的节奏
        # # # 取值   https://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        # #
        # ani.start()  # 动画开始---非阻塞
        # ani.setLoopCount(3)  # 设置动画次数---默认1次
        # ani.setDirection(QAbstractAnimation.Forward)  # 设置动画方向
        # # QAbstractAnimation.Backward=1  动画的当前时间随着时间减少（即，从结束/持续时间向0移动）---倒序
        # # QAbstractAnimation.Forward=0 动画的当前时间随着时间而增加（即，从0移动到结束/持续时间）---顺序
        #
        # # 信号
        # ani.currentLoopChanged.connect(self.FF)  # 循环遍数发生变化时
        # # 会向槽函数传递一个参数---当前循环的遍数
        #
        # # directionChanged(QAbstractAnimation.Direction newDirection)   动画方向发生改变时
        # # 会向槽函数传递一个参数---动画新方向
        #
        # ani.finished.connect(self.HH)  # 动画完成时
        #
        # ani.stateChanged.connect(self.GG)  # 状态发生改变时
        # # 会向槽函数传递两个参数---新状态和老状态
        #
        # ani.start()  # 启动动画
        # # 参数 QAbstractAnimation.KeepWhenStopped  停止时不会删除动画
        # #     QAbstractAnimation.DeleteWhenStopped   停止时动画将自动删除

    @staticmethod
    def clear_layout(layout):
        if layout is None:
            AnimWin('no layout')
            return
        # print(f'begin:count={layout.count()}')
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QLayout):
                Utils.clear_layout(item)
            elif isinstance(item, QtWidgets.QSpacerItem):
                # print(item)
                # item = QtWidgets.QSpacerItem()
                item.changeSize(0, 0)
                # item.setGeometry(QtCore.QRect(0, 0, 0, 0))
                # print(type(item.spacerItem()))
            # elif isinstance(item, object):
            else:
                wg = item.widget()
                if wg:
                    wg.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                    # wg.setParent(None)
                    # layout.removeWidget(wg)
                    wg.deleteLater()
            layout.removeItem(item)
        # print(f'end:count={layout.count()}')

    @staticmethod
    def get_version_via_com(filename):  # error
        parser = win32com.client.Dispatch("Scripting.FileSystemObject")
        version = parser.GetFileVersion(filename)
        size = os.path.getsize(filename)
        return version

    @staticmethod
    def getFileVersion(file_name):  # none
        try:
            info = win32api.GetFileVersionInfo(file_name, os.sep)
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            version = '%d.%d.%d.%d' % (
                win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
            return version
        except Exception as e:
            return "None"

    @staticmethod
    def formatTime(localtime):
        """格式化时间的函数"""
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(localtime))

    @staticmethod
    def formatByte(f_size):
        """格式化文件大小"""
        f_size = round(f_size, 2)  # 首先四舍五入到2位小数
        for (scale, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB")]:
            if f_size >= scale:
                return "%.2f %s" % (f_size * 1.0 / scale, label)
        # 小于1K字节
        return f'{f_size or 0} B'
        # byte = "%.2f" % (f_size or 0)
        # return (byte[:-3] if byte.endswith(".00") else byte) + "字节"

    @staticmethod
    def getFileInfo(filePath):
        # f_size = os.path.getsize(filePath)
        # f_size = f_size / float(1024 * 1024)
        # return round(f_size, 2)

        if not os.path.isfile(filePath):
            return

        file_info = os.stat(filePath)  # 获取文件的基本信息
        info = dict()
        info['完整路径'] = f'{os.path.abspath(filePath)}'
        info['索引号'] = f'{file_info.st_ino}'
        info['设备名'] = f'{file_info.st_dev}'
        info['最后一次的修改时间'] = Utils.formatTime(file_info.st_mtime)
        info['最后一次的状态变化时间'] = Utils.formatTime(file_info.st_ctime)
        info['最后一次的访问时间'] = Utils.formatTime(file_info.st_atime)
        info['文件大小'] = Utils.formatByte(file_info.st_size)

        return info

    @staticmethod
    def _getCompanyNameAndProductName(file_path):
        """
            Read all properties of the given file return them as a dictionary.
        """
        propNames = ('Comments', 'InternalName', 'ProductName',
                     'CompanyName', 'LegalCopyright', 'ProductVersion',
                     'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                     'FileVersion', 'OriginalFilename', 'SpecialBuild')

        props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

        try:
            # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
            fixedInfo = win32api.GetFileVersionInfo(file_path, '\\')
            props['FixedFileInfo'] = fixedInfo
            props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                                                    fixedInfo['FileVersionMS'] % 65536,
                                                    fixedInfo['FileVersionLS'] / 65536,
                                                    fixedInfo['FileVersionLS'] % 65536)

            # \VarFileInfo\Translation returns list of available (language, codepage)
            # pairs that can be used to retreive string info. We are using only the first pair.
            lang, codepage = win32api.GetFileVersionInfo(file_path, '\\VarFileInfo\\Translation')[0]

            # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
            # two are language/codepage pair returned from above

            strInfo = {}
            for propName in propNames:
                strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
                ## print str_info
                strInfo[propName] = win32api.GetFileVersionInfo(file_path, strInfoPath)

            props['StringFileInfo'] = strInfo
        except Exception as e:
            print(e)

        if not props["StringFileInfo"]:
            return None, None
        else:
            return props["StringFileInfo"]["CompanyName"], props["StringFileInfo"]["ProductName"]

    @staticmethod
    def _get_company_and_product(file_path):
        import pefile
        """ linux系统
            Read all properties of the given file return them as a dictionary.
            @return: a tumple, (company, product)
            """
        mype = pefile.PE(file_path)
        companyName = ""
        productName = ""

        if hasattr(mype, 'VS_VERSIONINFO'):
            if hasattr(mype, 'FileInfo'):
                for entry in mype.FileInfo:
                    if hasattr(entry, 'StringTable'):
                        for st in entry.StringTable:
                            for k, v in st.entries.items():
                                if k == u"CompanyName":
                                    companyName = v
                                elif k == u"ProductName":
                                    productName = v
        if not companyName:
            companyName = None
        if not productName:
            productName = None
        return companyName, productName

    @staticmethod
    def get_file_extension(filename):
        result = None
        if filename:
            result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', filename)[0]
        return result

    @staticmethod
    def file_is_given_type(img_filename, file_extension=('.jpg', '.jpeg', '.gif', '.bmp', '.png', '*.xpm')):
        """
        忽略大小写，忽略list还是tuple，判断文件后缀是否在内，后缀最好带上‘，’，以免误判
        :param img_filename: 文件名
        :param file_extension: 文件后缀列表或元祖或字符串或字符
        :return: True or False
        """
        try:
            suffixes = tuple(each.lower() for each in file_extension if isinstance(each, str))
            return img_filename.lower().endswith(suffixes)
        except Exception as e:
            print(f'is_image_file() : {e}')

    @staticmethod
    def files_in_dir(dir_name, suffix_list=[], full_path=False):
        '''
        列出目录下指定类型的所有文件
        :param dir_name: 目录名称
        :param suffix_list: 带.号的文件后缀列表
        :param full_path: 文件名带路径或者不含路径
        :return: 文件名称的列表
        '''
        if not dir_name:
            print('null dir')
            return
        if not isinstance(suffix_list, list):
            print('后缀应该存入列表中')

        if not os.path.isdir(dir_name):
            print("it's not a directory")
            return

        list_files = []
        dir_files = os.listdir(dir_name)  # 列出文件夹下所有的目录与文件
        for each in dir_files:
            path = os.path.join(dir_name, each)  # 构造完整路径
            # 判断路径是否是一个文件目录或者文件
            if os.path.isfile(path):
                if not suffix_list:  # 后缀列表空，默认全部文件列出
                    if full_path:
                        list_files.append(path)
                    else:
                        list_files.append(each)
                else:
                    if Utils.file_is_given_type(each, suffix_list):
                        # portion = os.path.splitext(each)  # 分离文件名与扩展名
                        # if portion[1] in suffix_list:
                        if full_path:
                            list_files.append(path)
                        else:
                            list_files.append(each)
            else:
                # print('it is a dir')
                pass

        return list_files

    @staticmethod
    def getFiles(path, suffixes):
        """ 列出目录及子目录下所有的指定类型的文件 """
        return [os.path.join(root, file) for root, dirs, files in os.walk(path)
                for file in files if Utils.file_is_given_type(file, suffixes)]

    @staticmethod
    def cout_list(the_list, indent=False, level=0, fh=sys.stdout):
        """	　　　　　　	　
        函数：print_list()
        功能：打印列表中的数据项，如果子项是列表，则递归打印
        参数：
        　　the_list:  列表
        　　indent:	　 是否开启嵌套打印时缩进显示，默认False表示不开启，即各级显示在同一列
        　　level:	　　控制缩进，如果level为正值，表示一行要增加多少个空格，如果为0，不缩进
        　　fh:　　	　 输出位置，默认为标准输出，即窗口，可以指定输出到文件中。　　
        """
        for item in the_list:
            if isinstance(item, list):  # 判断当前项是不是列表，如果是列表，递归操作
                Utils.cout_list(item, indent, level + 2, fh)  # 如果用++level会有问题
            else:  # 如果是具体的项
                if indent:  # 如果开启缩进
                    for tab_stop in range(level):  # 输出空格
                        print(" ", end='', file=fh)
                print(item, file=fh)

    @staticmethod
    def cout_dict(the_dict, json_file):
        # stus = {'xiaojun': '123456', 'xiaohei': '7890', 'lrx': '111111'}
        res = json.dumps(the_dict, indent=4, ensure_ascii=False, cls=MyEncoder)  # 使用.dumps()方法是要写入
        with open(json_file, 'w', encoding='utf8') as f:
            # json.dump(the_dict, f)
            f.write(res)

    # region string 中包含数字，根据数字排序
    ''' python list sort中string 中包含数字，根据数字排序 '''

    def tryint(c):
        try:
            return int(c)
        except:
            return c

    def alphanum_key(s):
        """ Turn a string into a list of string and number chunks.
            "z23a" -> ["z", 23, "a"]
        """
        return [Utils.tryint(c) for c in re.split('([0-9]+)', s)]

    def sort_nicely(l):
        """ Sort the given list in the way that humans expect.
        """
        if isinstance(l, list):
            l.sort(key=Utils.alphanum_key)

    # endregion

    @staticmethod
    def word2Pdf(wordPath, pdfPath):
        """
        word转pdf
        :param wordPath: word文件路径
        :param pdfPath:  生成pdf文件路径
        """
        # w = Dispatch("Word.Application")
        # try:
        #     # w.Visible = Debug
        #     doc = w.Documents.Open(input, ReadOnly=1)
        #     doc.ExportAsFixedFormat(pdfPath, constants.wdExportFormatPDF,
        #                             Item=constants.wdExportDocumentWithMarkup,
        #                             CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        #     return 0
        # except:
        #     return 1
        # finally:
        #     w.Quit(constants.wdDoNotSaveChanges)

        try:
            # 打开word软件
            word = gencache.EnsureDispatch('Word.Application')
            # 非可视化运行
            word.Visible = False
            doc = word.Documents.Open(wordPath, ReadOnly=1)

            doc.ExportAsFixedFormat(pdfPath,
                                    constants.wdExportFormatPDF,
                                    Item=constants.wdExportDocumentWithMarkup,
                                    CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            doc.Close()
            word.Quit(constants.wdDoNotSaveChanges)
        except Exception as e:
            return -1
        finally:
            return 0

    @staticmethod
    def doc2docx(srcdoc_path, dstdocx_path):
        word = Dispatch('Word.Application')
        doc = word.Documents.Open(srcdoc_path, ReadOnly=1)  # 目标路径下的文件
        doc.SaveAs(dstdocx_path, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
        doc.Close()
        word.Quit()

    @staticmethod
    def getDocPageNum(filePath):
        pageNum = 0
        try:
            # 建立ActiveX部件
            word = gencache.EnsureDispatch('Word.Application')
            word.Visible = False
            wrdDocs = word.getProperty("Documents").toDispatch()

            doc = word.Documents.Open(filePath, ReadOnly=1)
            selection = word.Selection()
            pageNum = selection.information(4)

            word.Close(constants.wdDoNotSaveChanges)
            word.Quit(constants.wdDoNotSaveChanges)
            # ActiveXComponent wordCom = new ActiveXComponent("Word.Application");
            # // word应用程序不可见
            # wordCom.setProperty("Visible", false);
            # // 返回wrdCom.Documents的Dispatch
            # Dispatch wrdDocs = wordCom.getProperty("Documents").toDispatch(); // Documents表示word的所有文档窗口（word是多文档应用程序）
            # // 调用wrdCom.Documents.Open方法打开指定的word文档，返回wordDoc
            # Dispatch wordDoc = Dispatch.call(wrdDocs, "Open", filePath, false, true, false).toDispatch();
            # Dispatch selection = Dispatch.get(wordCom, "Selection").toDispatch();
            # pageNum = Integer.parseInt(Dispatch.call(selection, "information", 4).toString()); // 总页数 // 显示修订内容的最终状态
            # // 关闭文档且不保存
            # Dispatch.call(wordDoc, "Close", new Variant(false));
            # // 退出进程对象
            # wordCom.invoke("Quit", new Variant[] {});
        except Exception as e:
            print(e)
        finally:
            return pageNum

    @staticmethod
    def wordinfo(wordPath):
        try:
            # 打开word软件
            word = gencache.EnsureDispatch('Word.Application')
            # 非可视化运行
            word.Visible = False
            doc = word.Documents.Open(wordPath, ReadOnly=1)

            # 下面是取得打开文件的页数
            pages = doc.ComputeStatistics(constants.wdStatisticPages)
            word.Close(constants.wdDoNotSaveChanges)
            word.Quit(constants.wdDoNotSaveChanges)

            return pages
        except Exception as e:
            return -1
        finally:
            return 0

    @staticmethod
    def mergewords(files_list, outfile, ctl_progress=None):
        '''
        合并多个已经排序的word文档
        :param files_list: 已经排序的文件名列表
        :param outfile: 合成后的文件
        :param ctl_progress:
        :return:
        '''

        if not files_list:
            return
        # 打开word软件
        word = gencache.EnsureDispatch('Word.Application')
        # 非可视化运行
        word.Visible = False
        output = word.Documents.Add()  # 新建合并后空白文档

        # 需要合并的文档路径，这里有个文档1.docx，2.docx，3.docx.
        # files = ['F://work//2.docx', 'F://work//1.docx', 'F://work//3.docx']
        Utils.sort_nicely(files_list)  # 按数字大小排序
        files_list.reverse()  # 从后往前插入

        files_weight = []
        if isinstance(ctl_progress, QtWidgets.QProgressBar):
            for file in files_list:
                files_weight.append(Utils.get_FileSize(file))
        print(sum(files_weight))

        for i in range(len(files_list)):
            output.Application.Selection.Range.InsertFile(files_list[i])  # 拼接文档
            if isinstance(ctl_progress, QtWidgets.QProgressBar):
                value = int(sum(files_weight[:i + 1]) / sum(files_weight) * 100)
                # print(value)
                ctl_progress.setValue(value)

        # # 获取合并后文档的内容
        # doc = output.Range(output.Content.Start, output.Content.End)
        # doc.Font.Name = "黑体"  # 设置字体

        output.SaveAs(outfile)  # 保存
        output.Close()

    # 获取CPU信息
    @staticmethod
    def GetCpuInfo():

        cpu_count = psutil.cpu_count(logical=False)  # 1代表单核CPU，2代表双核CPU
        # 获取cpu物理个数    计算方式：单个cpu核数*cpu个数

        xc_count = psutil.cpu_count()  # 线程数，如双核四线程
        # 获取cpu逻辑个数
        # 计算方式：单个cpu核数*cpu个数*2（cpu cores 这个规格值，如果支持并开启ht）
        # ht：intel的超线程技术(HT), 可以在逻辑上再分一倍数量的cpu core出来

        cpu_slv = round((psutil.cpu_percent(1)), 2)  # cpu使用率

        list_cpu = [cpu_count, xc_count, cpu_slv]
        return list_cpu

    # 获取内存信息
    @staticmethod
    def GetMemoryInfo():
        memory = psutil.virtual_memory()
        total_nc = round((float(memory.total) / 1024 / 1024 / 1024), 2)  # 总内存
        used_nc = round((float(memory.used) / 1024 / 1024 / 1024), 2)  # 已用内存
        free_nc = round((float(memory.free) / 1024 / 1024 / 1024), 2)  # 空闲内存
        syl_nc = round((float(memory.used) / float(memory.total) * 100), 2)  # 内存使用率

        ret_list = [total_nc, used_nc, free_nc, syl_nc]
        return ret_list

    # 获取硬盘信息
    @staticmethod
    def GetDiskInfo():
        list_disk = psutil.disk_partitions()  # 磁盘列表
        ilen = len(list_disk)  # 磁盘分区个数
        i = 0
        retlist1 = []
        retlist2 = []
        while i < ilen:
            diskinfo = psutil.disk_usage(list_disk[i].device)
            total_disk = round((float(diskinfo.total) / 1024 / 1024 / 1024), 2)  # 总大小
            used_disk = round((float(diskinfo.used) / 1024 / 1024 / 1024), 2)  # 已用大小
            free_disk = round((float(diskinfo.free) / 1024 / 1024 / 1024), 2)  # 剩余大小
            syl_disk = diskinfo.percent

            retlist1 = [i, list_disk[i].device, total_disk, used_disk, free_disk, syl_disk]  # 序号，磁盘名称，
            retlist2.append(retlist1)
            i = i + 1

        return retlist2

    @staticmethod
    def addTransparency(img_file, factor=0.7):
        img = Image.open(img_file)
        img = img.convert('RGBA')
        img_blender = Image.new('RGBA', img.size, (0, 0, 0, 0))
        img = Image.blend(img_blender, img, factor)
        return img

    @staticmethod
    def pil2pixmap(im):
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap

    # # 读取图片原有的亮度值
    # @staticmethod
    # def brightness(path):
    #     im = Image.open(path)
    #     stat = ImageStat.Stat(im)
    #     r, g, b = stat.mean
    #     return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
    # # 获取文件亮度平均值
    # @staticmethod
    # def brightness_avg(path):
    #     os.chdir(path)
    #     sum = 0.0
    #     img_len = len(os.listdir())
    #     for name_list_image in os.listdir():
    #         if name_list_image.endswith(".jpg"):
    #             image_url = os.getcwd() + '/' + name_list_image
    #             b = Utils.brightness(image_url)
    #             sum += b
    #             print('%s=%s' % (image_url, b))
    #     avg = sum / img_len
    #     return avg
    # 设置图片亮度
    # @staticmethod
    # def set_brightness(b_avg, path):
    #     for name_list_image in os.listdir():
    #         if name_list_image.endswith(".jpg"):
    #             image_url = os.getcwd() + '/' + name_list_image
    #             im = Image.open(image_url)
    #             im = ImageEnhance.Brightness(im).enhance(b_avg / Utils.brightness(image_url))
    #             # path = r'C:\Users\Smart\Desktop\image\new'
    #             flag = os.path.exists(path)
    #             if not flag:
    #                 os.mkdir(path)
    #             im.save(path + '/' + name_list_image)


class AnimWin(QtWidgets.QWidget):
    """ 自动消失的提示框 """

    def __init__(self, msg='', parent=None, font_size=16):
        super(AnimWin, self).__init__(parent)

        # self.parent = parent
        self.animation = None

        # 一定要先设置鼠标床头，否则无法穿透，应该是属性中间有值影响
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # 无边框，最前端
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   # 透明

        label = QtWidgets.QLabel(self)
        label.setText(msg)

        font = QtGui.QFont("Microsoft YaHei")
        font.setPointSize(font_size)
        font.setBold(True)
        fm = QtGui.QFontMetrics(font)
        rect = QtCore.QRect(fm.boundingRect(msg))  # 字符串所占的像素宽度, 高度
        margin = 5
        rect.setWidth(rect.width() + 5 * margin)
        rect.setHeight(rect.height() + 2 * margin)
        # rect = QtCore.QRect(0, 0, 1820, 980)
        self.resize(rect.size())
        # self.resize(500, 100)

        label.setFont(font)
        label.setAutoFillBackground(True)
        palette = QtGui.QPalette()  # 新建一个调色板
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor('#4682B4'))  # 设置颜色
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.darkRed)  # 设置颜色
        label.setPalette(palette)
        label.setAlignment(QtCore.Qt.AlignCenter)

        vl = QtWidgets.QVBoxLayout()  # 设置垂直布局
        # vl.setContentsMargins(margin*3, margin, margin*3, margin)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(label)  # 添加控件
        self.setLayout(vl)

        # if parent:
        #     print(parent.frameGeometry(), parent.geometry())
        #     self.move(parent.x() + int((parent.width() - rect.width()) / 2),
        #               parent.y() + int((parent.height() - rect.height()) / 2))
        self.win_center(parent)

        self.close()
        self.show()

    '''无边框移动'''

    # def mousePressEvent(self, QMouseEvent):
    #     if QMouseEvent.button() == Qt.LeftButton:
    #         self.flag = True
    #         self.m_Position = QMouseEvent.globalPos() - self.pos()
    #         QMouseEvent.accept()
    #         self.setCursor(Qt.QCursor(Qt.OpenHandCursor))
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.flag = False
    #     self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
    def closeEvent(self, event):
        if self.animation is None:
            self.animation = QtCore.QPropertyAnimation(self, b'windowOpacity')
            self.animation.setDuration(3000)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation.start()
            event.ignore()

    def win_center(self, parent=None):
        if parent:
            rect = self.rect()
            self.move(int((parent.width() - rect.width()) / 2),
                      int((parent.height() - rect.height()) / 2))
        else:
            # availableGeometry()返回屏幕可用区域的位置和尺寸的QRect对象，即扣除任务栏的区域
            # screenGeomtry():返回整个屏幕的位置和尺寸的QRect对象
            center = QtWidgets.QDesktopWidget().availableGeometry().center()
            window = self.geometry()
            # window = self.frameGeometry()  # 包括标题栏的高度和边框的宽度且要在显示之后调用才有效
            window.moveCenter(center)
            self.move(window.topLeft())


# 圆形按钮
class EllipseButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, width=100, height=100):
        super(EllipseButton, self).__init__(parent, width=100, height=100)
        self.parent = parent
        self.setFixedSize(width, height)

    def set(self, img, text='', border=0, padding=0, color=None, background_color=None, border_color=None):

        self.setText(text)

        width, height = self.width(), self.height()
        wide = min(width, height)

        radius = wide // 2 + padding + border

        color = 'blue' if color is None else color
        background_color = 'green' if background_color is None else background_color
        border_color = 'gray' if border_color is None else border_color

        qss = None
        if img:
            pix = QtGui.QImage(img)

            ratio_w = pix.width() / width
            ratio_h = pix.height() / height

            is_w = True if ratio_w > ratio_h else False
            # print(sw, sh, is_w)

            img_new = pix.scaledToWidth(height) if is_w else pix.scaledToHeight(width)
            new_img = './tmp.jpg'
            img_new.save(new_img)
            # self.setAutoFillBackground(True)  # /Widget增加背景图片时，这句一定要。
            # wide = min(width, height)
            # pix = QtGui.QPixmap(img).scaled(wide, wide, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
            # self.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(img_new)))
            # self.setIconSize(QtCore.QSize(wide, wide))
            # self.setFlat(True)  # 就是这句能够实现按钮透明，用png图片时很有用
            # border = 0  # 消除边框，取消点击效果

            qss = '''
                color: %s;
                background-color: %s;
                background: transparent;     /*全透明*/
                background-image:url(%s);
                background-position: center center;      /*图片的位置，居中，靠左对齐*/
                background-repeat: no-repeat;       /*背景不要重复*/

                border-style:none;
                border:%dpx solid %s; 
                padding:%dpx;
                min-width:%dpx;max-width:%dpx;
                min-height:%dpx;max-height:%dpx;            
                border-radius:%dpx;
                ''' % (color, background_color, new_img, border, border_color, padding,
                       width, width, height, height, radius)
        else:
            qss = '''
                color: %s;
                background-color: %s;

                border-style:none;
                border:%dpx solid %s; 
                padding:%dpx;
                min-width:%dpx;max-width:%dpx;
                min-height:%dpx;max-height:%dpx;            
                border-radius:%dpx;
                ''' % (color, background_color, border, border_color, padding,
                       width, width, height, height, radius)
        # print(qss)
        self.setStyleSheet(qss)

        # radius = width // 2 + padding + border if width < height else height // 2 + padding + border
        # color = 'blue' if color is None else color
        # background_color = 'green' if background_color is None else background_color
        # border_color = 'gray' if border_color is None else border_color
        #
        # qss = None
        # if img:
        #     qss = '''
        #         color: %s;
        #         background-color: %s;
        #         background-image:url(%s);
        #
        #         border-style:none;
        #         border:%dpx solid %s;
        #         padding:%dpx;
        #         min-width:%dpx;max-width:%dpx;
        #         min-height:%dpx;max-height:%dpx;
        #         border-radius:%dpx;
        #         ''' % (color, background_color, img, border, border_color, padding, width, width,
        #                height, height, self.radius)
        # else:
        #     qss = '''
        #         color: %s;
        #         background-color: %s;
        #
        #         border-style:none;
        #         border:%dpx solid %s;
        #         padding:%dpx;
        #         min-width:%dpx;max-width:%dpx;
        #         min-height:%dpx;max-height:%dpx;
        #         border-radius:%dpx;
        #         ''' % (color, background_color, border, border_color, padding,
        #                width, width, height, height, radius)
        # # print(qss)
        # self.setStyleSheet(qss)

    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     painter = QtGui.QPainter(self)
    #     painter.setRenderHint(QtGui.QPainter.Antialiasing)  # 反锯齿
    #     painter.setBrush(QtGui.QBrush(QtGui.QPixmap(self.img)))  # 设置底图的方式之一
    #     # painter.setBrush(QBrush(Qt.blue))
    #     painter.setPen(QtCore.Qt.transparent)
    #
    #     rect = self.rect()
    #     rect.setWidth(rect.width() - 1)
    #     rect.setHeight(rect.height() - 1)
    #     painter.drawEllipse(rect)
    #     # 也可用QPainterPath 绘制代替 painter.drawRoundedRect(rect, 15, 15)
    #     # painterPath= QPainterPath()
    #     # painterPath.addRoundedRect(rect, 15, 15)
    #     # painter.drawPath(painterPath)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # self.resize(800, 600)
        # self.setGeometry(800, 100, 800, 600)
        # self.win_center()
        AnimWin('好事多磨', self)

        # self.setupUi(self)

    def resizeEvent(self, event):
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap('res/background.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        self.setPalette(palette)


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    # sys.exit(app.exec_())
    # ll = Utils.GetCpuInfo()
    # print(f'cpu物理个数:{ll[0]}    cpu逻辑个数:{ll[1]}    cpu使用率:{ll[2]}')
    # ll = Utils.formatByte(0)
    # print(ll)
    # print(type(Utils.get_file_extension('ddsg.ext')))
    # print('ddd.ext'.endswith(''))
    # print(Utils.rand_str())
    # print(Utils.get_pin())
    print(Utils.files_in_dir(r'F:\重要', '.mp4'))