import sys
from PyQt5.QtWidgets import QApplication, QWidget           # 窗口
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit    # 控件
from PyQt5.QtWidgets import QGridLayout                     # 控件布局


class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.initUI()

    def initUI(self):            
        titleLabel = QLabel('标题')  
        authorLabel = QLabel('提交人')  
        contentLabel = QLabel('申告内容')  

        titleEdit = QLineEdit()  
        authorEdit = QLineEdit()  
        contentEdit = QTextEdit()  

        grid = QGridLayout()  
        grid.setSpacing(10)  

        grid.addWidget(titleLabel, 1, 0)  
        grid.addWidget(titleEdit, 1, 1)  

        grid.addWidget(authorLabel, 2, 0)  
        grid.addWidget(authorEdit, 2, 1) 

        # 把contentLabel放在QGridLayout布局的第3行第0列
        grid.addWidget(contentLabel, 3, 0)  
        # 把contentEdit放在QGridLayout布局的第3行第1列，跨越5行1列
        grid.addWidget(contentEdit, 3, 1, 5, 1)  

        self.setLayout(grid)   
        self.setGeometry(300, 300, 350, 300)  
        self.setWindowTitle('故障单')
        self.show()

if __name__ == "__main__":  
        app = QApplication(sys.argv) 
        form = Winform()
        sys.exit(app.exec_())
