import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QDockWidget,QTextEdit,QListWidget,\
QHBoxLayout
from PyQt5.QtGui import QIcon

class DockWidgetDemo(QMainWindow):

    def __init__(self,parent=None):
        super(DockWidgetDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QHBoxLayout()
        bar=self.menuBar()
        file=bar.addMenu("文件")
        file.addAction("新建")
        file.addAction("保存")
        file.addAction("退出")

        self.items=QDockWidget("Dockable",self)
        self.listWidget=QListWidget()
        self.listWidget.addItem("项目一")
        self.listWidget.addItem("项目二")
        self.listWidget.addItem("项目三")

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)
        self.setLayout(layout)
        self.setWindowTitle("QDockWidget 例子")

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=DockWidgetDemo()
    demo.show()
    sys.exit(app.exec_())