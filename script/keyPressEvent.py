

import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class writeKeyPressEvent(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("writeKeyPressEvent")
        self.show()

    # 空格键 Qt.Key_Space
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = writeKeyPressEvent()
    sys.exit(app.exec_())