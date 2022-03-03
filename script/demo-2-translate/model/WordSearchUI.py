import sys
sys.path.append("../")
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMessageBox

from model.DictTable import TableWidget
from model import Window
from slot import GetWord, UpdateMean, DeleteWord
from constants import SearchConstants as sc
from QSSTool import QSSTool  

class WordSearchUI(Window):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        super().initUI()
        # 连接信号，绑定槽
        self.table.change_signal.connect(self.table_content_change)     # 翻页
        self.table.update_signal.connect(self.table_content_update)     # 修改
        self.table.delete_signal.connect(self.table_content_delete)     # 删除
        self.table.copy_signal.connect(self.table_content_copy)         # 复制

    def right_layout(self):
        """右侧布局
        放入自定义的表格控件
        - 外部定义GetWord槽函数用于获取mysql数据
        """
        self.table = TableWidget(count = GetWord.all_count(self.conn), 
                                 data = GetWord.from_mysql(self.conn))
        self.table.setObjectName('widget')
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        return vbox

    def table_content_change(self, page):
        """表格翻页"""
        self.table.data = GetWord.from_mysql(self.conn, page = page)

    def table_content_delete(self, word):
        """表格内容删除"""
        status = DeleteWord.delete(self.conn, word = word)
        if not status:
            QMessageBox.warning(
                self, '警告', '删除错误',
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes
            )
        else:
            self.statusBar().showMessage(sc.SEARCH_DELETE_MESSAGE)

    def table_content_update(self, means, word):
        """表格内容修改"""
        status = UpdateMean.update(self.conn, means = means, word = word)
        if not status:  # 修改失败，弹出提示框
            QMessageBox.warning(
                self, '警告', '修改错误',
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes
            )
        else:           # 显示，'单词意思修改成功！'
            self.statusBar().showMessage(sc.SEARCH_UPDATE_MESSAGE)

    def table_content_copy(self, text):
        """表格内容复制"""
        self.statusBar().showMessage(sc.SEARCH_COPY_MESSAGE)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WordSearchUI()
    win.show()
    sys.exit(app.exec_())