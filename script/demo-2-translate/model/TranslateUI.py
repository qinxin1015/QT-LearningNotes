import sys
sys.path.append("../")
from PyQt5.QtCore import Qt, pyqtSignal                         # 基础部件与自定义信号
from PyQt5.QtWidgets import QWidget, QApplication               # 应用和窗体
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit   # 控件
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout            # 布局

from model import Window                                        # Window 基类 （继承）
from TranslateAPI import Translate                              # 翻译API

from slot import CollectSlot, DictionarySlot                    # 自定义槽函数
from QSSTool import QSSTool                                     # QSS样式表
from constants import TranslateConstants as tc                  # 常量配置


# 创建 TranslateUI 类，继承基类
class TranslateUI(Window):

    dictionary_signal = pyqtSignal(str, str)            # 定义翻译录入信号（将翻译的内容，录入词典）
    collect_signal = pyqtSignal(str, str)               # 定义收藏信号 （信号发生的时候，实现收藏功能）

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        """自定义UI界面"""
        super(TranslateUI, self).initUI()
        QSSTool.qss(self, tc.TRANSLATE_QSS_FILE_PATH)
        self.show()

    def top_layout(self):
        """
            翻译界面上侧布局
            return QHBoxLayout
        """
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 10, 0, 0)            # setContentsMargins：设置盒子边距
        
        self.line = QLineEdit(self)                     # self.line 用于后面的 复制 和 收藏 方法
        self.line.setObjectName('line')
        self.line.setPlaceholderText(tc.TRANSLATE_PLACEHODERTEXT)   # 输入提示信息

        clear_btn = QPushButton('清空', self.line)            # "清空"按钮 放到 self.line上面
        clear_btn.setGeometry(330, 0, 60, 45)                 # 按钮 在 self.line 上面的 相对位置 setGeometry(x, y,宽,高)
        clear_btn.setCursor(Qt.PointingHandCursor)            # 手型光标

        clear_btn.clicked.connect(self.clear)                 # 绑定槽函数

        translate_btn = QPushButton(tc.TRANSLATE_BUTTON_NAME)   # "翻译" 按钮
        translate_btn.setObjectName('translate')
        translate_btn.setCursor(Qt.PointingHandCursor)          # 手型光标

        translate_btn.clicked.connect(self.translate)           # 绑定槽函数

        # 往布局中添加控件 设置伸展模式  
        hbox.addWidget(self.line, stretch=6)        # 输入框：按钮 =  6:1
        hbox.addWidget(translate_btn, stretch=1)

        hbox.setSpacing(5)          # 控件之间的空格间隙

        return hbox

    def right_layout(self):
        """
            翻译界面整体布局
            return QVBoxLayout
        """
        self.text_edit = QTextEdit()                # 翻译结果显示窗口
        self.text_edit.setFocusPolicy(Qt.NoFocus)   # 将文本编辑框设置成不聚焦模式
                                                    # 输入焦点始终不在这个窗体上，即不能进行选中编辑
        vbox = QVBoxLayout()
        vbox.setSpacing(10)                         # 控件之间的空格间隙
        vbox.addLayout(self.top_layout())
        vbox.addWidget(self.text_edit)

        return vbox


    def translate(self):
        """翻译功能
        调用翻译API Translate

            >>> b = Translate()
            >>> b.translate("add a button")
            '添加按钮'

        """
        # 1. 获取搜索框文本
        text = self.line.text()
        # 2. 调用翻译API进行翻译，并返回翻译结果文本
        trans_api = Translate()
        translate_text = trans_api.translate(text)

        if translate_text:
            # 3.1 将翻译结果文本(如果存在)显示在下方显示框
            self.text_edit.setText(translate_text)
        else:
            # 3.2 翻译结果不存在，在状态栏给出提示信息“翻译失败，请重试 ！”
            self.statusBar.showMessage(tc.TRANSLATE_FAILURE_MESSAGE)

        # 4. 将单词更新到单词表中去
        self.dictionary_signal.connect(self.search_slot)
        self.dictionary_signal.emit(text, translate_text)


    def copy(self):
        """复制单词到剪切板"""
        # 1. 创建剪切板对象
        clipboard = QApplication.clipboard()
        # 2. 获取翻译结果文本
        text = self.text_edit.toPlainText()
        # 3. 如果文本存在，就复制到剪切板
        if text:
            clipboard.setText(text)
            self.statusBar().showMessage(tc.TRANSLATE_COPY_MESSAGE)

    def collect(self):
        """收藏单词到单词本"""
        # 1. 获取当前的待译文本及翻译结果
        word = self.line.text()
        means = self.text_edit.toPlainText()
        # 2. 发射信号，调用槽函数，实现收藏功能
        self.collect_signal.connect(self.collect_slot)
        if means: 
            self.collect_signal.emit(word, means)
            self.statusBar().showMessage(tc.TRANSLATE_COLLECT_MESSAGE)


    def collect_slot(self, word, means):
        # 执行外部的槽函数, 调用CollectSlot的to_mysql方法，实现收藏功能
        CollectSlot.to_mysql(self.conn, word, means)

    def search_slot(self, word, means):
        # 执行外部的槽函数
        DictionarySlot.to_mysql(self.conn, word, means)

    def clear(self):
        """清空行编辑器（搜索框）中的内容"""

        self.line.clear()
        self.text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TranslateUI()
    QSSTool.qss(win, "../QSSTool/translate.qss")
    sys.exit(app.exec_())