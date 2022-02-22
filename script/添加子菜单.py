# 1.导包
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QMenu


# 2.创建 Example 类
class Example(QMainWindow):

    # 4.初始化 调用 initUI 方法，展示窗口
    def __init__(self):
        super().__init__()

        self.initUI()

    # 3.自定义 initUI 方法
    def initUI(self):
        # 创建菜单栏，添加 file 菜单
        menu = self.menuBar()
        filemenu = menu.addMenu('file')

        # 添加 New 子菜单
        newact = QAction('new', filemenu)
        filemenu.addAction(newact)

        # 添加 email 子菜单
        emailmenu = QMenu('email', filemenu)
        emailmenu.addAction(QAction('163@mail', self))
        emailmenu.addAction(QAction('qq@mail', self))
        filemenu.addMenu(emailmenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('子菜单')
        self.show()


# 5.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())