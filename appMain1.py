from mainwindow import Ui_MainWindow
import sys
from PyQt5.Qt import *


class Qmywindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.on_pushButton_click)

    def on_pushButton_clicked(self):
        print('已经点击')
        d = int(self.ui.dLineEdit.text())
        s = int(self.ui.sLineEdit.text())
        if d % 2 == 0:
            self.ui.dOutLabel.setText("这是一个偶数")
        else:
            self.ui.dOutLabel.setText("这不是一个偶数")
        if s % 2 != 0:
            self.ui.sOutLabel.setText("这是一个奇数")
        else:
            self.ui.sOutLabel.setText("这不是一个奇数")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = Qmywindow()
    baseWidget.show()
    sys.exit(app.exec_())
