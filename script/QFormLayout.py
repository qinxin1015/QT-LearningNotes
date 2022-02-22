# 1.导包
import sys
from PyQt5.QtWidgets import QApplication, QWidget # 窗口
from PyQt5.QtWidgets import QLineEdit             # 控件
from PyQt5.QtWidgets import QFormLayout           # 控件布局

# 2.创建 Example 类
class Example(QWidget):

    # 4.初始化 调用 initUI 方法，展示窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    # 3.自定义 initUI 方法
    def initUI(self):
        # 创建表单布局
        layout = QFormLayout()

        layout.addRow('姓名', QLineEdit())
        layout.addRow('年龄', QLineEdit())
        layout.addRow('工作', QLineEdit())
        layout.addRow('住址', QLineEdit())

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('表单布局')
        self.show()


# 5.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())