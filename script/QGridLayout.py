import sys
from PyQt5.QtWidgets import QApplication, QWidget   # 窗口
from PyQt5.QtWidgets import QPushButton             # 控件
from PyQt5.QtWidgets import QGridLayout             # 控件布局

# 2.创建 Example 类
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):            
        # 1. 创建QGridLayout的实例，并设置窗口的布局
        grid = QGridLayout()  
        
        # 2. 创建按钮的标签列表
        names = ['Cls', 'Back', '', 'Close',  
                 '7', '8', '9', '/',  
                '4', '5', '6', '*',  
                 '1', '2', '3', '-',  
                '0', '.', '=', '+']  

        # 3. 在网格中创建一个位置列表   5行 4列    
        positions = [(i,j) for i in range(5) for j in range(4)]  

        # 4. 创建按钮并通过addWIdget（）方法添加到布局中
        for position, name in zip(positions, names):                
            if name == '':  
                continue  

            button = QPushButton(name)  
            grid.addWidget(button, *position)  

        self.setLayout(grid)  
        self.move(300, 150)  
        self.setWindowTitle('计算器页面布局') 
        self.show()


# 5.实例化对象 主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())