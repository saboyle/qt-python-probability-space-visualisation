import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication, QTableWidget, QTableWidgetItem)
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.Qt import QColor

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
        txt = QTableWidget()

        txt.setRowCount(13)
        txt.setColumnCount(13)

        txt.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for r in range(13):
            for c in range(13):
                val = r * c/169
                item = QTableWidgetItem(f"{val:0.02f}")

                rgba = cmap(val, bytes=True)

                item.setBackground(QColor(int(rgba[0]), int(rgba[1]), int(rgba[2])))
                item.setForeground(QColor(255, 255, 255))
                txt.setItem(r, c, item)

        txt.resizeColumnsToContents()
        txt.resizeRowsToContents()

        grid.addWidget(txt)

        self.move(300, 150)
        self.setWindowTitle(f"Qt CS Grid")
        self.show()


def centre_window():
    availableSize = app.desktop().availableGeometry()
    width = availableSize.width()
    height = availableSize.height()

    width *= 0.9
    height *= 0.9
    main.move((width - main.width()) / 2, (height - main.height()) /2)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QtCSGrid()
    centre_window()
    main.show()

    sys.exit(app.exec_())
