import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QTextEdit, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout

class Caculater(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        grid = QGridLayout()

        self.key_names = ['(', ')','x²', '√',
                     'AC','←','+/-','÷',
                     '9', '8', '7', '×',
                     '6', '5', '4', '-',
                     '3', '2', '1', '+',
                     '%', '0', '.', '=']

        key_objectNames = ['left_bracket',  'right_bracket','op_square','op_sqrt',
                            'op_clear',     'op_back',      'op_sign',  'op_divide',
                            'num_9',        'num_8',        'num_7',    'op_multiple',
                            'num_6',        'num_5',        'num_4',    'op_minus',
                            'num_3',        'num_2',        'num_1',    'op_plus',
                            'op_mod',       'num_0',        'num_dot',  'op_qual']

        positions = [[i,j] for i in range(4) for j in range(6)]

        for name, objName, pos in zip(self.key_names, key_objectNames, positions):
            b = QPushButton(name, self)
            b.setObjectName(objName)
            b.clicked.connect(self.clicked_func)
            print(pos[1], pos[0])
            grid.addWidget(b, pos[1], pos[0])

        self.lineedit = QLineEdit()

        layout.addWidget(self.lineedit)
        layout.addLayout(grid)
        self.setLayout(layout)

        self.setGeometry(300,300,400,500)
        self.setWindowTitle("计算器")
        self.show()


    def clicked_func(self):
        sender = self.sender()
        text = sender.text()

        linetext = self.lineedit.text()
        if text in self.key_names:
            self.lineedit.setText(linetext+text)

    def caculate(self, text):
        if 'x²' in text:
            text = text.replace('x²','**2')

        if '√' in text:
            text = text.replace('x²','**0.5')

        if '√' in text:
            text = text.replace('x²','**0.5')
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Caculater()
    sys.exit(app.exec_())