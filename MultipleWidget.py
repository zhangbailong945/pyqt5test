import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QDockWidget,QTextEdit,QListWidget,\
QHBoxLayout,QMdiArea,QAction,QMdiSubWindow
from PyQt5.QtGui import QIcon

class MultipleWidgetDemo(QMainWindow):
    count=0

    def __init__(self,parent=None):
        super(MultipleWidgetDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)
        bar=self.menuBar()
        file=bar.addMenu("file")
        file.addAction("new")
        file.addAction("cascade")
        file.addAction("tiled")
        file.triggered[QAction].connect(self.windowAction)
        self.setWindowTitle("MDI demo")
    
    def windowAction(self,q):
        if q.text()=="new":
            MultipleWidgetDemo.count=MultipleWidgetDemo.count+1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("sub window"+str(MultipleWidgetDemo.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if q.text()=="cascade":
            self.mdi.cascadeSubWindows()
        if q.text()=="tiled":
            self.mdi.tileSubWindows()

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=MultipleWidgetDemo()
    demo.show()
    sys.exit(app.exec_())