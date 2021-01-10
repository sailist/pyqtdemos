import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Model(QtCore.QObject):
    D_Changed = QtCore.pyqtSignal(float)
    R_on_Changed = QtCore.pyqtSignal(float)
    R_off_Changed = QtCore.pyqtSignal(float)
    W_0_Changed = QtCore.pyqtSignal(float)

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self._d = 0.0
        self._r_on = 0.0
        self._r_off = 0.0
        self._w_0 = 0.0

    def D(self):
        return self._d

    def setD(self, d):
        if self._d == d: return
        self._d = d
        self.D_Changed.emit(d)

    def R_on(self):
        return self._r_on

    def setR_on(self, r_on):
        if self._r_on == r_on: return
        self._r_on = r_on
        self.R_on_Changed.emit(r_on)

    def R_off(self):
        return self._r_off

    def setR_off(self, r_off):
        if self._r_off == r_off: return
        self._r_off = r_off
        self.R_off_Changed.emit(r_off)

    D = QtCore.pyqtProperty(float, fget=D, fset=setD, notify=D_Changed)
    R_on = QtCore.pyqtProperty(float, fget=R_on, fset=setR_on, notify=R_on_Changed)
    R_off = QtCore.pyqtProperty(float, fget=R_off, fset=setR_off, notify=R_off_Changed)

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        model = Model(self)

        self.d_label = QtWidgets.QLabel()
        self.r_on_label = QtWidgets.QLabel()
        self.r_off_label = QtWidgets.QLabel()

        model.D_Changed.connect(self.on_D_Changed)
        model.R_on_Changed.connect(self.on_R_on_Changed)
        model.R_off_Changed.connect(self.on_R_off_Changed)

        model.setD(10.0)
        model.setR_on(100)
        model.setR_off(16000)

        d_le = QtWidgets.QDoubleSpinBox(
            maximum=sys.float_info.max, 
            value=model.D,
            valueChanged=model.setD
        )
        r_on_le = QtWidgets.QDoubleSpinBox(
            maximum=sys.float_info.max, 
            value=model.R_on,
            valueChanged=model.setR_on
        )
        r_off_le = QtWidgets.QDoubleSpinBox(
            maximum=sys.float_info.max, 
            value=model.R_off,
            valueChanged=model.setR_off
        )
        groub_box_input = QtWidgets.QGroupBox("Edit Values")
        flay = QtWidgets.QFormLayout()
        flay.addRow("D (nm)", d_le)
        flay.addRow("R_on (\u03A9)", r_on_le)
        flay.addRow("R_off (\u03A9)", r_off_le)
        groub_box_input.setLayout(flay)

        groub_box_output = QtWidgets.QGroupBox("Default Parameters:")
        vlay = QtWidgets.QVBoxLayout()
        vlay.addWidget(self.d_label)
        vlay.addWidget(self.r_on_label)
        vlay.addWidget(self.r_off_label)
        groub_box_output.setLayout(vlay)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(groub_box_input)
        lay.addWidget(groub_box_output)

    @QtCore.pyqtSlot(float)
    def on_D_Changed(self, d):
        self.d_label.setText('D = {}'.format(d))

    @QtCore.pyqtSlot(float)
    def on_R_on_Changed(self, r_on):
        self.r_on_label.setText('R_on = {}\u03A9'.format(r_on))

    @QtCore.pyqtSlot(float)
    def on_R_off_Changed(self, r_off):
        self.r_off_label.setText('R_off = {}\u03A9'.format(r_off))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())