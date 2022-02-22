# 1.导包
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar


# 2.创建 Example 类
class Example(QMainWindow):

    # 4.初始化 调用 initUI 方法，展示窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    # 3.自定义 initUI 方法
    def initUI(self):
        # 创建菜单 添加子菜单
        menu = self.menuBar()
        filemenu = menu.addMenu('file')

        # 为菜单添加动作
        qact = QAction('open', filemenu, checkable=True)
        qact.setStatusTip('open file')
        qact.setChecked(True)
        qact.triggered.connect(self.status)

        filemenu.addAction(qact)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('勾选菜单')
        self.show()

    # 菜单事件，菜单勾选了或没勾选显示相应的状态
    def status(self, s):
        if s: # 如果菜单被勾选，显示'菜单被勾选了'
            self.statusBar().showMessage('菜单被勾选了')
        else: # 如果菜单没有被勾选，显示'菜单没被勾选'
            self.statusBar().showMessage('菜单没被勾选')


# 5.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())