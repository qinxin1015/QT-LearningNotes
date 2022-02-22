import sys

from PyQt5.QtWidgets import QApplication, QWidget  # 窗口
from PyQt5.QtWidgets import QLCDNumber, QSlider
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt


class LCD_and_Slider(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 创建两个控件
        self.lcd = QLCDNumber()
        self.slider = QSlider()

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.slider)

        self.slider.setRange(0, 100)               # 滑块数值范围
        self.slider.setOrientation(Qt.Horizontal)  # 水平滑块

        # 绑定信号与槽 slider 移动 lcd显示
        self.slider.valueChanged.connect(self.slider_show)

        self.setLayout(layout)
        self.setGeometry(300,300,600,400)
        self.setWindowTitle("Slider_LCD_Show")
        self.show()

    def slider_show(self):
        self.lcd.display(self.slider.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lcd_slider = LCD_and_Slider()
    sys.exit(app.exec_())