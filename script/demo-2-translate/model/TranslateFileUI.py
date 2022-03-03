import sys

from PyQt5.QtWidgets import QPushButton, QTextEdit, QLabel, QFileDialog
    
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QDir, Qt

from model import Window
from TranslateAPI import Translate
from QSSTool import QSSTool
from constants import TranslateFileConstants as tfc


class TranslateFileUI(Window):

    trans_api = Translate()   # 翻译 API

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        super(TranslateFileUI, self).initUI()
        QSSTool.qss(self, tfc.TRANSLATEFILE_QSS_FILE_PATH)

    def top_layout(self):
        """上部布局"""
        hbox = QHBoxLayout()                    # 按钮 水平布局
        hbox.setSpacing(20)                     # 按钮之间的间隔
        hbox.setContentsMargins(12, 10, 15, 0)  # 边距

        # 创建按钮
        names = ['加载文档','清空','翻译']
        obj_names = ['file_btn','clear_btn','translate_btn']
        cliecked_events = [self.loadText, self.__clear_text, self.translate_file]

        for name,obj_name,cli_event in zip(names, obj_names,cliecked_events):
            btn = QPushButton(name)                     # 按钮控件实例化
            btn.setObjectName(obj_name)                 # 设置 objectname
            btn.setCursor(Qt.PointingHandCursor)        # 设置手型
            btn.clicked.connect(cli_event)              # 绑定点击事件
            hbox.addWidget(btn)                         # 添加到布局

        return hbox

    def right_layout(self):
        """整体布局"""
        self.text_edit = QTextEdit()
        self.result_widget = QTextEdit()

        self.text_edit.setObjectName('text_edit')
        self.result_widget.setObjectName('result_widget')
        self.result_widget.setCursor(Qt.PointingHandCursor)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(5, 10, 15, 0)
        # 布局上中下三部分所占空间比为 1:4:4
        vbox.addLayout(self.top_layout(), stretch = 1)
        vbox.addWidget(self.text_edit, stretch = 4)
        vbox.addWidget(self.result_widget, stretch = 4)
        return vbox


    def loadText(self):
        """加载文档"""

        dialog = QFileDialog()
        # 获取选中文件绝对路径
        file_path = dialog.getOpenFileName(self, "选取文件", tfc.TRANSLATEFILE_FILE_PATH, "Text Files(*.txt)")[0]

        if file_path:
            with open(file_path, encoding='utf-8') as f:
                data = f.read()
                self.text_edit.setText(data)

    def translate_file(self):
        """翻译文档"""
        # 1. 获取待翻译文档
        text = self.text_edit.toPlainText()
        # 2. 调用翻译API进行翻译
        if text:
            text_list = [[j for j in i.split('。') if j] for i in text.split('\n')]
            # print(text_list)
            result = ''
            for x in text_list:
                y = [self.trans_api.translate(i) for i in x] # 逐句翻译
                result += ''.join(y) + '\n'                  # 翻译结果整合
            self.result_widget.setText(result)
        else:
            self.statusBar().showMessage(tfc.TRANSLATEFILE_FAILURE_MESSAGE)

    def __clear_text(self):
        """清空控件内容"""
        self.text_edit.clear()
        self.result_widget.clear()