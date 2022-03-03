
# 封装好，每次使用只需调用即可
class QssTool:
    """
        读取样式
    """
    @staticmethod
    def qss(file_path, wigdet):  # 参数：QSS file path， QSS作用的控件
        # 读取 QSS 文件
        with open(file_path, encoding='utf-8') as f:
            wigdet.setStyleSheet(f.read())