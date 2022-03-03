import sys,re
import PyQt5
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from QSSTool.QSSTool import QssTool

class Caculater(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):
        layout = QVBoxLayout()
        grid = QGridLayout()

        key_names = ['(', ')','x²', '√',
                     'AC','←','+/-','÷',
                     '9', '8', '7', '×',
                     '6', '5', '4', '-',
                     '3', '2', '1', '+',
                     '%', '0', '.', '=']

        positions = [(i,j) for i in range(6) for j in range(4)]

        for name, pos in zip(key_names, positions):
            b = QPushButton(name, self)
            if pos[0] == 0:
                b.setObjectName('row1')
            if pos[1] == 3:
                b.setObjectName('col4')   
            if pos[0] == 5:
                b.setObjectName('row6') 

            b.clicked.connect(self.clicked_func)
            grid.addWidget(b, *pos)

        self.lineedit = QLineEdit() # 显示计算公式
        self.rstlabel = QLabel()    # 显示结果
        # 结果靠右显示
        self.lineedit.setAlignment(Qt.AlignRight)
        self.rstlabel.setAlignment(Qt.AlignRight)

        layout.addWidget(self.lineedit)
        layout.addWidget(self.rstlabel)
        layout.addLayout(grid)
        self.setLayout(layout)

        # self.setGeometry(300,300,400,500)
        self.setWindowTitle("计算器")
        self.setObjectName("widget")
        self.setWindowIcon(QIcon('fig/calculator.jpg'))
        self.center()
        self.show()

    def center(self):
        """窗口居中"""
        
        # 获取窗口坐标
        qr = self.frameGeometry()
        # 获取屏幕中心点坐标
        cp = QDesktopWidget().availableGeometry().center()
        # 将窗口移动到屏幕中心点
        qr.moveCenter(cp)

    def clicked_func(self):
        sender = self.sender()
        text = sender.text()
        linetext = self.lineedit.text()

        if text in ['(', ')','÷','√',
                     '9', '8', '7', '×',
                     '6', '5', '4', '-',
                     '3', '2', '1', '+',
                     '%', '0', '.']:

            self.lineedit.setText(linetext+text)

        if text == 'x²':
            self.lineedit.setText(linetext+'^2')

        if text == 'AC':
            self.lineedit.clear()
            self.rstlabel.clear()

        if text == '←':
            self.lineedit.setText(linetext[:-1])

        # 按下 +/- 按钮，添加负数
        if text == '+/-':
            nums = re.findall("[0-9]+", linetext)
            if nums:
                self.lineedit.setText(linetext.rstrip(nums[-1]) + '(-' + nums[-1] + ')')
            else:
                self.rstlabel.setText("error")
                print("error")

        if text == '=':
            self.caculate(linetext)

    def caculate(self, text):
        if not text: return

        if '^' in text:
            text = text.replace('^','**')

        if '√' in text:
            sqrt_nums = re.findall('(√[0-9]+)', text) # 找到text中有多少需要开根号的数
            if sqrt_nums:
                for num in sqrt_nums:
                    text = text.replace(num, num[1:] + '**0.5')
            else: # 只有根号 没有需要开根号的数值，如，√ + √5 + 3
                self.rstlabel.setText("error")

        if '÷' in text:
            text = text.replace('÷','/')

        if '×' in text:
            text = text.replace('×','*')    

        # 百分数运算
        if '%' in text:
            percent_nums = re.findall('(\d+\.\d+%|\d+%)', text) # 找到text中有多少需要开根号的数  
            # print('percent_nums = ', percent_nums)
            if percent_nums:
                for num in percent_nums:
                    text = text.replace(num, num[:-1] + '/100') 
            else: # 只有百分 没有需要百分数运算的数值，如，% + √5 + 3
                self.rstlabel.setText("error")

        try:
            self.rstlabel.setText(str(eval(text)))
        except:
            self.rstlabel.setText("error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Caculater()
    QssTool.qss("QSSTool/caculater.qss",app)
    sys.exit(app.exec_())