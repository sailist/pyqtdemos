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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
################################################

items_list=["C","C++","Java","Python","JavaScript","C#","Swift","go","Ruby","Lua","PHP"]

################################################
class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.lineedit = QLineEdit(self, minimumWidth=200)
        self.combobox = QComboBox(self, minimumWidth=200)
        self.combobox.setEditable(True)

        layout.addWidget(QLabel("QLineEdit", self))
        layout.addWidget(self.lineedit)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addWidget(QLabel("QComboBox", self))
        layout.addWidget(self.combobox)

        #初始化combobox
        self.init_lineedit()
        # self.init_combobox()

        #增加选中事件
        # self.combobox.activated.connect(self.on_combobox_Activate)

    def init_lineedit(self):
        # 增加自动补全
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        # self.m_model.insertRow(0)
        self.lineedit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onTxtChoosed)
        # self.m_model.setData(self.m_model.index(0,0),'java')
        # self.completer = QCompleter(self.m_model,self)
        # self.completer.activated[str].connect(lambda x:print(x))
        self.lineedit.textChanged.connect(self.on_loginTxt_textChanged)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        # self.completer.setFilterMode(Qt.MatchContains)
        # self.completer.
        # self.completer.setCompletionMode()
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        # self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.lineedit.setClearButtonEnabled(True)
        self.lineedit.setCompleter(m_completer)

    def onTxtChoosed(self, txt):
        self.lineedit.setText(txt)

    @pyqtSlot(str)
    def on_loginTxt_textChanged(self, text:str):
        if '@' in self.lineedit.text():
            return



        emaillist = ["@163.com", "@qq.com", "@gmail.com", "@live.com", "@126.com", "@139.com"]
        self.m_model.removeRows(0, self.m_model.rowCount())
        for i in range(0, len(emaillist)):
            self.m_model.insertRow(0)
            self.m_model.setData(self.m_model.index(0, 0), text + emaillist[i])

    def init_combobox(self):
        # 增加选项元素
        for i in range(len(items_list)):
            self.combobox.addItem(items_list[i])
        self.combobox.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.combobox.setCompleter(self.completer)

    def on_combobox_Activate(self, index):
        print(self.combobox.count())
        print(self.combobox.currentIndex())
        print(self.combobox.currentText())
        print(self.combobox.currentData())
        print(self.combobox.itemData(self.combobox.currentIndex()))
        print(self.combobox.itemText(self.combobox.currentIndex()))
        print(self.combobox.itemText(index))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())