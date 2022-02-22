import sys
from PyQt5.QtWidgets import QApplication, QWidget     # 窗口
from PyQt5.QtWidgets import QPushButton               # 控件
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout   # 控件布局
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        quitButton = QPushButton('退出')
        cancelButton = QPushButton('取消')

        # 水平布局
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(quitButton)
        hlayout.addWidget(cancelButton)

        # 垂直布局
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)

        # 将布局添加到窗口中
        self.setLayout(vlayout)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('盒子布局')
        self.show()

        # 绑定窗口退出事件
        quitButton.clicked.connect(QCoreApplication.instance().quit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())