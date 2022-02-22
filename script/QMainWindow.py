import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个退出动作
        qtool = QAction(QIcon('../fig/3.cat.jpg'), 'exit', self)
        qtool.setShortcut('ctrl+q')
        qtool.triggered.connect(qApp.quit)
        # 将退出动作添加到工具栏
        toolbar = self.addToolBar('exit')
        toolbar.addAction(qtool)

        # 状态栏显示“欢迎来到 PyQt5 !”
        self.statusBar().showMessage('欢迎来到 PyQt5 !')

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('工具栏和状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
