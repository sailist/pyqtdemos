"""
    Copyright (C) 2020 Shandong University

    This program is licensed under the GNU General Public License 3.0 
    (https://www.gnu.org/licenses/gpl-3.0.html). 
    Any derivative work obtained under this license must be licensed 
    under the GNU General Public License as published by the Free 
    Software Foundation, either Version 3 of the License, or (at your option) 
    any later version, if this derivative work is distributed to a third party.

    The copyright for the program is owned by Shandong University. 
    For commercial projects that require the ability to distribute 
    the code of this program as part of a program that cannot be 
    distributed under the GNU General Public License, please contact 
            
            sailist@outlook.com
             
    to purchase a commercial license.
"""

import sys
import typing

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from ui.components.mixin import *
from ui.components.wrap_widgets import *
from ui.components.utils import *

class FirstWindow(QMainWindow, EAddMixin, ERealShowMixin):

    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)
        self.layout = EVBoxLayout()
        # self.layout = QHBoxLayout()
        # shortcut_open = QShortcut(QKeySequence('Esc'), self)
        # AddShortCut(self,"Esc",lambda :self.hide())
        def func():
            print(123)
        AddShortCut(self,'Shift+Ctrl+A',lambda: self.real_show(),global_shortcut=True)
        AddShortCut(self,'Shift+Ctrl+B',lambda: self.hide(),global_shortcut=True)
        # shortcut_open.activated.connect(lambda: self.hide())

        self.layout.temp = QLabel('123')
        print(self.layout.temp)

        # self.layout.edit = QLineEdit()
        # self.layout.edit = EKeyPressWrap(self.layout.edit)
        # EAddKeyPressListener(self.layout.edit,lambda x:print(x))
        # EAddKeyPressListener(self.layout.edit,lambda x:print(2))
        self.layout.edit = ELineEdit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    ex.show()
    sys.exit(App.exec_())