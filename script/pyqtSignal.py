

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal

class mySignal(QWidget):

    close_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.close_signal.connect(self.close)

        self.setGeometry(300,300,300,300)
        self.show()

    # 鼠标按下 => close_signal发出信号 => 连接到槽事件 => 关闭窗口
    def mousePressEvent(self, event):
        self.close_signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mySignal()
    sys.exit(app.exec_())