import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Example(QWidget):

    def __init__(self,parent=None):
        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建按钮，并为它绑定了点击事件，当被点击时，调用 msg 方法
        b = QPushButton('点我', self)
        b.clicked.connect(self.msg)

        self.setWindowTitle('消息盒子')
        self.setGeometry(260, 200, 400, 300)
        self.show()

    # 消息盒子 里面定义了提示框 当按钮被点击时调用
    def msg(self):
        reply1 = QMessageBox.information(self, '提示框', '学习PyQt5好玩吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply2 = QMessageBox.question(self, "询问框", "学习PyQt5好玩吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply3 = QMessageBox.warning(self, "警告框", "学习PyQt5好玩吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply4 = QMessageBox.critical(self, "错误框", "学习PyQt5好玩吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        reply5 = QMessageBox.about(self, "关于", "学习PyQt5好玩吗？")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())