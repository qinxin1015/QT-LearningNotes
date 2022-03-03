import sys

from PyQt5.QtWidgets import QApplication

from model import TranslateUI, WordSearchUI, ReciteWordUI, TranslateFileUI


class WindowShow:
    
    def __init__(self):
        app = QApplication(sys.argv)

        self.translate_ui = TranslateUI()
        self.search_ui = WordSearchUI(self.translate_ui)
        self.recite_ui = ReciteWordUI(self.translate_ui)
        self.translate_file_ui = TranslateFileUI(self.translate_ui)

        # self.search_ui.move(232, 208)
        # self.recite_ui.move(232, 208)
        # self.translate_file_ui.move(232, 208)

        self.switch()


        sys.exit(app.exec_())
    
    def show_translate_ui(self):
        """展示翻译界面"""

        self.translate_ui.show()
        self.search_ui.hide()
        self.recite_ui.hide()
        self.translate_file_ui.hide()

        self.translate_ui.group_btn.buttons()[0].setChecked(True)

    def show_search_ui(self):
        """展示查单词界面"""

        self.search_ui.show()
        self.translate_ui.hide()
        self.recite_ui.hide()
        self.translate_file_ui.hide()

        self.search_ui.group_btn.buttons()[1].setChecked(True)

    def show_recite_ui(self):
        """展示背单词界面"""

        self.recite_ui.show()
        self.search_ui.hide()
        self.translate_ui.hide()
        self.translate_file_ui.hide()

        self.recite_ui.group_btn.buttons()[2].setChecked(True)

    def show_translate_file_ui(self):
        """展示译文档界面"""

        self.translate_file_ui.show()
        self.recite_ui.hide()
        self.search_ui.hide()
        self.translate_ui.hide()

        self.translate_file_ui.group_btn.buttons()[3].setChecked(True)

    def switch(self):
        """页面切换"""

        # 切换至翻译界面
        self.translate_ui.word_translate_page_signal.connect(self.show_translate_ui)
        self.search_ui.word_translate_page_signal.connect(self.show_translate_ui)
        self.recite_ui.word_translate_page_signal.connect(self.show_translate_ui)
        self.translate_file_ui.word_translate_page_signal.connect(self.show_translate_ui)

        # 切换至查单词界面
        self.translate_ui.search_page_signal.connect(self.show_search_ui)
        self.search_ui.search_page_signal.connect(self.show_search_ui)
        self.recite_ui.search_page_signal.connect(self.show_search_ui)
        self.translate_file_ui.search_page_signal.connect(self.show_search_ui)

        # 切换至背单词界面
        self.translate_ui.recite_page_signal.connect(self.show_recite_ui)
        self.search_ui.recite_page_signal.connect(self.show_recite_ui)
        self.recite_ui.recite_page_signal.connect(self.show_recite_ui)
        self.translate_file_ui.recite_page_signal.connect(self.show_recite_ui)

        # 切换至译文档界面
        self.translate_ui.file_translate_page_signal.connect(self.show_translate_file_ui)
        self.search_ui.file_translate_page_signal.connect(self.show_translate_file_ui)
        self.recite_ui.file_translate_page_signal.connect(self.show_translate_file_ui)
        self.translate_file_ui.file_translate_page_signal.connect(self.show_translate_file_ui)


if __name__ == '__main__':
    WindowShow()
