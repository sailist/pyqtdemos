from PyQt5 import QtCore, QtWidgets, QtGui
import sys


# ------------------------------------------------------------------------------
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data = [[]], headers = None, parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__data = data

    def rowCount(self, parent):
        return len(self.__data)

    def columnCount(self, parent):
        return len(self.__data[0])

    def data(self, index, role):
        row = index.row()
        column = index.column()
        if role == QtCore.Qt.DisplayRole:
            value = self.__data[row][column]
            return value
        if role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor(255, 255, 255))

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable


# ------------------------------------------------------------------------------
class TableView(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)


# ------------------------------------------------------------------------------
class Delegate(QtWidgets.QStyledItemDelegate):

    # <Modification>
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if (
                index.row() == tableView.currentIndex().row() and
                index.column() == tableView.currentIndex().column()
        ):
            option.backgroundBrush = QtGui.QBrush(QtGui.QColor(232, 244, 252))

    def paint(self, painter, option, index):
        if (index.column() == 0):

            # <Modification>
            if (
                    index.row() == tableView.currentIndex().row() and
                    index.column() == tableView.currentIndex().column()
            ):
                self.initStyleOption(option, index)
                painter.setPen(QtCore.Qt.NoPen)
                painter.setBrush(option.backgroundBrush)
                painter.drawRect(option.rect)

            image = QtGui.QImage('open.png')
            pixmap = QtGui.QPixmap.fromImage(image)
            x = option.rect.center().x() - pixmap.rect().width() / 2
            y = option.rect.center().y() - pixmap.rect().height() / 2
            painter.drawPixmap(x, y, pixmap)

        else:
            super().paint(painter, option, index)



# ------------------------------------------------------------------------------
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    tableView = TableView()
    tableView.resize(550, 160)
    tableView.setItemDelegate(Delegate())
    tableView.show()

    rowCount = 3
    columnCount = 4
    data = [
        [i for i in range(columnCount)]
        for j in range(rowCount)
    ]

    model = TableModel(data)
    tableView.setModel(model)

    sys.exit(app.exec_())