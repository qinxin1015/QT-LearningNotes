import sys
sys.path.append("../")
from queue import Queue, LifoQueue
import random
import copy

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout, QButtonGroup

from model import Window
from QSSTool.QSSTool import QSSTool
from slot import ReciteWord, AnswerCheck, AnswerGet, WordKill
from constants import ReciteConstants as rc


class ReciteWordUI(Window):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.queue = Queue(rc.RECITE_QUEUE_SIZE)
        self.queue_next = Queue(rc.RECITE_QUEUE_SIZE)       # 下一个
        self.queue_prev = LifoQueue(rc.RECITE_QUEUE_SIZE)   # 上一个
        self.n = 0

        self.initUI()

    def initUI(self):
        super(ReciteWordUI, self).initUI()
        QSSTool.qss(self, rc.RECITE_QSS_FILE_PATH)  # QSS
        self.__data_process()
        self.__data_set()

    def top_layout(self):
        """上边布局
        显示 要背的单词
        """
        self.label = QLabel()
        self.label.setObjectName('label')
        self.label.setAlignment(Qt.AlignCenter)     # 设置文本居中对齐
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        return hbox

    def mid_layout(self):
        """中间布局
        显示 A,B,C,D 四个选项
        """
        answer_names = ['A', 'B', 'C', 'D']

        answer_objnames = ['answer_a', 'answer_b', 'answer_c', 'answer_d']
        btn_objnames = ['btn_a', 'btn_b', 'btn_c', 'btn_d']

        self.vbox = QVBoxLayout()
        self.group_opt = QButtonGroup()
        
        for name, ans_objname, btn_objname in zip(answer_names, answer_objnames, btn_objnames):
            # 选项按钮
            option_btn = QPushButton()
            option_btn.setObjectName(btn_objname)
            option_btn.setCursor(Qt.PointingHandCursor) # 手型
            option_btn.setCheckable(True)
            option_btn.clicked.connect(self.answser_click)
            # 在选项按钮上放置标签
            label = QLabel(name, option_btn)
            label.setAlignment(Qt.AlignCenter)          # 居中
            label.setObjectName(ans_objname)

            self.group_opt.addButton(option_btn)        # 选项按钮加入按钮组管理
            self.vbox.addWidget(option_btn)             # 加入布局管理        

        return self.vbox

    def bottom_layout(self):
        """下边布局
        操作按钮： '上一个'、'不认识'、'腰斩'、'下一个'
        """
        btn_names = [
            rc.RECITE_PREV_BUTTON_NAME, rc.RECITE_UNKW_BUTTON_NAME,
            rc.RECITE_KILL_BUTTON_NAME, rc.RECITE_NEXT_BUTTON_NAME
        ]
        btn_objnames = ['pre', 'unkwon', 'kill', 'next']
        click_events = [self.prev_btn_click, 
                        self.unkw_btn_click,
                        self.kill_btn_click, 
                        self.next_btn_click]
        hbox = QHBoxLayout()
        hbox.setSpacing(5)      # 控件之间的间距
        for name, object_name,click_event in zip(btn_names, btn_objnames,click_events):
            b = QPushButton(name)
            b.setObjectName(object_name)
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(click_event)
            hbox.addWidget(b)
        return hbox

    def right_layout(self):
        """整体布局
        合并 上、中、下 界面，垂直布局管理
        """
        vbox = QVBoxLayout()
        vbox.setContentsMargins(12, 10, 20, 10)
        vbox.setSpacing(0)

        # 上、中、下布局占据空间比为 3:5:1
        vbox.addLayout(self.top_layout(), stretch=3)
        vbox.addLayout(self.mid_layout(), stretch=5)
        vbox.addLayout(self.bottom_layout(), stretch=1)
        return vbox

    def __data_process(self):
        """数据加载、构造"""
        data = ReciteWord.from_mysql(self.conn, self.n)
        """
        数据格式：
            (
                ('abandon', '丢弃，放弃，抛弃；放纵'),
                ('ability', '能力；能耐，本领'),
                ...
            )
        """
        self.n += 1
        # 转换成键值对
        new_data = {i[0]: i[1] for i in data}

        values = list(new_data.values())
        # 将顺序随机打乱
        random.shuffle(values)

        while new_data:
            # 生成随机单词及答案选项
            word, means = new_data.popitem()

            item_list = [means]             # 答案选项 （1个对的，3个随机的）
            temp = copy.deepcopy(values)
            for _ in range(3):
                v = random.choice(temp)
                item_list.append(v)
                temp.remove(v)

            del temp

            # 打包，逐个放进队列
            self.queue.put({
                'word': word,
                'A': item_list[0],
                'B': item_list[1],
                'C': item_list[2],
                'D': item_list[3]
            })

            self.queue_next.put({
                'word': word,
                'A': item_list[0],
                'B': item_list[1],
                'C': item_list[2],
                'D': item_list[3]
            })

    def __data_set(self):
        """设置背单词页面打开时的第一个单词数据"""
        # 判断队列是否为空
        if self.queue_next.empty():
            return

        data = self.queue_next.get()
        btns = self.group_opt.buttons()
        # 设置答案
        self.label.setText(data['word'])
        btns[0].setText(data['A'])
        btns[1].setText(data['B'])
        btns[2].setText(data['C'])
        btns[3].setText(data['D'])

    def answser_click(self):
        """答案校验"""
        btn = self.sender()     # 获取按下按钮的"答案"
        if AnswerCheck.check(self.conn, self.label.text(), btn.text()): # 答案正确
            btn.setStyleSheet("""
                #btn_a:checked, #btn_b:checked,
                #btn_c:checked, #btn_d:checked {
                    background-color: lightgreen;
                } """)
            btn.children()[0].setStyleSheet("""
               #answer_a, #answer_b, #answer_c, #answer_d {
                   background-color: lightgreen;
               } """)
        else:                                                           # 答案错误
            btn.setStyleSheet("""
                #btn_a:checked, #btn_b:checked,
                #btn_c:checked, #btn_d:checked {
                    background-color: red;
                }""")
            btn.children()[0].setStyleSheet("""
                #answer_a, #answer_b, #answer_c, #answer_d {
                    background-color: red;
                }""")

    def __queue_struct(self, data):
        """队列重构 更新上一个、下一个单词队列"""
        # data 是当前页面中加载出来的一个单元数据

        for x in self.queue.queue:
            if data == x:
                w = list(self.queue.queue)
                index = w.index(x)
                prev_list = w[:index]
                next_list = w[index + 1:]

        self.queue_next = Queue(rc.RECITE_QUEUE_SIZE)
        self.queue_prev = LifoQueue(rc.RECITE_QUEUE_SIZE)

        for x in prev_list:
            self.queue_prev.put(x)

        for x in next_list:
            self.queue_next.put(x)

    def __next_word_set(self):
        """加载下一个单词"""
        
        if self.queue_next.empty(): # 第一次判断队列是否为空，没有就从数据库中取
            self.refresh()
        
        if self.queue_next.empty(): # 第二次判断队列是否为空，如果还是空说明数据库中也没有了
            return

        self.__button_style_clear()

        data = self.queue_next.get()
        self.__queue_struct(data)

        btns = self.group_opt.buttons()

        self.label.setText(data['word'])
        btns[0].setText(data['A'])
        btns[1].setText(data['B'])
        btns[2].setText(data['C'])
        btns[3].setText(data['D'])

    def __prev_word_set(self):
        """加载上一个单词"""
        if self.queue_prev.empty():         # 判断队列是否为空
            return
        self.__button_style_clear()

        data = self.queue_prev.get()
        self.__queue_struct(data)

        btns = self.group_opt.buttons()

        self.label.setText(data['word'])
        print(self.label)
        btns[0].setText(data['A'])
        btns[1].setText(data['B'])
        btns[2].setText(data['C'])
        btns[3].setText(data['D'])

    def refresh(self):
        """数据更新"""

        # 这里起到清空队列的作用，self.queue一直是满队列，不清空数据将插不进去，
        # 会导致程序处于阻塞状态
        self.queue = Queue(rc.RECITE_QUEUE_SIZE)
        self.__data_process()

    def __button_style_clear(self):
        """上一个、下一个按钮样式清除"""
        btns = self.group_opt.buttons()
        for i in range(4):
            btns[i].setText("")                     # 清空 按钮 文本
            btns[i].setStyleSheet("")               # 清除 按钮 样式
            btns[i].children()[0].setStyleSheet("") # 清除 标签 样式

        # label = self.findChild(QLabel, "answer_a") # 另一种查子控件的方法
        # label.setStyleSheet("") 

    def unkw_btn_click(self):
        """获取答案"""
        answer = AnswerGet.get(self.conn, self.label.text())
        btns = self.group_opt.buttons()

        if not answer:
            self.statusBar().showMessage(rc.RECITE_ANSWER_GET_FAILURE_MESSAGE)
            return

        # 选中正确答案
        for btn in btns:
            if btn.text() == answer:
                btn.setChecked(True)
                btn.setStyleSheet("""
                            #btn_a:checked, #btn_b:checked,
                            #btn_c:checked, #btn_d:checked {
                                background-color: lightgreen;
                            }
                        """)
                btn.children()[0].setStyleSheet("""
                           #answer_a, #answer_b, #answer_c, #answer_d {
                               background-color: lightgreen;
                           }
                       """)
                break

    def kill_btn_click(self):
        """斩（删除）单词"""
        status = WordKill.kill(self.conn, self.label.text())
        if status:
            self.statusBar().showMessage(self.label.text() + rc.RECITE_ANSWER_DELETE_SECCESS_MESSAGE)
            self.__next_word_set()
        else:
            self.statusBar().showMessage(self.label.text() + rc.RECITE_ANSWER_DELETE_FAILURE_MESSAGE)
            return

    def prev_btn_click(self):
        """上一个按钮点击事件"""
        self.__prev_word_set()

    def next_btn_click(self):
        """下一个按钮点击事件"""
        self.__next_word_set()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ReciteWordUI()
    win.show()
    sys.exit(app.exec_())