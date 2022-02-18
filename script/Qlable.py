import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 需求实现：
        # 1. 创建标签对象
        label = QLabel("人生苦短，我用 Python", self)
        # 2. 设置标签对象的位置、宽高
        label.setGeometry(100, 100, 200, 50)
        # 3. 设置标签对象的样式 边框样式：2px 实线 红色
        label.setStyleSheet("""border: 2px solid red""")
        # 4. 标签对象在窗口中 水平+垂直居中
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # 5. 打印标签文本内容
        print(label.text())

        self.setGeometry(300, 300, 400, 320)  # 窗口的位置、宽高
        self.setWindowTitle('标签控件')        # 窗口标题
        self.show()                           # 窗口显示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())