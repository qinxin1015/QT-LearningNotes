import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    # 创建一个应用对象
    # sys.argv 是一组命令行参数的列表，Python 可以在 shell 里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)
    # QWidge 控件是一个用户界面的基本控件(窗口)
    win = QWidget()

    # 设置窗口的位置、大小
    win.resize(250, 150)  # 大小
    win.move(300, 300)    # 位置 （屏幕坐标系的原点是屏幕的 左上角）

    # setWindowTitle()：给窗口添加标题
    win.setWindowTitle('Hello World, PYQT5 !')

    # show()：让控件在桌面上显示出来（控件先在内存中创建，然后在显示器上显示）。
    win.show()

    # 退出
    sys.exit(app.exec_())
    # sys.exit()：让主循环安全退出。
    # app.exec_() 执行应用程序，程序进入消息循环，等待用户操作，当用户点击右上角的 × 时，窗口才会正常结束。
    # 如果不加这行代码，窗口会一闪而过。

