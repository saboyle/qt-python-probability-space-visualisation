import sys
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from poisson_football import correct_score_grid

from scipy.stats import norm
from matplotlib import cm
import numpy as np

cmaps = ['Spectral', 'gnuplot', 'brg']
cmap = cm.get_cmap(cmaps[0])


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


if __name__ == "__main__":
    a = QtWidgets.QApplication([])
    w = QtWidgets.QTableView()

    d = correct_score_grid(5.2, 7.1, 13)
    m = NumpyModel(d)
    w.setItemDelegate(HMDelegate(m))
    w.setModel(m)
    w.resizeColumnsToContents()
    w.resizeRowsToContents()
    w.show()

    sys.exit(a.exec_())