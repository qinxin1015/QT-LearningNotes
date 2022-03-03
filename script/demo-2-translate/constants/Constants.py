import os

WORK_PATH = os.getcwd()  # 项目工作目录 (返回当前工作目录)

class WindowConstants: 
    """基类常量"""
    WINDOW_WORK_PATH = WORK_PATH
    WINDOW_QSS_FILE_PATH = WORK_PATH + '/QSSTool/window.qss'
    
    WINDOW_ICON_PATH = WORK_PATH + '/resource/figs/translate.png'
    WINDOW_EXIT_ICON_PATH = WORK_PATH + '/resource/figs/exit.png'
    WINDOW_EXIT_SHORTCUT = "ctrl+q"

    WINDOW_WELCOM_MESSAGE = "欢迎来到 PyQt5!"
    WINDOW_TITLE = '单词神器'

    WINDOW_WIDTH = 680
    WINDOW_HEIGHT = 400


class TranslateConstants:
    """翻译页面常量"""
    TRANSLATE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/translate.qss'
    TRANSLATE_PLACEHODERTEXT = '请输入翻译的词语或语句'

    TRANSLATE_BUTTON_NAME = "翻译一下"

    TRANSLATE_FAILURE_MESSAGE = '翻译失败，请重试！'

    TRANSLATE_COPY_MESSAGE = " 已复制到剪切板！"

    TRANSLATE_COLLECT_MESSAGE = " 已收藏至单词本！"


class TranslateFileConstants:
    """译文档界面常量"""
    TRANSLATEFILE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/translatefile.qss'

    TRANSLATEFILE_FILE_PATH = WORK_PATH + '/resource/将进酒.txt'
    
    TRANSLATEFILE_FAILURE_MESSAGE = '翻译内容为空！'


class TableConstants: 
    """自定义表格控件常量"""
    TABLE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/dicttable.qss'

    TABLE_DEFAULT_ROW = TABLE_DATA_SHOW_COUNT = 8
    TABLE_DEFAULT_COLUMN = 3

    TABLE_HEADER_LIST = ['单词', '意思', '操作']

    TABLE_HEADER_HEIGHT = 29
    TABLE_ROW_HEIGHT = 39


class SearchConstants:
    """ 查单词界面常量 """
    SEARCH_UPDATE_MESSAGE = '单词意思修改成功！'
    SEARCH_DELETE_MESSAGE = '删除成功！'
    SEARCH_COPY_MESSAGE = " 已复制到剪切板！"


class ReciteConstants:
    """ 背单词界面常量 """
    RECITE_PREV_BUTTON_NAME = '上一个'
    RECITE_UNKW_BUTTON_NAME = '不认识'
    RECITE_KILL_BUTTON_NAME = '腰斩'
    RECITE_NEXT_BUTTON_NAME = '下一个'

    RECITE_QSS_FILE_PATH = WORK_PATH + '/QSSTool/reciteword.qss'

    RECITE_QUEUE_SIZE = 32  # 一次加载32个单词

    RECITE_ANSWER_GET_FAILURE_MESSAGE = "数据加载失败！"
    RECITE_ANSWER_DELETE_SECCESS_MESSAGE = "删除成功！"
    RECITE_ANSWER_DELETE_FAILURE_MESSAGE = "删除失败！"