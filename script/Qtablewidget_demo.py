import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QHeaderView
)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. 创建一个四行三列的表格控件
        table = QTableWidget(4, 3, self)
        table.resize(420, 320)

        # 2. 设置水平方向的表头标签，必须在表格控件初始化行列之后进行，否则，没有效果
        table.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
        # 2. 隐藏垂直表头
        table.verticalHeader().setVisible(False)

        # 3. 单元格水平方向自适应伸缩模式
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 4. 将单元格设置为禁止编辑模式 (默认为可编辑)
        table.setEditTriggers(QTableWidget.NoEditTriggers)

        # 5. 设置表格整行选中
        table.setSelectionBehavior(QTableWidget.SelectRows)

        # 6. 添加数据
        newItem = QTableWidgetItem('张三')
        newItem.setTextAlignment(Qt.AlignCenter) # 文本居中
        table.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        newItem.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 2, newItem)

        self.setWindowTitle("表格")
        self.setGeometry(200, 200, 420, 320)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())