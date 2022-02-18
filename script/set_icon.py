import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle("Icon")       # 设置窗口标题

        icon = QIcon('../fig/cat.jpg')    # 设置窗口图标
        self.setWindowIcon(icon)

        # ---------------------------------------------------------------------------
        # self.setWindowIcon(QIcon())    # 设置图标之后，如果想取消图标，加上这行代码即可
        # ---------------------------------------------------------------------------

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())