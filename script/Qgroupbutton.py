import sys
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QRadioButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 1. 创建按钮分组器控件
        group = QButtonGroup(self)
        # 创建单选按钮控件
        male = QRadioButton('男', self)
        female = QRadioButton('女', self)
        
        male.move(150, 100)
        female.move(200, 100)

        # 2. 设置“男”单选框被默认选中
        male.setChecked(True)

        # 将单选按钮添加到按钮分组器中，这时这两个单选按钮具有互斥性，只能选中一个
        group.addButton(male)
        group.addButton(female)

        # 3. 给单选按钮设置 ID
        group.setId(male, 1)
        group.setId(female, 2)

        # 4. 打印按钮分组器中所有的按钮对象
        print(group.buttons())
        
        # 5. 打印 ID=2 的按钮文本
        print(group.button(2).text())
        
        # 6. 打印被按下的按钮文本
        print(group.checkedButton().text())

        self.setWindowTitle('按钮分组器')
        self.setGeometry(200, 200, 400, 320)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())