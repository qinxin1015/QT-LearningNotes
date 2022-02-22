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


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # 自定义 initUI 方法
    def initUI(self):
        self.__layout() # 重写控件布局
        self.statusBar().showMessage('Welcome to PyQt5!')
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSS Demo')
        self.show()


    # 创建窗口布局
    def __layout(self):  # 名称修饰

        widget = QWidget()
        # 由于 QMainWindow 中设计了自己的一套布局，贸然添加盒子布局会打破原有的自身的布局，
        # 所有把控件的父类替换成 QWidget，QWidget 将作为所有基础控件的父类
        self.setCentralWidget(widget)

        btn_names = ['删除', '修改', '复制'] 
        btn_objectnames = ['delete', 'update', 'copy']
        btn_click_events = [self.del_btn_click, self.upd_btn_click, self.cop_btn_click]

        hbox = QHBoxLayout()

        for name, objectname, event in zip(btn_names, btn_objectnames, btn_click_events):
            b = QPushButton(name)               #  标签 text 
            b.setObjectName(objectname)         # 控件名称 ObjectName 调用的时候会用到
            b.setCursor(Qt.PointingHandCursor)  # 设置新的光标：光标变为手型
            b.clicked.connect(event)            # 信号与槽 绑定

            hbox.addWidget(b)

        widget.setLayout(hbox)

    # 删除按钮点击事件
    def del_btn_click(self):
        self.statusBar().showMessage('删除')

    # 修改按钮点击事件
    def upd_btn_click(self):
        self.statusBar().showMessage('修改')

    # 复制按钮点击事件
    def cop_btn_click(self):
        self.statusBar().showMessage('复制')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    # 使用 QSS 工具
    QSSTool.qss('demo_qss.qss', app)
    sys.exit(app.exec_())