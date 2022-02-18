import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit,
    QVBoxLayout, QPushButton
)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 1. 创建多行文本编辑器控件
        self.text = QTextEdit()
        # 1. 创建两个按钮 控件
        self.show_text = QPushButton("显示文本")
        self.show_html = QPushButton("显示 HTML")

        # 创建垂直布局管理器
        layout = QVBoxLayout()
        # 向垂直布局管理器中添加控件
        layout.addWidget(self.text)
        layout.addWidget(self.show_text)
        layout.addWidget(self.show_html)
        # 将布局管理器添加到 QWidget 的布局中
        self.setLayout(layout)

        # 给两个按钮空格键绑定点击槽函数（事件）
        # 2. 当显示文本按钮本点击时，显示内容
        self.show_text.clicked.connect(self.show_text_click)
        # 3. 当显示 HTML 按钮本点击时，显示内容
        self.show_html.clicked.connect(self.show_html_click)

        self.setGeometry(200, 200, 400, 320)
        self.setWindowTitle("多行文本编辑器")
        self.show()

    def show_text_click(self):
        """2. 显示文本按钮控件槽函数"""

        # 设置文本
        self.text.setPlainText("你好，派森诺生物!")

    def show_html_click(self):
        """3. 显示 HTML 按钮控件槽函数"""

        # 设置 HTML
        self.text.setHtml("<p style='color:red;font-size:30px'>你好，派森诺生物!</p>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())