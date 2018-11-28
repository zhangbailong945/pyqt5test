from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle


##QSS的UI美化

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.pix=QPixmap()
        self.lastPoint=QPoint(600,500)
        self.endPoint=QPoint()
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
                #辅助画布
        self.temppix=QPixmap()
        #标志是否正在绘画
        self.isDrawing=False
        self.initUI()

    def initUI(self):
        self.resize(600,500)
        self.languageCombox=QComboBox()
        self.languageCombox.setObjectName('languageCombox')
        items=['汉语','英语','葡萄牙语']
        self.languageCombox.addItems(items)
        layout=QVBoxLayout()
        layout.addWidget(self.languageCombox)
        self.setLayout(layout)
        self.setWindowTitle("QSS美化")


if __name__=="__main__":
    app=QApplication(sys.argv)
    qssStyle='''
      QComboBox#languageCombox:drop-down{
          image:url(d:/PyQt5Projects/pyqt5test/images/test.ico);
      }
      QComboBox:hover{
          background-color:red;
      }
      QComboxBox::drop-down:hover{
          background-color:red;
      }
    '''
    demo=WinForm()
    #demo.setStyleSheet(qssStyle)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    print(os.path.dirname(__file__))
    demo.show()
    sys.exit(app.exec_())