#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Project : Puck
#  File    : test3
#  Date    : 2020/7/14 1:06
#  Site    : https://github.com/eastdorado
#  Author  : By cyh
#            QQ: 260125177
#            Email: 260125177@qq.com 
#  Copyright = Copyright (c) 2020 CYH
#  Version   = 1.0

import os
import sys
import copy
import math
from random import randint
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utilities import Utils, EllipseButton
from functools import partial
import win32gui
import win32api
import win32con

# sys.setrecursionlimit(10000)


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QtWidgets.QStyleOptionViewItem.Right
        super(ItemDelegate, self).paint(painter, option, index)


# 样式管理类
class StyleSheet(object):
    """
           设置窗口边框圆角时有两种方式，一种是设置样式，另一种是在paintEvent事件中绘制窗口
                    border-radius 属性，关于这个属性，可选的样式有
                    border-top-left-radius 设置左上角圆角;
                    border-top-right-radius 设置右上角圆角;
                    border-bottom-left-radius 设置左下角圆角;
                    border-bottom-right-radius 设置右下角圆角;
                    border-radius 设置四个角圆角;
                        border-radius:15px 一个参数
                        border-radius: 15px 50px  两个参数 第一个参数设置X轴方向的半径 第二个参数设置Y轴方向的半径

                    设置无边框或者背景透明可以去掉按钮的白色方框
                    给按钮设置如下样式即可。
                    {background-color:transparent;}
                    或者
                    {border:none;}

            图片是白色半透明，作为子窗体的底图，则子窗体半透明，上面控件不透明。
            实现底图半透明化
            # Tool_Widget{
            border - radius: 10
            px;
            border - image: url(img / toolbg.png)
            }
        """
    GoodStyle = ['''/* === Shared === */
QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {
    background-color: #222222;
    color: #BBBBBB;
    font-family: "Segoe UI";
}

/* === QWidget === */
QWidget:window {
    background: #222222;
    color: #BBBBBB;
    font-family: "Segoe UI";
}

/* === QToolTip === */
QToolTip {
    background-color: #000000;
    border: 2px solid #333333;
    color: yellow;
}

/* === QPushButton === */
QPushButton {
    border: 1px solid #333333;
    padding: 4px;
    min-width: 65px;
    min-height: 12px;
}

QPushButton:hover {
    background-color: #333333;
    border-color: #444444;
}

QPushButton:pressed {
    background-color: #111111;
    border-color: #333333;
    color: yellow;
}

QPushButton:disabled {
    color: #333333;
}

/* === Checkable items === */
QCheckBox::indicator, QRadioButton::indicator, QTreeView::indicator {
    width: 16px;
    height: 16px;
    background-color: #111111;
    border: 1px solid #333333;
}

QRadioButton::indicator {
    border-radius: 8px;
}

QCheckBox::indicator::checked, QRadioButton::indicator::checked, QTreeView::indicator::checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #111111);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled {
    background-color: #444444;
}

QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled {
    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #444444);
}

/* === QComboBox === */
QComboBox {
    background-color: black;
    border: 1px solid #333333;
    color: white;
    padding:1px 2em 1px 3px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-left: 1px solid #333333;
}

QComboBox::down-arrow {
    border: 2px solid #333333;
    width: 6px;
    height: 6px;
    background: #5f5f5f;
}

/* === QGroupBox === */
QGroupBox {
    border: 2px solid #333333;
    margin-top: 2ex;
}

QGroupBox::title {
    color: yellow;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    margin-left: 5px;
}

/* === QTabWidget === */
QTabWidget::pane {
    background: #222222;
    border: 2px solid #333333;
}

/* === QTabBar === */
QTabBar::tab {
    background: transparent;
    border: 1px solid #333333;
    border-bottom: none;
    color: #BBBBBB;
    padding-left: 5px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 3px;
}

QTabBar::tab:hover {
    background-color: #333333;
    border: 1px solid #444444;
    border-bottom: none;
}

QTabBar::tab:selected {
    background-color: #111111;
    border: 1px solid #333333;
    border-top: 1px solid yellow;
    border-bottom: none;
    color: yellow
}

/* === QToolBar === */
QToolBar {
    background-color: #222222;
    border: none;
    padding: 1px;
}

QToolBar:handle {
    background: #222222;
    border-left: 1px dotted yellow;
    color: #BBBBBB;
}

QToolBar::separator {
    width: 6px;
    background-color: #222222;
}

/* === QToolButton === */
QToolButton {
    border: 1px solid #333333;
    margin: 1px;
}

QToolButton:hover {
    background-color: #333333;
    border: 1px solid #444444;
}

QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
    padding-right: 20px; /* make way for the popup button */
}

QToolButton::menu-button {
    border-left: 1px solid #333333;
    background: transparent;
    width: 16px;
}

QToolButton::menu-button:hover {
    border-left: 1px solid #444444;
    background: transparent;
    width: 16px;
}

QToolButton:checked, QToolButton:pressed {
    background-color: #111111;
    color: yellow;
}

/* === QMenu === */
QMenu {
    background-color: black;
    border: 1px solid gray;
    color: white;
    padding: 1px;
}

QMenu::item {
    padding: 2px 25px 2px 20px;
    border: 1px solid transparent;
}

QMenu::item:disabled {
    color: #666666;
}

QMenu::item:selected {
    border-color: gray;
    background: #222222;
}

QMenu::icon:checked {

}

QMenu::separator {
    height: 1px;
    background: #222222;
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 1px;
    margin-bottom: 1px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}

/* === QMenuBar === */
QMenuBar {
    background-color: black;
    color: white;
}

QMenuBar::item {
    background: transparent;
}

QMenuBar::item:disabled {
    color: gray;
}

QMenuBar::item:selected {
    background: #222222;
}

QMenuBar::item:pressed {
    background: #444444;
}
 
/* === QScrollBar:vertical === */
QScrollBar:vertical {
    background: #111111;
    width: 16px;
    margin: 16px 0 16px 0;
}

QScrollBar::handle:vertical {
    background: #555555;
    min-height: 16px;
}

QScrollBar::add-line:vertical {
    background: #444444;
    height: 16px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    background: #444444;
    height: 16px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:up-arrow:vertical, QScrollBar:down-arrow:vertical {
    border: 2px solid #333333;
    width: 6px;
    height: 6px;
    background: #5f5f5f;
}

/* === QScrollBar:horizontal === */
QScrollBar:horizontal {
    background: #111111;
    height: 16px;
    margin: 0 16px 0 16px;
}

QScrollBar::handle:horizontal {
    background: #555555;
    min-width: 16px;
}

QScrollBar::add-line:horizontal {
    background: #444444;
    width: 16px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    background: #444444;
    width: 16px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:left-arrow:horizontal, QScrollBar:right-arrow:horizontal {
    border: 2px solid #333333;
    width: 6px;
    height: 6px;
    background: #5f5f5f;
}

/* =================== */
QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox {
    background-color: black;
    color: #BBBBBB;
    border: 1px solid #333333;
}

QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox {
    border-color: #333333;
    border: 1px solid #333333;

}

/* === QHeaderView === */
QHeaderView::section {
    background: #222222;
    border: 0;
    color: #BBBBBB;
    padding: 3px 0 3px 4px;
}

/* === QListView === */
QListView::item:hover {
    background: #333333;
}

QListView::item:selected {
    background: #111111;
    color: yellow;
}

/* === QTableView === */
QTableView::item:hover {
    background: #333333;
}

QTableView::item:hover {
    background: #111111;
    color: yellow;
}

/* === QTreeView === */
QTreeView::item {
    background: black;
}

QTreeView::item:hover {
    background: #333333;
}

QTreeView::item:selected {
    background: #111111;
    color: yellow;
}

QTreeView::branch {

}

QTreeView::branch:has-siblings:adjoins-item {

}

QTreeView::branch:has-siblings:!adjoins-item {

}

QTreeView::branch:closed:has-children:has-siblings {

}

QTreeView::branch:has-children:!has-siblings:closed {

}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {

}

QTreeView::branch:open:has-children:has-siblings {

}

QTreeView::branch:open:has-children:!has-siblings {

}

/* === Customizations === */
QFrame#infoLabel {
    border: 1px inset #333333;
}

2.
.QWidget {
   background-color: beige;
}

QToolBar {
    background-color: beige;
}

QDialog, QFileDialog {
    background-color: beige;
}

QTabWidget::pane { /* The tab widget frame */
    border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
    left: 5px; /* move to the right by 5px */
}

QTabBar, QTabWidget {
    background-color: beige;
}
QTabBar::tab {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
     border: 1px solid darkkhaki;
     border-bottom-color: #C2C7CB; /* same as the pane color */
     border-top-left-radius: 4px;
     border-top-right-radius: 4px;
     min-width: 8ex;
     padding: 2px;
 }
QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB; /* same as pane color */
}

QTabBar::tab:!selected {
    margin-top: 2px; /* make non-selected tabs look smaller */
}

/* Nice Windows-XP-style password character. */
QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

QHeaderView::section {
     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                       stop:0 #616161, stop: 0.5 #505050,
                                       stop: 0.6 #434343, stop:1 #656565);
     color: white;
     padding-left: 4px;
     border: 1px solid #6c6c6c;
 }

 QHeaderView::section:checked
 {
     background-color: red;
 }


/* We provide a min-width and min-height for push buttons
   so that they look elegant regardless of the width of the text. */
QPushButton {
    background-color: palegoldenrod;
    border-width: 2px;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 5;
    padding: 3px;
    min-width: 9ex;
    min-height: 2.5ex;
}

QPushButton:hover {
   background-color: khaki;
}

/* Increase the padding, so the text is shifted when the button is
   pressed. */
QPushButton:pressed {
    padding-left: 5px;
    padding-top: 5px;
    background-color: #d0d67c;
}

QLabel, QAbstractButton {
    font: bold;
}

/* Mark mandatory fields with a brownish color. */
.mandatory {
    color: brown;
}

/* Bold text on status bar looks awful. */
QStatusBar QLabel {
   font: normal;
}

QStatusBar::item {
    border-width: 1;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 2;
}

QStackedWidget, QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView, QWebView, QTreeView, QHeaderView {
    background-color: cornsilk;
    selection-color: #0a214c; 
    selection-background-color: #C19A6B;
}

QListView {
    show-decoration-selected: 1;
}

QListView::item:hover {
    background-color: wheat;
}

/* We reserve 1 pixel space in padding. When we get the focus,
   we kill the padding and enlarge the border. This makes the items
   glow. */
QLineEdit, QFrame {
    border-width: 1px;
    padding: 1px;
    border-style: solid;
    border-color: darkkhaki;
    border-radius: 5px;
}

/* As mentioned above, eliminate the padding and increase the border. */
QLineEdit:focus, QFrame:focus {
    border-width: 3px;
    padding: 0px;
}

/* A QLabel is a QFrame  */
QLabel {
    border: none;
    padding: 0;
    background: none;
}

/* A QToolTip is a QLabel  */
QToolTip {
    border: 2px solid darkkhaki;
    padding: 5px;
    border-radius: 3px;
    opacity: 200;
}

/* Nice to have the background color change when hovered. */
QRadioButton:hover, QCheckBox:hover {
    background-color: wheat;
}

/* Force the dialog's buttons to follow the Windows guidelines. */
QDialogButtonBox {
    button-layout: 0;
}


3.
/*
    Style by evilworks, 2012-2013. pollux@lavabit.com
    This file is Public Domain.
*/

/* === Shared === */
QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog, QTabBar {
    font-family: "Segoe UI";
    background-color: #888;
    color: #000;
}

/* === QWidget === */
QWidget:window {
    font-family: 'Segoe UI';
    background-color: #888;
}

/* === QPushButton === */
QPushButton {
    border: 1px solid #555;
    padding: 4px;
    min-width: 65px;
    min-height: 12px;
}

QPushButton:hover {
    background-color: #999;
}

QPushButton:pressed {
    background-color: #333;
    border-color: #555;
    color: #AAA;
}

QPushButton:disabled {
    color: #333333;
}

/* === QComboBox === */
QComboBox {
    background-color: #AAA;
    border: 1px solid #555;
    color: black;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-left: 1px solid #333333;
}

/* === QGroupBox === */
QGroupBox {
    border: 1px solid #555;
    margin-top: 2ex;
}

QGroupBox::title {
    color: black;
    subcontrol-origin: margin;
    subcontrol-position: top left;    
    border: 1px solid #555;
}

/* === QTabBar === */
QTabBar::tab {
    border-bottom: none;
    color: #000;
    padding: 4px;
    background-color: #888;
    border: 1px solid #555;
}

QTabBar::tab:hover {
    background-color: #AAA;
}

QTabBar::tab:selected {
    background-color: #000;
    color: white;
}

/* === QTabWidget === */
QTabWidget::pane {
    background: #888;
    border: 1px solid #555;
}


/* === QToolBar === */
QToolBar {
    background: #949494;
    border: none;
    padding-left: 0px;
    padding-right: 0px;
    margin: 2px;
}

QToolBar::separator {
    width: 1px;
    margin-left: 3px;
    margin-right: 3px;
    background-color: #555;
}

/* === QToolButton === */
QToolButton {
    border: 1px solid #666;
    margin: 1px;
}

QToolButton:hover {
    background-color: #AAA;
}

QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
    padding-right: 20px; /* make way for the popup button */
}

QToolButton::menu-button {
    border-left: 1px solid #666;
    background: transparent;
    width: 16px;
}

QToolButton::menu-button:hover {
    border-left: 1px solid #666;
    background: transparent;
    width: 16px;
}

QToolButton:checked, QToolButton:pressed {
    background-color: #000;
    border: 1px solid #555;
    color: white;
}

/* === QScrollBar:vertical === */
QScrollBar:vertical {
    width: 16px;
    margin: 16px 0 16px 0;
    background: #333;
}

QScrollBar::handle:vertical {
    background: #888;
    min-height: 16px;
    border-top: 1px solid #666;
    border-bottom: 1px solid #666;
}

QScrollBar::add-line:vertical {
    background: #888;
    height: 16px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    background: #888;
    height: 16px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/* === QScrollBar:horizontal === */
QScrollBar:horizontal {
    height: 16px;
    margin: 0 16px 0 16px;
    background: #333;
}

QScrollBar::handle:horizontal {
    background: #888;
    min-width: 16px;
    border-left: 1px solid #666;
    border-right: 1px solid #666;
}

QScrollBar::add-line:horizontal {
    background: #888;
    width: 16px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    background: #888;
    width: 16px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* === QMenu === */
QMenu {
    background-color: black;
    border: 1px solid gray;
    color: white;
    padding: 1px;
}

QMenu::item {
    padding: 2px 25px 2px 20px;
    border: 1px solid transparent;
}

QMenu::item:disabled {
    color: #666666;
}

QMenu::item:selected {
    border-color: gray;
    background: #222222;
}

QMenu::icon:checked {

}

QMenu::separator {
    height: 1px;
    background: #222222;
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 1px;
    margin-bottom: 1px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}

/* === QMenuBar === */
QMenuBar {
    background-color: black;
    color: white;
}

QMenuBar::item {
    background: transparent;
}

QMenuBar::item:disabled {
    color: gray;
}

QMenuBar::item:selected {
    background: #222222;
}

QMenuBar::item:pressed {
    background: #444444;
}
/* =================== */
QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox {
    background-color: #AAA;
    color: #000;
    border: 1px solid #555;
}

QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox {
    border: 1px solid #555;
}

/* === QHeaderView === */
QHeaderView::section {
    height: 20px;
}

QHeaderView::section {
    background: #666;
    border: 0;
    color: #000;
    padding-left: 4px;
}

/* === QListView === */
QListView::item:hover {
    background: #AAA;
}

QListView::item:selected {
    background: #333;
    color: #AAA;
}

/* === QTableView === */
QTableView::item:hover {
    background: #333333;
}

QTableView::item:hover {
    background: #111111;
    color: yellow;
}

/* === QTreeView === */
QTreeView::item {
    background: #AAA;
}

QTreeView::item:hover {
    background: #CCC;
}

QTreeView::item:selected {
    background: #333;
    color: #AAA;
}

QTreeView::branch {

}

QTreeView::branch:has-siblings:adjoins-item {

}

QTreeView::branch:has-siblings:!adjoins-item {

}

QTreeView::branch:closed:has-children:has-siblings {

}

QTreeView::branch:has-children:!has-siblings:closed {

}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {

}

QTreeView::branch:open:has-children:has-siblings {

}

QTreeView::branch:open:has-children:!has-siblings {

}
''']
    # 美化样式表
    Stylesheets = [
        """     /*******************主窗体***********************/
                #Canvas{
                    /*background-image: url(./res/background/background1.jpg);*/
                    border-radius:20px;     /*画出圆角*/
                    /*background-repeat: no-repeat;       背景不要重复*/
                    background-position: center center;      /*图片的位置，居中，靠左对齐*/
    
                                  /*  min-width: 1000px;      屏幕宽度在1000px以内时，图片大小保持不变*/
                                  /*  position:absolute;      固定在屏幕的最上方和最左方*/
                                  /*  top: 0;             固定在屏幕的最上方和最左方*/
                                  /*  left: 0;            固定在屏幕的最上方和最左方*/
                                  /*  width:100%;     屏幕一样的大小，从而达到全屏效果
                                    height:100%;   */
    
                                    /* 下面都不识别*/
                                    /*z-index:-10;            最下层级, 背景图片
                                    zoom: 1;*/
                                    /*background-size: cover;
                                    -webkit-background-size: cover;
                                    -o-background-size: cover;          让图片随屏幕大小同步缩放*/
                }
        """,
        """     /*******************列表控件***********************/
                /*去掉item虚线边框*/
                QListWidget, QListView, QTreeWidget, QTreeView {
                    outline: 0px;
                }
                /*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
                QListWidget {
                    /*border-bottom-left-radius:15;
                    min-width: 120px;
                    max-width: 120px;*/
                    color: white;
                    background: black;
                    font-size:16px;font-weight:bold;font-family:Roman times;
                }
                /*被选中时的背景颜色和左边框颜色*/
                QListWidget::item:selected {
                    background: rgb(52, 152, 52);
                    border-left: 2px solid rgb(9, 187, 7);
                }
                /*鼠标悬停颜色*/
                HistoryPanel::item:hover {
                    background: rgb(52, 52, 52);
                }
                
                /*右侧的层叠窗口的背景颜色*/
                QStackedWidget {
                    background: rgb(30, 30, 30);
                }
                
                /*模拟的页面*/
                QLabel {
                    color: white;
                }
        """
    ]

    # 初始化并可添加多个样式，字符串型
    def __init__(self, *args, **kwargs):
        super(StyleSheet, self).__init__()

        # print(type(args), args)
        # print(type(kwargs), kwargs)
        if args:
            for each in args:
                if isinstance(each, str):
                    self.Stylesheets.append(each)

    # 输出样式库
    def __str__(self):
        return '\n'.join(self.Stylesheets)

    # 运行时也能输出样式库
    __repr__ = __str__

    # 添加多个样式，字符串型
    def add(self, *args):
        if args:
            for each in args:
                if isinstance(each, str):
                    self.Stylesheets.append(each)

    # 用下标指定的样式列表库中的样式设置的控件/窗体
    def set(self, widget, *args):
        # print(type(args), args)
        style = []
        length = len(self.Stylesheets)
        if args:
            for each in args:
                if isinstance(each, int) and each < length:
                    style.append(self.Stylesheets[each])
        else:
            style = self.Stylesheets

        widget.setStyleSheet(''.join(style))
        # print('\n'.join(style))


# 圆形图片按钮
class RoundButton(QPushButton):
    def __init__(self, img_src, img_hovered, img_pressed, parent=None):
        super(RoundButton, self).__init__(parent)
        # self.setEnabled(True)
        self.a = img_src
        self.b = img_hovered
        self.c = img_pressed
        self.hovered = False
        self.pressed = False
        self.color = QColor(Qt.gray)
        self.hightlight = QColor(Qt.lightGray)
        self.shadow = QColor(Qt.black)
        self.opacity = 1.0
        self.roundness = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.isEnabled():
            if self.hovered:
                self.color = self.hightlight.darker(250)
        else:
            self.color = QColor(50, 50, 50)

        button_rect = QRect(self.geometry())
        painter.setPen(QPen(QBrush(Qt.red), 2.0))
        painter_path = QPainterPath()
        # painter_path.addRoundedRect(1, 1, button_rect.width() - 2, button_rect.height() - 2, self.roundness,
        # self.roundness)
        painter_path.addEllipse(1, 1, button_rect.width() - 2, button_rect.height() - 2)
        painter.setClipPath(painter_path)
        if self.isEnabled():
            if not self.pressed and not self.hovered:
                icon_size = self.iconSize()
                icon_position = self.calculateIconPosition(button_rect, icon_size)
                painter.setOpacity(1.0)
                painter.drawPixmap(icon_position, QPixmap(QIcon(self.a).pixmap(icon_size)))
            elif self.hovered and not self.pressed:
                icon_size = self.iconSize()
                icon_position = self.calculateIconPosition(button_rect, icon_size)
                painter.setOpacity(1.0)
                painter.drawPixmap(icon_position, QPixmap(QIcon(self.b).pixmap(icon_size)))
            elif self.pressed:
                icon_size = self.iconSize()
                icon_position = self.calculateIconPosition(button_rect, icon_size)
                painter.setOpacity(1.0)
                painter.drawPixmap(icon_position, QPixmap(QIcon(self.c).pixmap(icon_size)))
        else:
            icon_size = self.iconSize()
            icon_position = self.calculateIconPosition(button_rect, icon_size)
            painter.setOpacity(1.0)
            painter.drawPixmap(icon_position, QPixmap(QIcon(self.a).pixmap(icon_size)))

    def enterEvent(self, event):
        self.hovered = True
        self.repaint()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event):
        self.hovered = False;
        self.repaint()
        QPushButton.leaveEvent(self, event)

    def mousePressEvent(self, event):
        self.pressed = True
        self.repaint()
        QPushButton.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):

        self.pressed = False
        self.repaint()
        QPushButton.mouseReleaseEvent(self, event)

    def calculateIconPosition(self, button_rect, icon_size):

        x = (button_rect.width() / 2) - (icon_size.width() / 2)
        y = (button_rect.height() / 2) - (icon_size.height() / 2)

        width = icon_size.width()
        height = icon_size.height()

        icon_position = QRect()
        icon_position.setX(x)
        icon_position.setY(y)
        icon_position.setWidth(width)
        icon_position.setHeight(height)

        return icon_position


class MyQLabel(QLabel):
    clicked = pyqtSignal()  # 自定义单击信号
    DoubleClicked = pyqtSignal()  # 自定义双击信号

    def __init__(self, *args, **kwargs):
        super(MyQLabel, self).__init__(*args, **kwargs)
        # self.setFixedSize(200, 200)

    def set(self, img, border=0, padding=0, color=None, background_color=None, border_color=None):

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

    @staticmethod
    def get_round_pixmap(pix_src, radius):
        if not pix_src:
            return QPixmap()

        size = QSize(2 * radius, 2 * radius)
        mask = QtGui.QBitmap(size)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.fillRect(0, 0, size.width(), size.height(), Qt.white)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRoundedRect(0, 0, size.width(), size.height(), 99, 99);
        image = QPixmap(pix_src.scaled(size))
        image.setMask(mask)

        return image

    # 把图片按比例全部显示出来，不遮蔽，且居中，最大化
    def show_center_img(self, img_file):
        img = QImage(img_file)
        sw, sh = self.width(), self.height()
        ratio_w = img.width() / sw
        ratio_h = img.height() / sh

        is_w = True if ratio_w < ratio_h else False
        # print(sw, sh, is_w)

        img_new = img.scaledToWidth(sh) if is_w else img.scaledToHeight(sw)
        # img_new = img.scaled(sw, sh, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # print(img_new.size(), img.size())

        self.setPixmap(QPixmap.fromImage(img_new))
        self.setAlignment(Qt.AlignCenter)

    # def show_circle_img(self, img_file, scale=1.0):
    #     assert img_file, "参数错误"
    #
    #     #     # 显示圆形图标
    #     #     label.setStyleSheet('min-width:  100px;max-width:  100px;'
    #     #                     'min-height: 100px;max-height: 100px;'
    #     #                     'border-radius: 50px;border-width: 0 0 0 0;'
    #     #                     'border-image: url(./res/images/water.png) 0 0 0 0 stretch')
    #
    #     # 设置椭圆的长轴、短轴
    #     sw = self.width()
    #     sh = self.height()
    #
    #     pix = QtGui.QPixmap(img_file)
    #
    #     pix_new = QtGui.QPixmap(sw, sh)
    #     pix_new.fill(QtCore.Qt.transparent)
    #     painter = QtGui.QPainter(pix_new)
    #     painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    #
    #     path = QtGui.QPainterPath()
    #     path.addEllipse(0, 0, sw, sh)  # 绘制椭圆
    #     painter.setClipPath(path)
    #
    #     painter.drawPixmap(0, 0, sw, sh, pix)
    #     # self.setPixmap(img_file)

    # 重写鼠标单击事件

    def mousePressEvent(self, QMouseEvent):  # 单击
        self.clicked.emit()

    # 重写鼠标双击事件
    def mouseDoubleClickEvent(self, QMouseEvent):  # 双击
        self.DoubleClicked.emit()

    # 在widget四周画阴影
    def paintEvent(self, event):
        m = 9
        path = QtGui.QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(m, m, self.width() - m * 2, self.height() - m * 2)
        painter = QtGui.QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(path, QtGui.QBrush(Qt.white))

        color = QColor(250, 100, 100, 30)
        # for(int i=0; i<10; i++)

        for i in range(m):
            path = QtGui.QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRoundedRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2, 1, 1)

            al = 90 - math.sqrt(i) * 30
            # print(al)
            color.setAlpha(int(al))
            painter.setPen(QtGui.QPen(color, 1, Qt.SolidLine))
            painter.drawRoundedRect(QtCore.QRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2),
                                    0, 0)


class TitleBar(QWidget):
    StyleSheet = """
    /*标题栏*/
    TitleBar {
        /*background-color: skyblue;*/
        /*background: transparent;     全透明*/
        /*background:rgba(0,0,0,0.1)      半透明,qss中无效*/
        border-top-right-radius:15;
        /*background-image:url(./res/background/t1.png);*/
    }
    /*最小化最大化关闭按钮通用默认背景*/
    #buttonMinimum,#buttonMaximum,#buttonClose {
        /*background-color: skyblue;*/
        /*background:rgba(0,0,0,0.3)      半透明*/
        border:none;    /*全透明*/
    }
    /*悬停*/
    #buttonMinimum:hover,#buttonMaximum:hover {
        /*background-color: green;*/
        /*color: red;放在下面的前面才有效果*/
        background:rgba(0,0,0,0.2)     /*半透明*/
    }
    /*鼠标按下不放*/
    #buttonMinimum:pressed,#buttonMaximum:pressed {
        /*background-color: Firebrick;*/
        /*color: blue;放在下面的前面才有效果*/
        background:rgba(0,0,0,0.4)      /*半透明*/
    }
    #buttonClose:hover {
        color: red;
        /*background-color: gray;*/
        /*background:rgba(0,0,0,0.4)      半透明*/
    }
    #buttonClose:pressed {
        color: red;
        /*background-color: Firebrick;*/
        /*background:rgba(0,0,0,0.4)      半透明*/
    }
    """

    # region 信号声明区
    sign_win_minimize = pyqtSignal()  # 窗口最小化信号
    sign_win_maximize = pyqtSignal()  # 窗口最大化信号
    sign_win_resume = pyqtSignal()  # 窗口恢复信号
    sign_win_close = pyqtSignal()  # 窗口关闭信号
    sign_win_move = pyqtSignal(QPoint)  # 窗口移动

    # endregion

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)

        self.setStyleSheet(TitleBar.StyleSheet)

        # 窗体透明，控件不透明
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 支持qss设置背景
        self.mPos = None
        self.iconSize = 20  # 图标的默认大小
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)

        # 布局
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)

        # 窗口左图标
        self.lb_icon = QLabel(self)
        self.lb_icon.setPixmap(QtGui.QPixmap('./res/images/star.png'))
        # self.lb_icon.setScaledContents(True)
        # self.lb_icon.setFixedWidth(100)
        # self.lb_icon.setStyleSheet('background: transparent; ')
        layout.addWidget(self.lb_icon)

        # 窗口标题
        layout.addStretch()
        self.lb_title = QLabel(self.tr('运动达人'), self)
        self.lb_title.setMargin(2)
        self.lb_title.setStyleSheet(
            'color: red;font-size:24px;font-weight:bold;font-family:Roman times;')
        layout.addWidget(self.lb_title)
        # layout.addStretch()
        # 中间伸缩条
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 利用Webdings字体来显示图标
        font = self.font() or QFont()
        font.setFamily('Webdings')

        # 最小化按钮
        self.min_button = QPushButton(
            '0', self, clicked=self.sign_win_minimize.emit, font=font, objectName='buttonMinimum')
        # self.min_button.setAutoFillBackground(False)
        # self.min_button.setStyleSheet("background-color: rgb(28, 255, 3);")
        # self.min_button.setAutoDefault(False)
        # self.min_button.setDefault(False)
        # self.min_button.setFlat(False)
        layout.addWidget(self.min_button)
        # 最大化/还原按钮
        self.buttonMaximum = QPushButton(
            '1', self, clicked=self.showMaximized, font=font, objectName='buttonMaximum')
        layout.addWidget(self.buttonMaximum)
        # 关闭按钮
        self.buttonClose = QPushButton(
            'r', self, clicked=self.sign_win_close.emit, font=font, objectName='buttonClose')
        layout.addWidget(self.buttonClose)
        # 初始高度
        self.setHeight()

    def showMaximized(self):
        if self.buttonMaximum.text() == '1':
            # 最大化
            self.buttonMaximum.setText('2')
            self.sign_win_maximize.emit()
        else:  # 还原
            self.buttonMaximum.setText('1')
            self.sign_win_resume.emit()

    def setHeight(self, height=38):
        """设置标题栏高度"""
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        # 设置右边按钮的大小
        self.min_button.setMinimumSize(height, height)
        self.min_button.setMaximumSize(height, height)
        self.buttonMaximum.setMinimumSize(height, height)
        self.buttonMaximum.setMaximumSize(height, height)
        self.buttonClose.setMinimumSize(height, height)
        self.buttonClose.setMaximumSize(height, height)

    def setTitle(self, title):
        """设置标题"""
        self.titleLabel.setText(title)

    def setIcon(self, icon):
        """设置图标"""
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))

    def setIconSize(self, size):
        """设置图标大小"""
        self.iconSize = size

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)

    def mouseDoubleClickEvent(self, event):
        super(TitleBar, self).mouseDoubleClickEvent(event)
        self.showMaximized()

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()  # widget窗口左上角相对于电脑屏幕的左上角的（x=0,y=0）偏移位置
            # pos = QtGui.QMouseEvent()
            # self.mPos = event.globalPos()  # 鼠标偏离电脑屏幕左上角（x=0,y=0）的位置
        event.accept()
        self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseReleaseEvent(self, event):
        """鼠标弹起事件"""
        self.mPos = None
        event.accept()
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            # 需要在主窗体隐藏后减去背景窗体的margins
            self.sign_win_move.emit(self.mapToGlobal(event.pos() - self.mPos - QPoint(15, 15)))
            # self.sign_win_move.emit(event.globalPos() - self.mPos)
        event.accept()


# 访问Windows API
class WinInfo(object):
    hwnd_title_class = dict()

    def __init__(self, *args, **kwargs):
        super(WinInfo, self).__init__(*args, **kwargs)

    @staticmethod
    def get_hwnd_pos(class_name="MozillaWindowClass", title_name="百度一下，你就知道"):
        # 通过类名和标题查找窗口句柄，并获得窗口位置和大小
        hwnd = win32gui.FindWindow(class_name, title_name)  # 获取句柄
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口左上角和右下角坐标

        return hwnd, left, top, right, bottom

    @staticmethod
    def get_title_class(hwnd, mouse):
        # 获取某个句柄的类名和标题
        if win32gui.IsWindow(hwnd):
            # 去掉条件就输出所有
            if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                class_name = win32gui.GetClassName(hwnd)

            WinInfo.hwnd_title.update({hwnd: (title, class_name)})

    @staticmethod
    def get_child_by_name(hwnd, class_name):
        # 获取父句柄hwnd类名为class_name的子句柄
        return win32gui.FindWindowEx(hwnd, None, class_name, None)

    @staticmethod
    def get_child_windows(hwnd):
        """
        获得 hwnd的所有子窗口句柄
         返回子窗口句柄列表
         """
        if not hwnd:
            return
        hwndChildList = []
        win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
        return hwndChildList

        # 实现遍历windows所有窗口并输出窗口标题的方法

    @staticmethod
    def set_mouse_pos(x, y):
        # 鼠标定位到(30,50)
        win32api.SetCursorPos([x, y])

    @staticmethod
    def mouse_clicked(flag=1):
        if flag == 1:  # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        else:  # 右键单击
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

    @staticmethod
    def key_enter():
        # 发送回车键
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def close_win(classname, titlename):
        # 关闭窗口
        win32gui.PostMessage(win32gui.findWindow(classname, titlename), win32con.WM_CLOSE, 0, 0)

    @staticmethod
    def get_all_win():
        # 输出所有窗口
        win32gui.EnumWindows(WinInfo.get_title_class, 0)

        for h, t in WinInfo.hwnd_title_class.items():
            if t:
                print(h, t)


class VideoDisplay(QWidget):
    def __init__(self, *args, **kwargs):
        super(VideoDisplay, self).__init__(*args, **kwargs)
        self.parent = args[0]

        # 默认视频源为相机
        self.ui.radioButtonCam.setChecked(True)
        self.isCamera = True

        # 信号槽设置
        ui.Open.clicked.connect(self.Open)
        ui.Close.clicked.connect(self.Close)
        ui.radioButtonCam.clicked.connect(self.radioButtonCam)
        ui.radioButtonFile.clicked.connect(self.radioButtonFile)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    def radioButtonCam(self):
        self.isCamera = True

    def radioButtonFile(self):
        self.isCamera = False

    def Open(self):
        if not self.isCamera:
            self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
            self.cap = cv2.VideoCapture(self.fileName)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        else:
            # 下面两种rtsp格式都是支持的
            # cap = cv2.VideoCapture("rtsp://admin:Supcon1304@172.20.1.126/main/Channels/1")
            self.cap = cv2.VideoCapture("rtsp://admin:Supcon1304@172.20.1.126:554/h264/ch1/main/av_stream")

        # 创建视频显示线程
        th = threading.Thread(target=self.Display)
        th.start()

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()

    def Display(self):
        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)

        while self.cap.isOpened():
            success, frame = self.cap.read()
            # RGB转BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.ui.DispalyLabel.setPixmap(QPixmap.fromImage(img))

            if self.isCamera:
                cv2.waitKey(1)
            else:
                cv2.waitKey(int(1000 / self.frameRate))

            # 判断关闭事件是否已触发
            if True == self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DispalyLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                break


# 阴影、圆角、底图的子窗体，充当画布
class Canvas(QWidget):
    def __init__(self, parent):
        super(Canvas, self).__init__()

        self.parent = parent
        self.data = []
        self.dir = r'C:\Users\big\Desktop\家庭哑铃计划'
        self.left_width = 250  # 左侧宽度
        self.title_height = 50  # 标题栏高度

        self.layout_main = QHBoxLayout(self, spacing=0)  # 左右布局

        self.fm_left = QFrame()
        self.pb_person = EllipseButton(self, 50, 50)
        self.listWidget = QListWidget()

        self.fm_right = QFrame()
        self.titleBar = TitleBar()
        self.stackedWidget = QStackedWidget()

        self.margin = parent.margin if isinstance(parent, MainWin) else 15

        self.init_date()
        self.init_canvas_ui()
        self.init_ui()

    def init_date(self):
        # 初始化数据
        self.data = Utils.files_in_dir(self.dir, ['.mp4'])
        # print(self.data)

    # 主画布设置
    def init_canvas_ui(self):
        self.resize(500, 500)
        self.setObjectName('Canvas')
        # self.setStyleSheet('background-image:url(./res/images/background1.jpg);border-radius:20px;')

        # self.setAttribute(Qt.WA_StyledBackground, True)  # 子QWdiget背景透明
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框窗口
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowOpacity(0.9)  # 设置窗口透明度

        shadow = QGraphicsDropShadowEffect(self)  # 阴影
        shadow.setOffset(5, 5)  # 阴影宽度
        shadow.setColor(QColor(0, 0, 0, 200))  # 阴影颜色
        shadow.setBlurRadius(20)  # 阴影半径，虚化程度，不能大于圆角半径
        # vl.setContentsMargins(50, 50, 50, 50) # 重要，设置阴影的距离

        # opacity = QGraphicsOpacityEffect(self)  # 透明
        # opacity.setOpacity(0.5)  # 透明度
        # 你的控件.setGraphicsEffect(op)
        # 你的控件.setAutoFillBackground(True)

        # render = QGraphicsColorizeEffect(self)

        # blur = QGraphicsBlurEffect(self)  # 虚化
        # blur.setBlurHints()  # 设置模糊质量 参数如下：
        # PerformanceHint 表明渲染性能是最重要的因素，但可能会降低渲染质量。（默认参数）
        # QualityHint 表明渲染质量是最重要的因素，但潜在的代价是降低性能。
        # AnimationHint 表示模糊半径将是动画的，暗示实现可以保留一个源的模糊路径缓存。如果源要动态更改，则不要使用此提示。
        # blur.setBlurRadius(50)  # 设置模糊半径，半径越大，模糊效果越明显，默认为5
        # self.main_wg.setGraphicsEffect(blur)
        # pixItem = QGraphicsPixmapItem()
        # pixItem.setPixmap(QPixmap('./res/images/water.png').scaled(300, 200))
        # pixItem.setGraphicsEffect(self.blur)
        # pixItem.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

        self.setGraphicsEffect(shadow)  # 本身带上阴影特效，需要父窗体留出margin
        # self.setGraphicsEffect(opacity)

        # the same QGraphicsEffect can not be shared by other widgets
        # 子窗体带阴影的设置
        # for children in self.findChildren(QWidget):
        #     shadow = QGraphicsDropShadowEffect(blurRadius=15, xOffset=5, yOffset=5, color=QColor(0, 0, 0, 255))
        #     children.setGraphicsEffect(shadow)

        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.layout_main.addWidget(self.fm_left)
        self.layout_main.addWidget(self.fm_right)

        # 信号槽，还是发给父窗口处理
        self.titleBar.sign_win_minimize.connect(self.parent.showMinimized)
        self.titleBar.sign_win_maximize.connect(self.parent.sign_showMaximized)
        self.titleBar.sign_win_resume.connect(self.parent.sign_showNormal)
        self.titleBar.sign_win_close.connect(self.parent.close)
        self.titleBar.sign_win_move.connect(partial(self.parent.sign_move, self.left_width))
        # self.windowTitleChanged.connect(self.titleBar.setTitle)
        # self.windowIconChanged.connect(self.titleBar.setIcon)

    # 添加控件
    def init_ui(self):
        # 初始化界面

        # region 左侧界面设置(上面按钮，下面QListWidget)
        # region 左侧总体
        lv_left = QVBoxLayout(self.fm_left, spacing=0)
        lv_left.setContentsMargins(0, 15, 0, 0)

        lv_left.addWidget(self.pb_person, 0, Qt.AlignCenter)
        lv_left.addStretch()
        lv_left.addWidget(self.listWidget, 0, Qt.AlignCenter)
        lv_left.addStretch()

        # self.fm_left.setWindowOpacity(0.5)  # 设置窗口透明度
        self.fm_left.setObjectName('left_fm')
        # self.fm_left.setFixedWidth(self.left_width)  # 直接设置宽度，按钮不居中；通过样式设置则居中
        qss_left = '#left_fm{border-top-left-radius:%d;border-bottom-left-radius:%d;' \
                   'min-width: %dpx;max-width: %dpx;' \
                   'font-size:16px;font-weight:bold;font-family:Roman times;' \
                   'color: white;background: rgba(0, 0, 0, 80);' \
                   'background-position: center center}' % (self.margin, self.margin, self.left_width, self.left_width)
        self.fm_left.setStyleSheet(qss_left)
        # self.fm_left.setStyleSheet('background-image: url(./res/background/background1.jpg);'
        #                            '/*border-radius:20px;     画出圆角*/'
        #                            'background-repeat: no-repeat;       /*背景不要重复*/'
        #                            'background-position: center center;      /*图片的位置，居中，靠左对齐*/')
        # endregion

        # region 左侧图标
        # self.lb_person.setAlignment(Qt.AlignCenter)
        # self.lb_person.setIcon(QIcon('./res/images/girl1.png'))
        # self.pb_person.setFixedSize(QSize(self.left_width, 40))
        self.pb_person.set('./res/images/girl1.png')

        # self.lb_person.setStyleSheet('border-top-left-radius:%d;'
        #                              'background: transparent;     /*全透明*/'
        #                              '/*background:rgba(0,0,0,0.1);      半透明*/' % self.margin)
        # self.lb_person.setStyleSheet("color:black;"
        #                              "color:red;"
        #                              "background-color:rgb(78,255,255);"
        #                              "border:2px;"
        #                              "border-radius:15px;"
        #                              "padding:2px 4px;")

        # self.lb_person.setStyleSheet(
        #     'min-width:  50px;max-width:  40px;'
        #     'min-height: 50px;max-height: 40px;'
        #     'border-width: 0 0 0 0;'
        #     'border-image: url(./res/images/water.png) 0 0 0 0 stretch;')
        # pix = self.get_round_pixmap(QPixmap('./res/images/1.png'), 100)
        # self.lb_person.setPixmap(pix)
        # self.tb_person.setFixedHeight(self.title_height)
        # self.tb_person.setAutoFillBackground(True)
        # endregion

        # region 列表框设置
        self.listWidget.clicked.connect(self.slot_list_row_changed)

        # self.delegate = ItemDelegate()
        # self.listWidget.setItemDelegate(self.delegate)#图标在右侧
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.setFrameShape(QListWidget.NoFrame)  # 去掉边框
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        count = len(self.data)
        if count > 11:
            self.listWidget.setFixedHeight(60 * 11)
        else:
            self.listWidget.setFixedHeight(60 * count)

        # self.listWidget.resize(365, 400)
        # 设置显示模式,一般的文本配合图标模式(也可以用Icon模式,setViewMode)
        # self.listWidget.setViewMode(QListView.IconMode)

        # # 设置QListWidget中单元项的图片大小
        # self.listWidget.setIconSize(QSize(100, 100))
        # # 设置QListWidget中单元项的间距
        # self.listWidget.setSpacing(10)
        # self.listWidget.setViewportMargins(0, 0, 0, 0)
        # # 设置自动适应布局调整（Adjust适应，Fixed不适应），默认不适应
        # self.listWidget.setResizeMode(QListWidget.Adjust)
        # # 设置不能移动
        # self.listWidget.setMovement(QListWidget.Static)

        for i in range(count):
            #     print(i, self.data[i])

            # for i in range(21):
            #     item = QListWidgetItem(
            #         QIcon('./res/images/%d.ico' % randint(1, 4)), str('选 项 %s' % i), self.listWidget)
            item = QListWidgetItem(QIcon(), self.data[i], self.listWidget)
            item.setToolTip(self.data[i])
            item.setSizeHint(QSize(16777215, 60))  # 设置item的默认宽高(这里只有高度比较有用)
            item.setTextAlignment(Qt.AlignCenter)  # 文字居中

            # continue
            # item = QListWidgetItem(QIcon(), '', self.listWidget)
            # item.setSizeHint(QSize(16777215, 1))
            # line = QtWidgets.QFrame()
            # line.setFixedHeight(2)
            # line.setEnabled(False)
            # line.setStyleSheet('background:transparent;background-color:rgb(155,155,155);'
            #                    'border:1px solid rgb(155,155,155)')
            # # line.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Raised)

            # self.listWidget.setItemWidget(item, line)
        # endregion
        # endregion

        # region 右侧界面设置(上边TitleBar，下边QStackedWidget)
        # region 右侧总体
        lv_right = QVBoxLayout(self.fm_right, spacing=0)
        lv_right.setContentsMargins(0, 0, 0, 0)
        # self.stackedWidget = QStackedWidget()
        lv_right.addWidget(self.titleBar)
        lv_right.addStretch()
        # lv_right.addWidget(self.stackedWidget)

        self.fm_right.setObjectName('right_fm')
        # self.fm_left.setFixedWidth(self.left_width)  # 直接设置宽度，按钮不居中；通过样式设置则居中
        qss_right = '#right_fm{border-top-right-radius:%d;border-bottom-right-radius:%d;' \
                    'font-size:16px;font-weight:bold;font-family:Roman times;' \
                    'background-position: center center}' % (self.margin, self.margin)
        self.fm_right.setStyleSheet(qss_right)
        # endregion

        # region 右侧工具栏
        self.titleBar.setHeight(self.title_height)
        # self.titleBar.setStyleSheet('border-top-right-radius:15;border-bottom-right-radius:15')
        # self.titleBar.setAttribute(Qt.WA_StyledBackground, True)
        # endregion

        # region 右侧stackedWidget
        # self.stackedWidget.setStyleSheet('background: rgb(%d, %d, %d);margin: 0px;'
        #                                  % (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.setStyleSheet('background: lightgray;margin: 0px;'
                                         'border-bottom-right-radius:15')
        # 定义播放页面

        # 再模拟20个右侧的页面(就不和上面一起循环放了)
        for i in range(1):
            # label = QLabel(f'我是页面{i}', self)
            # label.setAlignment(Qt.AlignCenter)
            label = MyQLabel('学生', self)
            label.resize(400, 400)
            # print('df fd', self.stackedWidget.size(), label.size())
            # 设置label的背景颜色(这里随机)
            # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
            # self.stackedWidget.setStyleSheet('background: rgb(%d, %d, %d);margin: 0px;'
            #                     % (randint(0, 255), randint(0, 255), randint(0, 255)))
            label.setStyleSheet('background: green;margin: 50px;')
            label.show_center_img('./res/images/1_horizontal.jpg')

            self.stackedWidget.addWidget(label)
        # endregion
        # endregion

    def init_video_display(self):
        pass

    def slot_list_row_changed(self):
        cur_row = self.listWidget.currentRow()

        # print(cur_row)

        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        # self.stackedWidget.setCurrentIndex(cur_row // 2)

        path = os.path.join(self.dir, self.data[cur_row])
        # print('动态拉伸', path)
        os.startfile(path)  # 利用系统调用默认程序打开本地文件

    def paintEvent(self, event):
        # # 主窗体无边框时是加载不了样式的，仅在子控件上实现样式。
        # # 要在主窗体本身实现样式，需要在paintEvent事件中加上如下代码，设置底图也是一样的
        # opt = QStyleOption()
        # opt.initFrom(self)
        # p = QPainter(self)
        # p.setRenderHint(QPainter.Antialiasing)  # 反锯齿
        # self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
        # # super(Canvas, self).paintEvent(event)

        # 不通过样式，直接设置圆角，通用，且不继承于子控件
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 反锯齿

        # 显示全图充满
        img = QImage('./res//background/background11.jpg')
        w, h = self.width(), self.height()
        ratio_w = img.width() / w
        ratio_h = img.height() / h
        is_w = True if ratio_w > ratio_h else False

        img_new = img.scaledToWidth(h) if is_w else img.scaledToHeight(w)

        painter.setBrush(QBrush(QPixmap.fromImage(img_new)))  # 设置底图的方式之一
        # painter.setBrush(QBrush(Qt.blue))
        painter.setPen(Qt.transparent)

        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        painter.drawRoundedRect(rect, 20, 20)
        # 也可用QPainterPath 绘制代替 painter.drawRoundedRect(rect, 15, 15)
        # painterPath= QPainterPath()
        # painterPath.addRoundedRect(rect, 15, 15)
        # painter.drawPath(painterPath)

        # 直接设置底图，与圆角的画刷设置不能同时
        # pix = QPixmap('./res/images/background11.jpg')
        # painter.drawPixmap(self.rect(), pix)

        # super(testShadow, self).paintEvent(event)


class MainWin(QWidget):
    # 四周边距
    margin = 15

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.resize(1200, 800)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 子QWdiget背景透明

        canvas = Canvas(self)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)  # 给阴影留下位置
        # layout.setContentsMargins(0, 0, 0, 0)  # 给阴影留下位置
        layout.addWidget(canvas)

    # def mouseMoveEvent(self, event):
    #     print('in')

    def sign_showMaximized(self):
        """最大化,要先去除上下左右边界,如果不去除则边框地方会有空隙"""
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.showMaximized()

    def sign_showNormal(self):
        """还原,要先保留上下左右边界,否则没有边框无法调整"""
        self.layout().setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        super(MainWin, self).showNormal()

    # def close(self):
    #     super(MainWin, self).close()

    def sign_move(self, x_offset, pos):
        if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
            # 最大化或者全屏则不允许移动
            return

        # if self._widget is None:
        #     return

        pos_new = copy.copy(pos)
        pos_new.setX(pos.x() - x_offset)  # 减去左侧列表框占用的
        # print('this', pos_new.x(), pos.x())

        super(MainWin, self).move(pos_new)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    g_style = StyleSheet()  # 包围窗体，定义在前
    w = MainWin()  # 添加在中间
    # w = Canvas(None)
    w.show()
    g_style.set(app)  # 包围窗体，设置在后

    sys.exit(app.exec_())
