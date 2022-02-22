import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication, QAction

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Context menu')
        self.show()

    # 创建右键菜单 contextMenuEvent
    def contextMenuEvent(self, event):
        # 1. 创建右键菜单
        cmenu = QMenu()

        # 2. 添加子菜单
        newact = cmenu.addAction('new')
        openact = cmenu.addAction('open')
        quitact = cmenu.addAction('quit')

        # 3. 显示菜单
        act = cmenu.exec_(self.mapToGlobal(event.pos()))

        # 3. 实现菜单中的 “退出信号”
        if quitact == act:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())