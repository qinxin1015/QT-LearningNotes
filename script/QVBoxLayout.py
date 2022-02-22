import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. 创建垂直布局
        layout = QVBoxLayout()

        # 2. 向垂直布局中添加控件
        layout.addWidget(QPushButton('OK'))
        layout.addWidget(QPushButton('Cancel'))

        # 3. 将布局添加到窗口中
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('垂直布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())