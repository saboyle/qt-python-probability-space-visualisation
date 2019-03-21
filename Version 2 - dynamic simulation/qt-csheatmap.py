import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication, QTableWidget, QTableWidgetItem)
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.Qt import QColor, QTimer

import random

from scipy.stats import norm

from matplotlib import cm

cmaps = ['Spectral', 'gnuplot', 'brg']
cmap = cm.get_cmap(cmaps[0])


class QtCSGrid(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.txt = QTableWidget()

        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshGrid)
        self.timer.start(500)

        self.txt.setRowCount(13)
        self.txt.setColumnCount(13)

        self.txt.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for r in range(13):
            for c in range(13):
                val = r * c/169 * random.random()
                item = QTableWidgetItem(f"{val:0.02f}")

                rgba = cmap(val, bytes=True)

                item.setBackground(QColor(int(rgba[0]), int(rgba[1]), int(rgba[2])))
                item.setForeground(QColor(255, 255, 255))
                self.txt.setItem(r, c, item)

        self.txt.resizeColumnsToContents()
        self.txt.resizeRowsToContents()

        grid.addWidget(self.txt)

        self.move(300, 150)
        self.setWindowTitle(f"Qt CS Grid")
        self.show()

    def refreshGrid(self):
        for r in range(13):
            for c in range(13):
                val = r * c/169 * random.random()
                item = QTableWidgetItem(f"{val:0.02f}")

                rgba = cmap(val, bytes=True)

                item.setBackground(QColor(int(rgba[0]), int(rgba[1]), int(rgba[2])))
                item.setForeground(QColor(255, 255, 255))
                self.txt.setItem(r, c, item)
        self.txt.repaint()

def centre_window():
    availableSize = app.desktop().availableGeometry()
    width = availableSize.width()
    height = availableSize.height()

    main.move((width - main.width()) / 2, (height - main.height()) / 2)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QtCSGrid()
    centre_window()
    main.show()

    sys.exit(app.exec_())
