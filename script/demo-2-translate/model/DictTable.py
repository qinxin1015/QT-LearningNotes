import sys
sys.path.append("../")

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QButtonGroup
from PyQt5.QtWidgets import (QPushButton, QLineEdit,QHeaderView, QTableWidget,QLabel, QMessageBox,
QAbstractItemView,QTableView, QTableWidgetItem, QInputDialog)

from QSSTool import QSSTool
from constants import TableConstants as tc


class TableWidget(QWidget):

    delete_signal = pyqtSignal(str)             # 删除信号
    update_signal = pyqtSignal(str, str)        # 修改信号
    copy_signal = pyqtSignal(str)               # 复制信号

    change_signal = pyqtSignal(str)             # 内容改变信号

    def __init__(self, *args, **kwargs):

        # API: count：数据库中的总条数 data：8条初始数据
        # 父类中不需要 count 和 data 参数，所以需要 pop
        if kwargs.get('count') is not None:
            count = kwargs.pop('count')
        else:
            count = 0

        if kwargs.get('data') is not None:
            self.data = kwargs.pop('data')
        else:
            self.data = ()

        # 计算总页数
        if count and count % tc.TABLE_DATA_SHOW_COUNT == 0:
            self.page = count // tc.TABLE_DATA_SHOW_COUNT
        else:
            self.page = count // tc.TABLE_DATA_SHOW_COUNT + 1

        super(TableWidget, self).__init__(*args, **kwargs)
        self.initUI()
        
    def initUI(self):
        self.setLayout(self.__layout())
        QSSTool.qss(self, tc.TABLE_QSS_FILE_PATH)
        self.show()

    def __layout(self):
        """
            表格布局 和 Window.py 的 __layout 方法不一样，
            注意区别，这里是自定义表格控件的布局方法
        """
        self.table = QTableWidget(tc.TABLE_DEFAULT_ROW, tc.TABLE_DEFAULT_COLUMN)    # 8行3列
        self.table.setHorizontalHeaderLabels(tc.TABLE_HEADER_LIST)                  # 表头
        self.table.horizontalHeader().setFixedHeight(tc.TABLE_HEADER_HEIGHT)        # 表头高度
        for i in range(tc.TABLE_DEFAULT_ROW):                                       # 设置行高
            self.table.setRowHeight(i, tc.TABLE_ROW_HEIGHT)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)              # 只能选中一行
        self.table.setEditTriggers(QTableView.NoEditTriggers)                       # 不可编辑
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)               # 设置只有行选中
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 列自动拉伸，充满界面
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)              # 表格
        vbox.addLayout(self.page_layout())      # 页码
        self.data_show()

        return vbox

    def page_layout(self):
        """页码布局"""
        # 单击 想要到达的页数
        home_page = QPushButton("首页")
        home_page.clicked.connect(self.__home_page)
        last_page = QPushButton("<上一页")
        last_page.clicked.connect(self.__last_page)
        page1 = QPushButton("1")
        page2 = QPushButton("2")
        page3 = QPushButton("3")
        page4 = QPushButton("4")
        page5 = QPushButton("5")
        next_page = QPushButton("下一页>")
        next_page.clicked.connect(self.__next_page)
        finally_page = QPushButton("尾页")
        finally_page.clicked.connect(self.__finally_page)

        # 创建按钮组
        self.group = QButtonGroup(self)
        btn_list = [page1, page2, page3, page4, page5]
        for b in btn_list:
            self.group.addButton(b)
            b.setCheckable(True)
            b.clicked.connect(self.changeTableContent)
        
        self.group.buttons()[0].setChecked(True)

        self.total_page = QLabel("共" + str(self.page) + "页")
        # 手动输入 达到的页数
        skip_to = QLabel("跳到")
        self.skip_page = QLineEdit()
        skip_page_to = QLabel("页")
        confirm = QPushButton("确定")
        confirm.clicked.connect(self.__confirm_skip)

        # 将控件添加到布局中
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        w_list = [
            home_page, last_page, page1, page2,
            page3, page4, page5, finally_page,
            next_page, self.total_page, skip_to, self.skip_page,
            skip_page_to, confirm
        ]
        objectname_list = [
            'home_page', 'last_page', 'page1', 'page2',
            'page3', 'page4', 'page5', 'finally_page',
            'next_page', 'total_page', 'skip_to', 'skip_page',
            'skip_page_to', 'confirm'
        ]

        for w, objectname in zip(w_list, objectname_list):
            w.setObjectName(objectname)
            hbox.addWidget(w)

        return hbox

    def data_show(self):
        """每页的数据展示"""
        self.table.clearContents()

        row_num = min(len(self.data), 8)
        for row in range(row_num):
            word, means = self.data[row]

            word_item = QTableWidgetItem(word)
            means_item = QTableWidgetItem(means)

            word_item.setTextAlignment(Qt.AlignCenter)      # 文本居中
            means_item.setTextAlignment(Qt.AlignCenter)
            # col0: word_item; col1: means_item; col2: self.oparate(row)
            self.table.setItem(row, 0, QTableWidgetItem(word_item))
            self.table.setItem(row, 1, QTableWidgetItem(means_item))
            self.table.setCellWidget(row, 2, self.oparate(row))

    # 对表格中的数据进行操作
    def oparate(self, row):
        """设置 "操作" 按钮"""
        
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        btn_name_list = ['删除', '修改', '复制']
        btn_objectname_list = ['delete', 'update', 'copy']
        btn_click_event_list = [self.__delete, self.__update, self.__copy]

        for btn_name, btn_objectname, btn_click_event in zip(
                btn_name_list, btn_objectname_list, btn_click_event_list):

            btn = QPushButton(btn_name)
            btn.setObjectName(btn_objectname)
            btn.clicked.connect(btn_click_event)

            btn.setMinimumSize(50, 39)
            btn.setCursor(Qt.PointingHandCursor)
            btn.row = row

            hbox.addWidget(btn)

        widget = QWidget()
        widget.setLayout(hbox)
        return widget

    def __delete(self):
        """删除操作按钮点击事件"""
        row = self.sender().row
        word = self.table.item(row, 0).text()

        self.delete_signal.emit(word)           # 发出"删除"信号
        self.changeTableContent()

    def __update(self):
        """修改操作按钮点击事件"""
        row = self.sender().row
        word = self.table.item(row, 0).text()

        text, ok = QInputDialog.getText(self, "修改", "请输入修改内容：", QLineEdit.Normal, "")
        if ok and text:
            self.update_signal.emit(text, word) # 发出"修改"信号
        self.changeTableContent()

    def __copy(self):
        """复制操作按钮点击事件"""
        row = self.sender().row
        word = self.table.item(row, 0).text()
        means = self.table.item(row, 1).text()
        text = word + ':' + means

        clipboard = QApplication.clipboard()    # 实例化剪切板对象
        clipboard.setText(text)

        self.copy_signal.emit(text)             # 发出"复制"信号

    def changeTableContent(self):
        """发射当前页表格内容改变信号"""
        btn = self.group.checkedButton()
        self.change_signal.emit(btn.text())

        self.data_show()

    def __home_page(self):
        """点击首页信号"""
        buttons = self.group.buttons()

        for i in range(5):
            buttons[i].setText(str(i+1))

        buttons[0].setChecked(True)                 # 选中第一页
        self.changeTableContent()

    def __finally_page(self):
        """点击尾页信号"""
        total_page = self.total_page.text()[1:-1]   # 获取总页数
        buttons = self.group.buttons()

        if int(total_page) <= 5:                    
            p = range(1, 6)
        else:                                       # 获取最后5页的页码
            p = range(int(total_page) - 4, int(total_page) + 1)
        
        for i in range(5):
            buttons[i].setText(str(p[i]))

        buttons[-1].setChecked(True)                # 选中最后一页
        self.changeTableContent()

    def __last_page(self):
        """点击 上一页 信号"""
        # 获取页码和当前页按钮位置
        buttons = self.group.buttons()
        for b in buttons:
            if b.isChecked():       # 当前页按钮位置
                page = b.text()
                index = buttons.index(b)
                break

        if page == '1':
            QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
            return

        # 如果是第一个按钮被选中则页码减一，否则前一个按钮被选中
        if index == 0:
            p = range(int(page) - 1, int(page) + 4)     # 页码往前移动一位

            for i in range(5):
                buttons[i].setText(str(p[i]))

            buttons[index].setChecked(True)
        else:
            buttons[index-1].setChecked(True)
        self.changeTableContent()

    def __next_page(self):
        """点击下一页信号"""
        total_page = self.total_page.text()[1:-1]
        buttons = self.group.buttons()

        for b in buttons:
            if b.isChecked():
                page = b.text()
                index = buttons.index(b)
                break

        if page == total_page:
            QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
            return

        # 页码按钮效果处理
        if index == 4 and int(total_page) > 5:
            p = range(int(page) - 3, int(page) + 2)
            for i in range(5):
                buttons[i].setText(str(p[i]))
            buttons[index].setChecked(True)
        else:
            buttons[index + 1].setChecked(True)
        self.changeTableContent()

    def __confirm_skip(self):
        """页码跳转信号"""
        total_page = self.total_page.text()[1:-1]
        buttons = self.group.buttons()

        page = self.skip_page.text()        # 要跳转到的页码
        self.skip_page.clear()
        
        if not page:                        # 如果没有输入页码，则什么也不做
            return

        if int(total_page) < int(page) or int(page) < 0:
            QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
            return

        # 页码按钮效果处理
        if int(page) + 5 > int(total_page):
            p = range(int(total_page) - 4, int(total_page) + 1)
            for i in range(5):
                buttons[i].setText(str(p[i]))
                if p[i] == int(page):
                    buttons[i].setChecked(True)
        else:
            p = range(int(page), int(page) + 5)
            for i in range(5):
                buttons[i].setText(str(p[i]))
                if str(p[i]) == page:
                    buttons[0].setChecked(True)

        self.changeTableContent()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TableWidget()
    # QSSTool.qss(win, "../QSSTool/dicttable.qss")
    sys.exit(app.exec_())