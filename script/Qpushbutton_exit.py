import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(240, 200, 400, 300)
        self.setWindowTitle("窗口关闭事件")

        # 1. 给提示语设置字体 这里用的字体是：微软雅黑 14px
        QToolTip.setFont(QFont('微软雅黑', 14))

        # 2. 创建退出按钮
        button = QPushButton('退出', self)
        
        # 3. 给按钮添加提示语
        self.setToolTip('<b>点我</b>可以<i style="color:blue">关闭窗口</i>')
        
        # 4. 绑定点击事件（信号） 点击了就会关闭窗口（槽函数）
        button.clicked.connect(QCoreApplication.instance().quit)

        self.show()


# 5.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())