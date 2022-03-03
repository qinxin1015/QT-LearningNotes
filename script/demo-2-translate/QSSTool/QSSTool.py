class QSSTool:
    @staticmethod
    def qss(widget, file_path=None, file_path_list=None):
        """
        	参数：
                widget：控件
                file_path：文件路径
                file_path_list：文件路径列表
                
            如果有多个QSS文件可以列表的形式传入路径
        """
        
        if file_path is not None:
            try:
                with open(file_path, encoding='utf-8') as f:
                    widget.setStyleSheet(f.read())
            except:
                print(file_path, "此文件不存在！")

        elif file_path_list is not None:
            for path in file_path_list:
                try:
                    with open(path, encoding='utf-8') as f:
                        widget.setStyleSheet(f.read())
                except:
                    print(path, "此文件不存在！")

        else:
            print("您没有输入QSS文件不存在！")

