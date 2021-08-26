from untitled import Ui_MainWindow
import sys
from PyQt5.Qt import *


class Qmywindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dOutLabel.setText("我要疯了")


    def on_pushButton_click(self):
        print('已经点击')
    # self.ui.dLable.setText("这是一个偶数")
    # self.ui.sLable.setText("这不是一个奇数")
    # d = int(self.dLineEdit.text())
    # s = int(self.sLineEdit.text())
    # if d%2 == 0:
    #     self.ui.dLable.setText("这是一个偶数")
    # else:
    #     self.ui.dLable.setText("这不是一个偶数")
    # if s%2 != 0:
    #     self.ui.sLable.setText("这是一个奇数")
    # else:
    #     self.ui.sLable.setText("这不是一个奇数")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = Qmywindow()
    baseWidget.show()
    sys.exit(app.exec_())
