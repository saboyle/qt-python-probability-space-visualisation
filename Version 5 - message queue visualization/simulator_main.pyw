from qt_simulator import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
import sys

# See https://nikolak.com/pyqt-qt-designer-getting-started/
# For useful tutorial / notes

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
