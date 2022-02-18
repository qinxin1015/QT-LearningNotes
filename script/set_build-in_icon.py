
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStyle


class Example(QWidget):
    # 初始化，调用父类 __init__ 方法
    def __init__(self):
        super().__init__()
        # 4.调用 initUi 方法
        self.initUi()

    # 编写内置图标
    def initUi(self):

        # 实现原理：通过 `QStyle.StandardPixmap` 枚举，此枚举引用了可用的标准像素图
        # 要换内置图标，换下标即可
        self.setWindowIcon(QApplication.style().standardIcon(0))  # Qt 图标
        # self.setWindowIcon(QApplication.style().standardIcon(1))  # 最小化按钮图标
        # self.setWindowIcon(QApplication.style().standardIcon(2))  # 最大化按钮图标
        # self.setWindowIcon(QApplication.style().standardIcon(3))  # 关闭按钮图标


        self.setWindowTitle('Build in Icon')
        self.setGeometry(400, 300, 400, 300)
        self.show()


# 实例化 Example
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec())