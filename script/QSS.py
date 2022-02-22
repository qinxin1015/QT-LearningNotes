# 1.导包
import sys

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt


class QSSTool:
    @staticmethod
    def qss(file_path, widget):
        with open(file_path, encoding='utf-8') as f:
            widget.setStyleSheet(f.read())


# 2.创建 Example 类
class Example(QMainWindow):

    # 5.初始化 调用 initUI 方法，展示窗口
    def __init__(self):
        super().__init__()

        self.initUI()

    # 3.自定义 initUI 方法
    def initUI(self):
        self.__layout()
        self.statusBar().showMessage('欢迎来到蓝桥学习 PyQt5!')
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSS 小案例')
        self.show()

    # 4.创建窗口布局
    def __layout(self):

        widget = QWidget()
        # 由于 QMainWindow 中设计了自己的一套布局，贸然添加盒子布局会打破原有的自身的布局，
        # 所有把控件的父类替换成 QWidget，QWidget 将作为所有基础控件的父类
        self.setCentralWidget(widget)

        btn_names = ['删除', '修改', '复制']
        btn_objectnames = ['delete', 'update', 'copy']
        btn_click_events = [self.del_btn_click, self.upd_btn_click, self.cop_btn_click]

        hbox = QHBoxLayout()

        for name, objectname, event in zip(btn_names, btn_objectnames, btn_click_events):
            b = QPushButton(name)
            b.setObjectName(objectname)
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(event)

            hbox.addWidget(b)

        widget.setLayout(hbox)

    # 删除按钮点击事件
    def del_btn_click(self):
        self.statusBar().showMessage('删除按钮被点击了')

    # 修改按钮点击事件
    def upd_btn_click(self):
        self.statusBar().showMessage('修改按钮被点击了')

    # 复制按钮点击事件
    def cop_btn_click(self):
        self.statusBar().showMessage('复制按钮被点击了')


# 6.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    # 使用 QSS 工具
    QSSTool.qss('demo11_1.qss', app)
    sys.exit(app.exec_())