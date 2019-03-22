import sys
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from poisson_football import correct_score_grid

from brownian import brownian
from matplotlib import cm
import numpy as np

import functools

cmaps = ['Spectral', 'gnuplot', 'brg']
cmap = cm.get_cmap(cmaps[0])

# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtCore import QModelIndex


class HMDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, model):
        self.max = model.max
        self.min = model.min
        QtWidgets.QStyledItemDelegate.__init__(self)

    def initStyleOption(self, option, index):
        # let the base class initStyleOption fill option with the default values
        super(HMDelegate, self).initStyleOption(option, index)

        rgba = cmap(float(index.data()) / float(self.max), bytes=True)

        colour = Qt.QColor(int(rgba[0]), int(rgba[1]), int(rgba[2]))
        option.backgroundBrush = QtGui.QBrush(colour)


class NumpyModel(QtCore.QAbstractTableModel):
    def __init__(self, narray, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._array = narray
        self.max = np.max(narray)
        self.min = np.min(narray)

    def updateData(self, narray):
        self._array = narray
        self.dataChanged.emit(Qt.QModelIndex(), Qt.QModelIndex(), [])

    def rowCount(self, parent=None):
        return self._array.shape[0]

    def columnCount(self, parent=None):
        return self._array.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                row = index.row()
                col = index.column()
                return QtCore.QVariant("%.3f" % self._array[row, col])
        return QtCore.QVariant()


def update_data(model, home_sim, away_sim):
    h = max([0, next(home_sim)])
    a = max([0, next(away_sim)])
    model.updateData(correct_score_grid(h, a))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QTableView()

    home_simulator = brownian(1, 0.1, 2.2)
    away_simulator = brownian(1, 0.1, 3.2)
    data = correct_score_grid(2.2, 3.2, 13)  # Hardcoded for now.
    model = NumpyModel(data)

    widget.setItemDelegate(HMDelegate(model))
    widget.setModel(model)
    widget.resizeColumnsToContents()
    widget.resizeRowsToContents()
    widget.show()

    timer = Qt.QTimer()
    cb = functools.partial(update_data, model, home_simulator, away_simulator)

    timer.timeout.connect(cb)
    timer.start(50)

    sys.exit(app.exec_())
