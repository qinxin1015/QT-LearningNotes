import sys
from PyQt5.QtWidgets import QApplication, QWidget # 窗口
from PyQt5.QtWidgets import QPushButton           # 控件
from PyQt5.QtWidgets import QHBoxLayout           # 控件布局
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
           
    def initUI(self):
        # 创建两个按键
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 创建一个水平布局
        hbox = QHBoxLayout()
        # 伸缩量设置为1
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
 
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('水平布局')    
        self.show()        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())