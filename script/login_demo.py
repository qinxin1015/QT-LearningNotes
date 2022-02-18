import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. 创建标签、行编辑控件
        account = QLabel("账号", self)
        account_line = QLineEdit(self)

        password = QLabel("密码", self)
        password_line = QLineEdit(self)

        mail = QLabel("邮箱", self)
        mail_line = QLineEdit(self)

        # 设置控件位置，如果不设置就全部叠在一起了 
        # 这个也可以通过 Qt Designer 设置
        account.move(30, 15)
        password.move(30, 45)
        mail.move(30, 75)

        account_line.move(60, 10)
        password_line.move(60, 40)
        mail_line.move(60, 70)

        # 2. 设置输出模式 密码输入模式
        password_line.setEchoMode(QLineEdit.Password)
        # 3. 设置掩码，长度限制为 10 位
        mail_line.setInputMask('xxxxxxxxxx@163.com; ')

        # 4. 设置提示文本
        account_line.setPlaceholderText("请输入用户名")
        password_line.setPlaceholderText("请输入密码")

        self.setGeometry(300, 300, 400, 320)
        self.setWindowTitle('单行文本编辑器控件')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())