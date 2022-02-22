import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建动作，添加图标，绑定事件
        qact = QAction(QIcon('../fig/cat.jpg'), 'exit', self)
        qact.setShortcut("ctrl+q")
        qact.setStatusTip('退出')
        qact.triggered.connect(qApp.quit)

        # 创建菜单
        menu = self.menuBar()
        filemenu = menu.addMenu("file")
        filemenu.addAction(qact)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('菜单栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())