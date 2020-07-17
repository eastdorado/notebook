#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @Product: PyCharm
#  @Project: Neworld
#  @File    : PlayDumbbell.py
#  @Author  : big
#  @Email   : shdorado@126.com
#  @Time    : 2020/7/11 18:11
#  功能：

import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import cv2

import pyttsx3
import win32com.client
# from aip import AipSpeech  # 百度文本转语音

# from apscheduler.schedulers.blocking import BlockingScheduler
import schedule  # 轻量级定时任务调度库
import sched  # 定时
import time
from datetime import datetime

import multiprocessing  # 进程
import threading  # 线程
from threading import Timer

from utilities import Utils, AnimWin
import cgitb

cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示

data1 = [
    '每个动作10-15次，循环2-3组。训练过程每个动作尽量慢一点，动作都做到位，体会每个肌群的发力。',  # 每组循环提醒
]
data2 = [
    ['周一训练目标：胸+肱二头肌', '每个动作8-12次，每次做3-5组',
     ['动作一：上斜哑铃卧推', '将椅背调节到与地面呈30度左右，双脚踩实地面，臀部收紧，绷紧腹部，肩胛骨后缩下沉使上背平贴凳子\n'
                    '双手握住哑铃，拳心朝前，小臂垂直地面放于身体两侧\n'
                    '胸部发力，使上臂向身体中间靠拢，在最高点肘关节微弯，保持1秒；肩膀始终后缩下沉\n'
                    '缓慢下落，小臂始终垂直地面，下落至哑铃下沿与胸部在同一高度，稍作停顿', '2_1.gif'],
     ['动作二：平地哑铃卧推', '双脚踩实地面，臀部收紧，绷紧腹部，肩胛骨后缩下沉使上背平贴凳子，小臂垂直地面举起哑铃在身体两侧\n'
                    '胸部发力，使上臂向身体中间靠拢；在最高点肘关节微弯，稍作停留，肩膀始终后缩下沉\n'
                    '缓慢下落，小臂始终垂直地面，下落至哑铃下沿与胸部在同一高度，稍作停顿', '2_2.gif'],
     ['动作三：哑铃弯举', '站姿或坐姿，腰背挺直\n'
                  '两手各持一哑铃放于体侧，屈臂将哑铃举起\n'
                  '前臂与上臂尽量靠拢，稍停然后慢慢放下哑铃至两臂完全伸直', '2_3.gif'],
     ['动作四：锤式弯举', '站姿（或坐姿），手持哑铃垂于体侧，掌心相对，上臂紧贴体侧，肘关节是唯一运动的关节。\n'
                  '用力向上弯举，可感受到肱二头肌外侧膨胀隆起。最高点进行顶峰收缩，并坚持片刻，然后缓慢还原，最低点时手臂完全伸直。\n'
                  '为避免动作过程中身体借力，躯干可稍前倾', '2_4.gif']],
    ['周二训练目标：背+腹', '前两个动作8-12次，后两个动作做20次，每次做3-5组',
     ['动作一：单臂哑铃划船', '下背部保持挺直，腰部不要转动\n'
                    '下放时肩胛骨打开前伸，发力是肩胛骨收紧后缩\n'
                    '顶端保持1~2秒，下放时控制速度', '2_5.gif'],
     ['动作二：双臂哑铃划船', '双脚分开，俯身约90°；双手对握哑铃，拳心相对；手肘微屈，双臂垂直于地面\n'
                    '夹肘上拉哑铃至腹部两侧，在最高点时略作停顿，缓慢下放哑铃至起始位置\n'
                    '动作全程保持肘部夹紧', '2_6.gif'],
     ['动作三：卷腹', '平躺，屈膝，双腿分开与肩同宽，双脚踩实\n'
                '双手扶于两耳旁，用腹肌的力量将肩部和上背部卷离地面，在最高点略作停顿后，缓慢回到起始位置\n'
                '卷腹时，下背部保持紧贴地面，手肘保持向外打开', '2_7.gif'],
     ['动作四：仰卧抬腿', '双手放于臀部下方，伸直双腿，腿下落到约45°即可抬起\n'
                  '腰部始终贴地且不应出现紧张感\n'
                  '抬腿时用下腹的力量将臀部抬离地面', '2_8.gif']],
    ['周四训练目标：肩+肱三头肌', '每个动作8-12次，每次做3-5组',
     ['动作一：哑铃推举', '坐姿或站姿\n'
                  '最低点哑铃与双耳同高，最高点手肘略高于双耳\n'
                  '小臂垂直于地面上下运动\n'
                  '双肩下沉同时后张，手肘略微朝前', '2_9.gif'],
     ['动作二：直立哑铃飞鸟', '两脚开立与肩同宽，胸脯微挺，两手握哑铃从身侧起动\n'
                    '吸气，提肘张肩发力向两侧举臂当哑铃高出肩部后，向上挥腕（掌心向下）\n'
                    '握紧哑铃肘微屈，形成两臂整体用力的构架\n'
                    '缓慢下放还原', '2_10.gif'],
     ['动作三：俯身哑铃飞鸟', '两脚分开站立同肩宽，两手掌心相对各持哑铃，上体向前屈体至与地面平行，两腿稍屈\n'
                    '两手持铃向两侧举起，直至上臂与背部平行（或略为超过），稍停，然后放下哑铃还原\n'
                    '如果在持铃向两侧举起时，使肘和腕部稍微弯屈，你会感到能使三角肌群获到更好的收缩', '2_11.gif'],
     ['动作四：仰卧过项臂屈伸', '仰卧，双脚着地，腹部绷紧。 双手各握一个哑铃，伸直手臂，\n'
                     '肘部弯曲，慢慢将哑铃往下放，至头部的两侧。 往下放哑铃的时候，保持上臂不动\n'
                     '向上伸直双臂，回到起始位置\n'
                     '整个运动过程中，双肘要向身体收紧，不要向外张开', '2_12.gif']],
    ['周五训练目标：臀+腿', '每个动作8-12次，每次做3-5组',
     ['动作一：高脚杯深蹲', '双手捧着哑铃，将哑铃摆在胸前，两手内收，肩胛下压放松,'
                   '双脚与髋关节同宽，下蹲时，膝盖与脚尖方向一致。'
                   '身体重心居中，挺胸、抬头、收腹，屈髋屈膝，同时向下蹲,'
                   '下蹲的深度，根据自己的关节灵活程度和肌肉柔韧性为准', '2_13.gif'],
     ['动作二：哑铃哽拉', '双脚分开，收紧腹部核心，肩膀后缩下沉。'
                  '双手握住哑铃，大臂贴紧身体。'
                  '保持背部挺直，腹部核心收紧，哑铃下放至膝盖下方。'
                  '收紧臀部带动身体站直；拉起后，肩胛骨后缩，夹紧臀部。'
                  '哑铃运动轨迹始终贴近身体。'
                  '髋关节主导运动，膝关节被动弯曲', '2_14.gif'],
     ['动作三：哑铃甩摆', '俯身，保持背部挺直，，双手握紧哑铃，置于膝盖下方。'
                  '收缩臀部和大腿后部使躯干恢复站姿并且把哑铃向上前方带起，直到大臂水平。'
                  '保持膝盖微屈并且手臂自然伸直不参与发力。', '2_15.gif'],
     '在动作过程中，适当把动作速度放慢，这样会比较容易找到肌肉发力感，并且减小惯性，对局部肌肉的训练效果越好。'
     '如果是以增肌为目的，在重量和次数还有组数的选择来讲，应该选择大重量低次数，保证每个动作都做到标准，并每次做到力间歇，而且可以想做的时候就来上几组。'
     '如果是以塑形为目的，可以选择小重量多次数的方式来做。'
     '注意顶峰收缩，要求当某个动作做到肌肉收缩最紧张的位置时，保持一下这种收缩最紧张的状态，做静力性练习，然后慢慢回复到动作的开始位置。'
     '运动健身并不是一天两天就可以见效的事，要根据自身情况有计划地进行，坚持才是王道']]


# data3 = ['本文选取了11个哑铃训练动作，涵盖了上肢、下肢、心肺和核心四个方面，都是多关节大肌群参与,'
#                        '高效锻炼,适合居家练习。',
#          '下肢篇', '深蹲，号称“动作之王”，在健身动作中占据着最重要的位置。所以居家哑铃计划第一个安排的动作就是深蹲了。'
#                 '深蹲主要锻炼的是大腿前侧肌群，以及臀部肌群。'
#          ['高脚杯深蹲','双脚脚跟站距与肩同宽，脚尖自然外展，双手撑住哑铃贴近胸口。吸气匀速下蹲，保持膝盖与脚尖朝向一致，'
#                   '蹲到臀比膝盖略低位置。蹬地吐气站直，动作全程保持核心收紧，腰背挺直。','3_1.gif'],
#           ['深蹲推举','深蹲推举是在深蹲基础上加了一个向上推的动作，不仅可以练到下肢臀、腿肌群，还可以练到肩部肌群，'
#                   '同时也可以提高上下肢的协调性。双手握住哑铃置于肩上，掌心相对，小臂相互平行。吐气向上，伸膝同时伸肘，'
#                   '注意收紧核心稳定住躯干，保持好身体重心稳定在足中处。吸气缓慢下落。', '3_2.gif'],
#          ['过顶深蹲', '过顶深蹲相比于深蹲，可以更好地提高我们核心稳定性，以及肩胛肌群稳定性。动作要点是手臂伸直紧贴耳朵，'
#                   '保持身体重心在足中位置。这个动作难度较大，建议新人从徒手过顶蹲练起。'
#                   '硬拉，同样是一个经典的下肢动作。主要锻炼的是身体的后侧链，也就是臀部和大腿后侧肌群。对于女性翘臀有很大帮助。',
#           '3_3.gif'],
#          ['罗马尼亚硬拉', '双脚站距与髋同宽，双手握住哑铃置于大腿前侧。吸气臀向后，哑铃垂直地面缓慢下放，落到小腿一半位置。'
#                     '吐气时臀部发力向前顶，注意站起时不要耸肩，站直后挺胸展肩。动作全程也要收紧核心，腰背挺直。', '3_4.gif'],
#          ['单腿硬拉', '单腿硬拉和罗马尼亚硬拉技术要点相同，就是由双腿支撑改成单腿支撑，'
#                   '对臀、腿刺激更大，而且还可以提高下肢肌群的稳定性。', '3_5.gif'],
#          '上肢篇', '',
#          ['地板推胸', '地板卧推，主要锻炼胸部和大臂后侧肌群。仰卧屈膝，双脚踩住地面，下背部贴住地面。'
#                   '双手握住哑铃贴近胸口，向上发力吐气推起哑铃，感受胸部收缩，吸气缓慢下落。', '3_6.gif'],
#          ['哑铃划船', '划船是锻炼背部和大臂前侧肌群的动作。双脚站距与髋同宽，屈髋俯身，双手握住哑铃置于膝盖两侧。'
#                   '发力吐气向上顶肘，感受背部收缩，吸气缓慢下落。动作过程中同样保持核心收紧，腰背挺直。', '3_7.gif'],
#          ['单臂划船', '单臂划船是一侧手支撑在椅子上，所以对下背部的压力更小。由于是单侧发力，身体对于背部肌群的控制会更加灵敏，'
#                   '更有利于找到背部发力感觉。', '3_8.gif'],
#          ['哑铃弯举推举', '这个动作其实是由两部分组成。二头弯举+竖直推举，也就是同时锻炼到大臂前侧肌群和肩部肌群。'
#                     '两个动作加在一起更为高效。'
#                     '首先是双脚站距与肩同宽，臀、腹收紧，稳定住躯干，双手握住哑铃，掌心朝向前方，手臂自然伸直置于身体两侧。'
#                     '第一阶段，固定肘关节，屈肘将哑铃拉起至与肩同高位置，此时掌心朝向自己。'
#                     '第二阶段再将哑铃竖直向上推起，手臂伸直，掌心朝前。两个阶段注意保持动作连贯。'
#                     '哑铃以原轨迹下落，向上发力吐气，向下吸气。', '3_9.gif'],
#          '心肺篇', '',
#          ['哑铃swing', '双脚站距比肩略宽，双手握住哑铃，手臂自然下垂。吸气俯身大幅度屈髋，小幅度屈膝，哑铃顺势向后拉。'
#                      '吐气伸髋伸膝站直，哑铃顺势推起。屈伸髋动作需保持连贯性，动作过程中核心收紧，腰背挺直。', '3_10.gif'],
#          '核心篇', '',
#          ['平板划船', '平板划船过程中可以充分激活核心肌群稳定性的功能。首先，双手握住哑铃置于肩关节正下方，'
#                   '双脚距离宽一些保持髋关节稳定，臀部与地面平行。在保持身体稳定的状态下加上单臂划船动作。', '3_11.gif'],
#          '每个动作组间休息30s，做完一项休息1分钟再做下一项。上面的计划只包含了正式的训练动作，关于热身和拉伸动作。']

class LeftTabWidget(QtWidgets.QWidget):
    """左侧选项栏"""

    def __init__(self, parent):
        super(LeftTabWidget, self).__init__(parent)
        # self.setObjectName('LeftTabWidget')
        # self.setWindowTitle('LeftTabWidget')
        self.parent = parent
        self.data_list = None
        self.list_style = """
            QListWidget, QListView, QTreeWidget, QTreeView {
                outline: 0px;
                border-width: 1px;
                border-color: #999999;
                border-collapse: collapse;
            }
            QListWidget {
                font-size:17px;
                font-weight:bold;
                font-family:verdana,arial,Roman times;
                min-width: 120px;
                max-width: 240px;
                color: green;
                background: #F5F5F5;
                /*background: green;*/
            }
            QListWidget::Item:selected {
                color:blue;
                background: skyblue;
                border-left: 5px solid red;
            }
            HistoryPanel:hover {
                background: rgb(52, 52, 52);
            }
            """

        self.main_layout = QtWidgets.QHBoxLayout(self, spacing=0)  # 窗口的整体布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = QtWidgets.QListWidget()  # 左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        # self.right_widget = QtWidgets.QStackedWidget()
        # self.main_layout.addWidget(self.right_widget)

    def _setup_ui(self):
        """加载界面ui"""
        # self.left_widget.currentRowChanged.connect(self.slot_current_row_changed)  # list和右侧窗口的index对应绑定
        self.left_widget.clicked.connect(self.slot_clicked)  # 双击列表控件时发出信号
        # for each in self.plans:
        #     self.wl_plans.addItem(each[0])
        # self.wl_plans.setCurrentRow(0)

        self.left_widget.setFrameShape(QtWidgets.QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        for i in range(len(self.data_list)):
            self.item = QtWidgets.QListWidgetItem(self.data_list[i], self.left_widget)  # 左侧选项的添加
            self.item.setSizeHint(QtCore.QSize(30, 60))
            self.item.setTextAlignment(QtCore.Qt.AlignCenter)  # 居中显示

            # self.browser = QtWebEngineWidgets.QWebEngineView()  # 右侧用QWebView来显示html网页
            # self.browser.setUrl(QtCore.QUrl.fromLocalFile('C:/Users/big/Desktop/tt/%s' % url_list[i]))
            # # self.right_widget.addWidget(self.browser)
            # self.right_widget.addWidget(QtWidgets.QLabel(f'tu pian a {i}'))

    def set_date(self, data_list):
        self.data_list = data_list
        self._setup_ui()

    # def slot_current_row_changed(self, row):
    #     print(type(row), row)
    #     self.parent.slot_plan_selected(row)

    def slot_clicked(self):
        row = self.left_widget.currentRow()
        self.parent.slot_plan_selected(row)


# class BaiDuAI(object):
#     """ 你的 APPID AK SK """
#     APP_ID = '15289879'
#     API_KEY = 'Uwaa5zMsdq0KmXygY2EZCWyO'
#     SECRET_KEY = 'wP9aCnyB0byI4Zra7TzZc7k3PdWNfXaf'
#
#     def __init__(self):
#         self.client = AipSpeech(BaiDuAI.APP_ID, BaiDuAI.API_KEY, BaiDuAI.SECRET_KEY)
#         # print(type(self.client))
#         self.vol = 5
#         self.person = 3
#         self.speed = 7
#
#     def __str__(self):
#         return "百度智能"
#
#     def setArgs(self, args):
#         assert args, '默认参数'
#         self.vol = args[0] if 0 <= args[0] <= 15 else 5
#         self.person = args[1] if 0 <= args[1] <= 4 else 3
#         self.speed = args[2] if 0 <= args[2] <= 15 else 7
#
#     def talking(self, essay='你好百度'):
#         try:
#             print(essay)
#             # 详细参数可看python sdk 文档
#             args = {'vol': self.vol,  # 音量，取值0-15，默认为5中音量
#                     'per': self.person,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
#                     'spd': self.speed, }  # 语速，取值0-15，默认为5中语速
#             result = self.client.synthesis(essay, 'zh', 1, args)
#             print(type(result), result)
#         except Exception as e:
#             print(e)
#
#         # # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
#         # if not isinstance(result, dict):
#         #     with open('audio.mp3', 'wb') as f:
#         #         f.write(result)
#         # # 在工程目录下,就可以看到 audio.mp3 这个文件了,来听一听


class Talker(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Talker, self).__init__(*args, **kwargs)
        self.data = args

        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # self.speaker = pyaudio.PyAudio()  # 创建一个播放器

        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True

        self.is_do = True

    def setData(self, msg):
        print(msg)
        self.data = msg
        # self.speaker.rate = 2

    def run(self):
        print("run")
        while self.is_do and self.data:
            self.__flag.wait()
            print('I am running...')
            # time.sleep(2)

            # 播放
            self.speaker(self.data)

            self.data = ''

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞
        print("pause")

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞
        print("resume")

    def stop(self):
        # self.__flag.set()  # 将线程从暂停状态恢复, 如果已经暂停的话（要是停止的话我就直接让他停止了，干嘛还要执行这一句语句啊，把这句注释了之后就没有滞后现象了。）
        print('I am stopping it...')
        self.is_do = False

    # def restart(self):
    #     self.is_do


class Speaker(object):
    def __init__(self, *args, **kwargs):
        # super(Speaker, self).__init__(*args, **kwargs)
        self.data = args

        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

    def talk(self, msg):
        # time.sleep(1)
        self.speaker.Speak(msg)


class SportsPlan(QtWidgets.QFrame):
    def __init__(self, parent=None, pwd_size=8):
        super(SportsPlan, self).__init__(parent)

        # <editor-fold desc="数据声明">
        self.plans = []  # 锻炼计划
        self.cur_plan = -1  # 选中的锻炼计划
        self.summaries = []  # 每天所有锻炼动作的总体要求
        self.actions = []  # 每天的锻炼动作

        self.dir = r'C:\Users\big\Desktop\15图'
        # self.talker = Talker()
        # self.ai_speaker = BaiDuAI()
        # self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.engine = pyttsx3.init()  # 初始化语音库
        # self.schedule = sched.scheduler(time.time, time.sleep)  # scheduler的两个参数用法复杂,可以不做任何更改
        # </editor-fold>

        # <editor-fold desc="窗体控件声明">


        self.toolbar = QtWidgets.QToolBar(self.tr("工具栏"))  # 工具栏
        self.wl_plans = LeftTabWidget(self)
        self.stage = QtWidgets.QFrame()
        self.lb_title = QtWidgets.QLabel()  # 每个锻炼计划的标题及意义
        self.lb_summary = QtWidgets.QLabel()  # 当日提示
        self.lb_gist = QtWidgets.QLabel()  # 锻炼步骤
        self.lb_img = QtWidgets.QLabel()  # 锻炼动图
        self.movie = QtGui.QMovie()  # 锻炼动图

        # # QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(Qt.QUrl.fromLocalFile('test.mp4')))
        #
        # # Set widget
        # self.videoWidget = QVideoWidget()
        # self.videoWidget.setGeometry(self.pos().x(), self.pos().y(), self.width(), self.height())
        # self.setCentralWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)
        #
        # # Play
        # self.media.prepare_audio("一百万个可能.mp3")
        #
        # self.mediaPlayer.play()

        lh = QtWidgets.QHBoxLayout()  # 展示区
        lh.addWidget(self.lb_gist)
        lh.addStretch()
        lh.addWidget(self.lb_img)
        lh.addStretch()

        lv = QtWidgets.QVBoxLayout(self.stage)
        lv.addWidget(self.lb_title)
        lv.addWidget(self.lb_summary)
        lv.addStretch()
        lv.addLayout(lh)
        lv.addStretch()

        lh_main = QtWidgets.QHBoxLayout(spacing=0)
        # lh_main.setContentsMargins(0, 0, 0,0)
        lh_main.addWidget(self.wl_plans)
        lh_main.addWidget(self.stage)

        main_lv = QtWidgets.QVBoxLayout(self)
        main_lv.addWidget(self.toolbar)
        main_lv.addLayout(lh_main)
        main_lv.setContentsMargins(0, 0, 0, 0)
        # </editor-fold>

        self.data_stores()
        self.initialize()

    def data_stores(self):
        # 计划名称，简介，周期，间隔天数
        self.plans = [
            ('一副哑铃练全身', '    大部分的初学者都会选择哑铃来锻炼身体，这套计划用15个哑铃动作锻炼全身各个部位。'
                        '适合体格不太健壮的初级达人。30天一个周期，不间歇。', 30, 0),
            ('30天新手全身训练计划', '    真男人，练就男性完美身材。肌肉是支撑人体结构的重要组织，'
                            '全身肌肉共有600余块，约占体重的40％。力量训练可以提升体内肌肉生长激素的含量。'
                            '这几个动作可以全面的练到身体各个部位！包括胸，背，肩，肱二，肱三，腿！', 30, 0),
            ('一周哑铃训练计划', '要好身材不是说少吃点，多动点就能做到的.而想要玲珑好身材，就一定人有力量训练。'
                         '一周哑铃训练计划，每周4次，每次4个动作，在家打造完美身材，效果丝毫不逊健身房。', 7, 1),
            ('居家哑铃高效训练计划', '', 0, 0)]
        # 日日念念
        self.summaries = [
            ('每个动作为一组，每组1-2分钟，组间休息30s，记得练习!', ['0.jpg', '1.png']),
            ('每个动作10-15次，循环2-3组。训练过程每个动作尽量慢一点，动作都做到位，体会每个肌群的发力。', ['1.png', '0.jpg']),
            ('每周4次，每次4个动作，在家打造完美身材。', ['0.jpg', '1.png']),
            ('每周只需要练4次，每次只需要4个动作，每个动作8-12次，每次做3-5组，', ['0.jpg', '1.png'])]

        # 组数，次数，休息时间，动作(名称、要领、动图示范)
        self.actions = [[3, 5, 10, [['动作1、哑铃弯举+肩推', '训练肱二、三头肌、三角肌前束、中束；', '1_1.gif'],
                                    ['动作2、哑铃弯举+深蹲', '训练臀腿+肱二头肌，促睾就练腿。', '1_2.gif'],
                                    ['动作3、哑铃划船', '训练肩背部、手臂肌群', '1_3.gif'],
                                    ['动作4、负重行走', '别小看这个动作，这是提高体能的最原始方法之一。', '1_4.gif'],
                                    ['动作5、深蹲推举', '训练臀腿、手臂肌肉，几乎可以锻炼到全身70%肌肉，很有难度的动作。', '1_5.gif'],
                                    ['动作6、哑铃摇摆', '训练身体后侧中断肌肉、心肺功能。男的建议10-15kg，女的6-8kg。', '1_6.gif'],
                                    ['动作7、哑铃卧推', '训练胸大肌、二三头肌', '1_7.gif'],
                                    ['动作8、仰卧上拉', '训练背阔肌、胸大肌、三角肌后束、核心肌肉群', '1_8.gif'],
                                    ['动作9、仰卧负重卷腹', '训练腰腹核心肌群。', '1_9.gif']]],
                        []]

        # dumbbell = None

    def initialize(self):
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.resize(1200, 800)

        font = QtGui.QFont('Times New Roman', 14)
        self.setFont(font)

        # 工具栏
        # action = QtWidgets.QAction(QtGui.QIcon('./res/images/1.png'), '启动计划', self)
        # action.setShortcut('Ctrl+Q')
        # action.triggered['QAction*'].connect(self.slot_actions_triggered)
        action0 = QtWidgets.QAction('热身', self)
        action0.setToolTip('运动前要做好动态拉伸')
        action1 = QtWidgets.QAction('开始', self)
        action2 = QtWidgets.QAction('暂停', self)
        action3 = QtWidgets.QAction('继续', self)
        action4 = QtWidgets.QAction('终止', self)
        action9 = QtWidgets.QAction('放松', self)
        action9.setToolTip('运动后要做好静态拉伸')

        self.toolbar.setIconSize(QtCore.QSize(16, 16))
        self.toolbar.addAction(action0)
        self.toolbar.addSeparator()
        self.toolbar.addActions([action1, action2, action3, action4])
        self.toolbar.addSeparator()
        self.toolbar.addAction(action9)

        self.wl_plans.setFixedWidth(200)
        data = np.array(self.plans)
        self.wl_plans.set_date(data[:, 0])

        # self.stage.setFixedWidth(self.width)
        self.stage.setFrameStyle(2)

        self.lb_title.setMinimumHeight(40)
        # self.lb_summary.setFixedWidth(self.width)
        # self.lb_gist.setFixedWidth(self.width // 2)
        self.lb_title.setWordWrap(True)
        self.lb_title.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
        self.lb_title.setStyleSheet(
            "QLabel{background:white;color:rgba(255,0,0,255);}"
            "QLabel{font-size:24px;font-weight:bold;font-family:Roman times;}"
            "QLabel:hover{color:blue;}")
        self.lb_summary.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_summary.setWordWrap(True)
        self.lb_summary.setStyleSheet(
            "QLabel{background:white;color:blue;}"
            "QLabel{font-size:24px;font-weight:bold;font-family:Roman times;}"
            "QLabel:hover{color:skyblue;}")

        self.lb_gist.setWordWrap(True)

        self.lb_img.setAlignment(QtCore.Qt.AlignCenter)
        # self.lb_img.setStyleSheet("border: 2px solid blue")
        # self.lb_img.setScaledContents(True)
        self.lb_img.setMovie(self.movie)
        # 设置GIF位置以及大小---和label一致
        self.movie.setScaledSize(self.lb_img.size())
        # speed = self.movie.speed()
        # print(speed)
        # self.movie.setSpeed(100)

        self.toolbar.actionTriggered.connect(self.slot_actions_triggered)
        # self.bt_begin.pressed.connect(self.slot_begin_clicked)

        # self.engine = pyttsx3.init()  # 初始化语音库
        self.engine.setProperty('rate', self.engine.getProperty('rate') - 50)  # 设置语速
        self.engine.setProperty('volume', self.engine.getProperty('volume') + 5)  # 设置音量

        voices = self.engine.getProperty('voices')  # 选择语音
        # for voice in voices:
        #     print(voice.id, voice.languages)
        self.engine.setProperty("voice", voices[0].id)

    # def update_UI(self):
    #     summary = self.summaries[self.cur_plan]
    #     self.lb_summary.setText(summary)
    #
    #     self.lb_gist.setVisible(True)
    #
    #     """
    #     第一个参数是一个整数或浮点数，代表多少秒后执行这个action任务
    #     第二个参数priority是优先级，0 代表优先级最高，1 次之，2 次次之，当两个任务是预定在同一个时刻执行时，根据优先级决定谁先执行。
    #     第三个参数就是你要执行的任务，可以简单理解成你要执行任务的函数的函数名
    #     第四个参数是你要传入这个定时执行函数名函数的参数，最好用括号包起来，
    #     如果只传入一个 参数的时候用括号包起来，该参数后面一定要加一个逗号，如果不打逗号，会出现错误。
    #     """
    #     for i in range(2):
    #         dalay = 3
    #         self.schedule.enter(i * dalay, 0, self._motioning, (i,))

    # 播放语音
    def _talking(self, msg_list):
        print(msg_list)
        # self.speaker.Speak(msg_list)
        # for each in msg_list:
        #     # print('dd', type(each), each)
        #     self.speaker.Speak(each)  # speak() pause()暂停 resume() 继续

        for each in msg_list:
            self.engine.say(each)  # 读的内容
            # time.sleep(2)
        self.engine.runAndWait()

        # self.engine.endLoop()  # 朗读一次
        self.engine.stop()

    # 界面更新
    def _update_motion(self):
        act_id = 0
        tip = '\n\t'.join(self.actions[self.cur_plan][3][act_id][:2])
        self.lb_gist.setText(tip)
        self.lb_gist.setVisible(True)

        path = os.path.join(self.dir, self.actions[self.cur_plan][3][act_id][2])
        self.movie.setFileName(path)
        # self.movie.setSpeed(self.movie.speed() -100)
        self.lb_img.setMovie(self.movie)
        self.movie.start()

        # print(path, tip, self.movie.speed())

    # 动作更新
    def _update_face(self, msg):
        print(msg)
        # 当前计划的介绍
        self.lb_title.setText(self.plans[self.cur_plan][1])
        self.lb_summary.setText(self.summaries[self.cur_plan][0])

        self.lb_gist.setVisible(False)

        file = os.path.join(self.dir, self.summaries[self.cur_plan][1][0])
        self.lb_img.setPixmap(QtGui.QPixmap(file))

    def slot_actions_triggered(self, action):
        order = action.text()
        # print(type(action), order)
        if order == '热身':
            path = os.path.join(self.dir, '运动前动态拉伸动作.mp4')
            print('动态拉伸', path)
            os.startfile(path)  # 利用系统调用默认程序打开本地文件

            # cap = cv2.VideoCapture(path)
            # while cap.isOpened():
            #     ret, frame = cap.read()
            #     # if frame is read correctly ret is True
            #     if not ret:
            #         print("Can't receive frame (stream end?). Exiting ...")
            #         break
            #
            #     cv2.imshow('frame', frame)
            #     if cv2.waitKey(40) & 0xFF == ord('q'):
            #         break
            #
            # cap.release()
            # cv2.destroyAllWindows()
            return

        # if True:
        #     self.movie.stop()

        # if self.cur_plan == 0:
        #     path = os.path.join(self.dir, '0.jpg')
        #     print(path)
        #     self.lb_img.setPixmap(QtGui.QPixmap(path))
        # else:
        #     path = os.path.join(self.dir, f'{self.cur_plan}.gif')
        #     print(path, self.cur_plan)
        #     self.movie.setFileName(path)
        #     # self.movie.setSpeed(self.movie.speed() -100)
        #     self.lb_img.setMovie(self.movie)
        #     self.movie.start()
        # self.cur_plan += 1
        # return

        if self.cur_plan < 0:
            AnimWin('请选择运动计划')
            return

        if order == '开始':
            self._update_motion()

    def slot_plan_selected(self, index):
        self.lb_gist.setVisible(False)
        self.cur_plan = index  # self.wl_plans.currentRow()
        # print(self.cur_plan)

        # 第一个参数是一个整数或浮点数，代表多少秒后执行这个action任务
        # 第二个参数priority是优先级，0 代表优先级最高，1 次之，2 次次之，
        # 当两个任务是预定在同一个时刻执行时，根据优先级决定谁先执行。
        # 第三个参数就是你要执行的任务，可以简单理解成你要执行任务的函数的函数名
        # 第四个参数是你要传入这个定时执行函数名函数的参数，最好用括号包起来，
        # 如果只传入一个 参数的时候用括号包起来，该参数后面一定要加一个逗号，如果不打逗号，会出现错误。
        # 设置两个定时任务的调度
        # self.schedule.enter(0, 0, self._update_face, ("界面更新",))
        # self.schedule.enter(1, 2, self._talking, (msg_list,))  # 被调用触发的函数的参数tuple，只有一个参数就(xx,)
        # self.schedule.run()  # 运行。注意sched模块不是循环的，一次调度被执行后就Over了，如果想再执行，请再次enter
        # while True:
        #     time.sleep(100)

        if self.engine.isBusy():
            # self.engine.endLoop()
            self.engine.stop()

        msg_list = self.plans[self.cur_plan][:2]

        # 多线程执行定时任务
        Timer(0, self._update_face, ("界面更新",)).start()
        # Timer(1, self._talking, (msg_list,)).start()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = SportsPlan()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
