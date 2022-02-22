import sys
from PyQt5.QtWidgets import QApplication, QWidget     # 窗口
from PyQt5.QtWidgets import QPushButton, QLineEdit    # 控件
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout,QVBoxLayout   # 控件布局
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建需要的控件
        # 3个标签控件，3个行编辑控件和2个按钮
        titleEdit = QLineEdit()
        contextEdit = QLineEdit()
        phoneEdit = QLineEdit()

        submitButton = QPushButton('提交')
        cancelButton = QPushButton('取消')

        # 表单布局
        form = QFormLayout()
        form.addRow("标题", titleEdit)
        form.addRow("内容", contextEdit)
        form.addRow("电话", phoneEdit)

        # 水平布局
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(submitButton)
        hlayout.addStretch(1)
        hlayout.addWidget(cancelButton)
        hlayout.addStretch(1)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addStretch(1)
        layout.addLayout(hlayout)
        layout.addStretch(1)

        # 将布局添加到窗口中
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('布局综合应用')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

