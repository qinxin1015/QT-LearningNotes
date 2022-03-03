import sys
sys.path.append("../")
from PyQt5.QtCore import Qt, pyqtSignal                             # Qt 的基类、信号与槽
from PyQt5.QtGui import QIcon                                       # 图标
from PyQt5.QtWidgets import QWidget,QMainWindow,QDesktopWidget      # 窗口控件
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QButtonGroup   # 布局
# 在PyQt应用中，任何一个应用在启动时必须创建一个基于QtWidgets.QApplication或其派生类对应的应用对象，该对象用于处理事件。
# 如果需要在应用代码中的任何位置都能访问该应用对象，可以通过“QtWidgets.qApp”访问应用及其属性。
from PyQt5.QtWidgets import QApplication, qApp                      # 应用对象
from PyQt5.QtWidgets import QAction                                 # 动作
from PyQt5.QtWidgets import QPushButton 
# 自定义模块
from QSSTool import QSSTool
from constants import WindowConstants as wc
from database import DataBase

# 创建 Window 类，定义好相关方法。
class Window(QMainWindow):
    """
        所有窗口的基类，
        定义了左侧窗口布局，设计了公用的信号机制和布局接口，菜单形式
    """
    # 调用数据库 API，建立数据库连接
    conn = DataBase.connect()

    # 页面切换信号
    word_translate_page_signal = pyqtSignal()
    search_page_signal = pyqtSignal()
    recite_page_signal = pyqtSignal()
    file_translate_page_signal = pyqtSignal()

    def __init__(self, parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

    def initUI(self):
        """自定义程序界面"""
        QSSTool.qss(self, wc.WINDOW_QSS_FILE_PATH)              # QSS
        self.__layout()                                         # 布局
        self.center()                                           # 窗口居中显示
        # self.setContentsMargins(0,0,0,0)                        # 窗口的上下左右边距为0

        self.statusBar().showMessage(wc.WINDOW_WELCOM_MESSAGE)    # 窗口状态栏显示信息
        self.setWindowIcon(QIcon(wc.WINDOW_ICON_PATH))          # 窗口图标
        self.setWindowTitle(wc.WINDOW_TITLE)                    # 窗口标题显示

    def center(self):
        """窗口居中"""

        self.resize(wc.WINDOW_WIDTH, wc.WINDOW_HEIGHT)

        screen = QDesktopWidget().screenGeometry()              # 屏幕的大小
        size = self.geometry()                                  # 窗口的大小

        self.move(
            (screen.width() - size.width()) / 2,
            (screen.height() - size.height()) / 2
        )

    def left_layout(self):
        """
            左侧导航布局
            return QVBoxLayout
        """
        vbox = QVBoxLayout()
        self.group_btn = QButtonGroup()

        btn_name_list = ['翻译', '查词典', '背单词', '译文档', '复制', '收藏']
        
        btn_click_event_list = [
                self.__translate_word_page, 
                self.__search_word_page,
                self.__recite_word_page,
                self.__translate_file_page, 
                self.copy, 
                self.collect,
            ]

        for name, click_event in zip(btn_name_list,btn_click_event_list):
            btn = QPushButton(name)                 # 按钮名称
            btn.setObjectName('left_btn')           # ObjectName
            btn.setCursor(Qt.PointingHandCursor)    # 手型
            btn.setCheckable(True)                  # 可选属性
            btn.clicked.connect(click_event)        # 绑定点击事件槽函数
            self.group_btn.addButton(btn)           # 添加到按钮管理组
            vbox.addWidget(btn)                     # 添加到垂直布局
        
        self.group_btn.buttons()[0].setChecked(True)
        return vbox

    def right_layout(self):
        """
            右侧布局，供各个窗口重写此方法自定义右侧布局
            return QVBoxLayout
        """

        vbox = QVBoxLayout()
        return vbox

    def __layout(self):
        """
        窗口整体布局
        由于 QMainWindow 中设计了自己的一套布局，
        贸然添加盒子布局会打破原有的自身的布局，
        所以把控件的父类替换成 QWidget，QWidget 将作为所有基础控件的父类
        """
        widget = QWidget()
        self.setCentralWidget(widget)       # widget 作为 QMainWindow 的中心窗口

        hbox = QHBoxLayout()                # 中心窗口 水平布局
        left_layout = self.left_layout()
        right_layout = self.right_layout()
        hbox.addLayout(left_layout)
        hbox.addLayout(right_layout)

        widget.setLayout(hbox)              # 中心窗口 水平布局

    def __translate_word_page(self):
        """单词翻译页面信号发射"""
        self.word_translate_page_signal.emit()

    """ 页面切换信号的槽函数的槽函数 """
    def __search_word_page(self):
        # 查字典按钮槽函数
        self.search_page_signal.emit()

    def __recite_word_page(self):
        # 背单词按钮槽函数
        self.recite_page_signal.emit()

    def __translate_file_page(self):
        # 译文档按钮槽函数
        self.file_translate_page_signal.emit()

    def copy(self):
        # 复制按钮槽函数
        ...

    def collect(self):
        # 收藏按钮槽函数
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    QSSTool.qss(win, "../QSSTool/window.qss")
    win.show()
    sys.exit(app.exec_())