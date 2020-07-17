#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @项目名称: python
# @File    : mergeFiles.py
# @Time    : 2020/3/7 12:31
# @Author  : big
# @Email   : shdorado@126.com

import os
import sys
import re
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mergeFiles import Ui_MainWindow
from utilities import Utils, AnimWin

'''
QFileDialog要使用历史记录，有三个需要注意的地方：
1、directory设为空字符串（ ‘’）；
2、要使用参数少的那个函数方法，即不含有selectedFilter；
3、最后一个参数（options）要设为QtGui.QFileDialog.DontUseNativeDialog
'''


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.src_path = None
        self.save_path = None
        self.src_files = []
        self.merge_files = []
        # self.files_weight = []  # 文件大小
        self.ext_filter = "WORD Files(*.doc *.docx);;All Files(*.*)"
        # self.ext_filter = "Word Files(*.doc)\0*.doc\0All Files(*.*)\0*.*\0\0"

        self.margin = 10
        self.item_width = [0, 60, 80, 80, 140, 80, 80]  # table 列宽
        self.flag_sort = True

        # TODO 修改原始控件
        self.customUI()
        self.resize(1000, 600)

    def customUI(self):
        # self.verticalLayout.setMargin(self.margin)
        self.setupUi(self)
        self.tableWidget.initUI()

        pss = Utils.readQss('res/style/QProgressBarQss.txt')
        self.progressBar.setStyleSheet(pss)

        self.statusbar.showMessage('我昔钓白龙，放龙溪水傍。', 0)  # 状态栏本身显示的信息 第二个参数是信息停留的时间，单位是毫秒，默认是0（0表示在下一个操作来临前一直显示）
        self.allNum = QtWidgets.QLabel('总数:')
        self.selectNum = QtWidgets.QLabel('选中:')

        self.statusbar.addPermanentWidget(self.allNum, stretch=0)
        self.statusbar.addPermanentWidget(self.selectNum, stretch=0)

        font = QtGui.QFont('楷体', 14)
        # font.setBold(True)  # 设置字体加粗
        self.setFont(font)  # 设置字体
        qss = Utils.readQss('./res/style/radio_checkQss.txt')
        self.setStyleSheet(qss)

        self.cb_exit.setChecked(True)
        self.rb_digit_little.setChecked(True)
        # self.cb_select_all.setStyleSheet(qss)

        wg = self.tableWidget.createWidget(1)
        self.horizontalLayout_3.addWidget(wg)

        self.pb_save_path.clicked.connect(partial(self.slot_pb_clicked, self.pb_save_path))
        self.pb_merge.clicked.connect(lambda: self.slot_pb_clicked(self.pb_merge))
        self.pb_add_files.pressed.connect(lambda: self.slot_pb_clicked(self.pb_add_files))
        self.pb_open_dir.pressed.connect(lambda: self.slot_pb_clicked(self.pb_open_dir))
        self.pb_clear.pressed.connect(lambda: self.slot_pb_clicked(self.pb_clear))
        self.cb_select_all.pressed.connect(lambda: self.slot_cb_clicked(self.cb_select_all))
        self.comboBox.currentIndexChanged['int'].connect(self.slot_comboBox_clicked)
        self.cb_eyebrow.clicked.connect(partial(self.slot_cb_clicked, self.cb_eyebrow))
        self.cb_watermark.clicked.connect(partial(self.slot_cb_clicked, self.cb_watermark))
        self.lineEdit_src_dir.editingFinished.connect(partial(self.slot_le_edited, self.lineEdit_src_dir))
        self.lineEdit_save_path.editingFinished.connect(partial(self.slot_le_edited, self.lineEdit_save_path))

    def _createDate(self, files):
        if not files:
            return

        data = []
        for i in range(len(files)):
            file = files[i]
            size = Utils.getFileInfo(file)['文件大小']
            ct = Utils.getFileInfo(file)['最后一次的修改时间']
            data.append([files[i], '', '', size, ct])
        return data

    def slot_pb_clicked(self, controls):
        name = controls.objectName()
        # print(name)
        if name == 'pb_add_files':
            file_list, _ = QtWidgets.QFileDialog.getOpenFileNames(
                self, '多文件选取', '', self.ext_filter, None,
                QtWidgets.QFileDialog.DontUseNativeDialog)
            # print(file_list)
            data = self.createDate(file_list)
            self.tableWidget.update_data(data)
            self.tableWidget.update_table()
        elif name == 'pb_open_dir':
            path = QtWidgets.QFileDialog.getExistingDirectory(
                self, "选取源文件夹", '',
                QtWidgets.QFileDialog.ShowDirsOnly)  # 起始路径
            if path:
                self.src_path = path
                self.lineEdit_src_dir.setText(path)
                self.src_files = Utils.files_in_dir(path, ['.doc', '.docx'], True)

                data = self._createDate(self.src_files)
                self.tableWidget.update_data(data)
                self.tableWidget.update_table()
        elif name == 'pb_clear':
            self.tableWidget.update_data(None)
            self.tableWidget.update_table()
        elif name == 'pb_save_path':
            path = QtWidgets.QFileDialog.getSaveFileName(
                self, "选取保存文件夹", '.', self.ext_filter)  # 起始路径
            if path:
                # self.save_path, self.save_file = os.path.splitdrive(path[0])
                # self.save_path, self.save_file = os.path.splitext(path[0])
                self.save_path, self.save_file = os.path.split(path[0])
                self.save_path = path[0]
                # print(path)
                self.lineEdit_save_path.setText(self.save_path)
        elif name == 'pb_merge':
            rows = self.tableWidget.selectedItems()
            self.merge_files.clear()
            # self.files_weight.clear()
            for each in rows:
                file_name = each.text()
                file_path = os.path.join(self.src_path, file_name)  # 构造完整路径
                if os.path.isfile(file_path):
                    self.merge_files.append(file_path)
                    # self.files_weight.append(Utils.get_FileSize(file_path))

            # print(self.files_weight)
            # print(self.save_path)

            if self.save_path:
                # path = os.path.join(self.save_path, self.save_file)  # 构造完整路径
                if self.merge_files:
                    Utils.mergewords(self.merge_files, self.save_path, self.progressBar)
                else:
                    AnimWin('请指定保存路径')
        else:
            pass

    def slot_tb_clicked(self, controls, flag_other=0):
        name = controls.objectName()
        # 获取点击所在的行列号
        parent = controls.parent()
        x = parent.frameGeometry().x()
        y = parent.mapToParent(QtCore.QPoint(0, 0)).y()
        index = self.tableWidget.indexAt(QtCore.QPoint(x, y))
        row = index.row()
        col = index.column()
        # print('row', row, col)

        if name == 'open_file':
            file = None
            if flag_other == 1:
                file = self.save_path
            else:
                file = self.tableWidget.item(row, 0).text()
            # print(file)
            if file and os.path.isfile(file):
                os.startfile(file)
        elif name == 'open_dir':
            if flag_other == 1:
                file = self.save_path
            else:
                file = self.tableWidget.item(row, 0).text()
            if file and os.path.isfile(file):
                path, file = os.path.split(file)
                QtWidgets.QFileDialog.getOpenFileName(
                    self, '打开文件', path, self.ext_filter)
        elif name == 'recycle':
            if self.save_path and os.path.isfile(self.save_path):
                reply = QtWidgets.QMessageBox.question(
                        self, '提醒', '删除输出文件吗？',
                        QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    os.remove(self.save_path)
            else:
                self.tableWidget.delete_row(row)  # 删除指定行
        else:
            pass

    def slot_comboBox_clicked(self, value):
        print(value)

    def slot_cb_clicked(self, controls):
        name = controls.objectName()
        unchecked = controls.isChecked()  #
        # print(name, unchecked)
        if name == 'cb_select_all':
            if unchecked:
                self.tableWidget.clearSelection()
                self.tableWidget.setCurrentItem(None)
            else:
                self.tableWidget.selectAll()

    def slot_le_edited(self, controls):
        name = controls.objectName()
        # print(name)
        if name == 'lineEdit_save_path':
            self.save_path = self.lineEdit_save_path.text()
        elif name == 'lineEdit_src_dir':
            self.src_path = self.lineEdit_src_dir.text()
            # print(self.src_path)
        else:
            pass

    def handleItemClicked(self, row):
        # row = QtWidgets.QTableWidgetItem()
        print('row', row.row(), row.column())
        table_column = row.column()
        # table_row = row.row()
        # current_item = self.tableWidget.item(table_row, table_column)
        # current_widget = self.tableWidget.cellWidget(table_row, table_column)
        # print(table_column, table_row)
        # print(type(current_item), type(current_widget))

    def slot_itemchanged(self, value):
        # print(type(value))
        self.allNum.setText(f'总数:{self.tableWidget.rowCount()}')
        self.selectNum.setText(f'选中:{len(self.tableWidget.selectedItems())}')

    def resizeEvent(self, event):
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap('res/images/background9.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
