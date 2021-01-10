from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from urllib import request

# need Pyqt5.14+
class Demo(QTextEdit):
    def __init__(self):
        super().__init__()
        md = self.get_markdown()
        self.setMarkdown(md)

    def get_markdown(self):
        url = 'https://raw.githubusercontent.com/PyQt5/PyQt/master/README.md'
        response = request.urlopen(url)
        return response.read().decode()

app = QApplication([])
demo = Demo()
demo.show()
app.exec()

# other example：https://doc.qt.io/qt-5/qtwebengine-webenginewidgets-markdowneditor-example.html