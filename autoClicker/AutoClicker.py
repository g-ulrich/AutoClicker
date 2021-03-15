from g import Ui_mainWindow
from PyQt5 import QtWidgets
import sys
from uiConfig import *


class StartUtility(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.utility = Window()
        self.utility.show()


class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Presets.init_ui(self)


if __name__ == "__main__":
    app = StartUtility(sys.argv)
    sys.exit(app.exec_())
