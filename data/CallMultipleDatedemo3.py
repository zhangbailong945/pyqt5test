from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from multipleDatedemo3 import DateDialog
import sys,time

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle('信号与槽 子窗口的数据传递')
        self.lineEdit_inner=QLineEdit(self)
        self.lineEdit_emit=QLineEdit(self)
        self.btn_GetTime=QPushButton('获取时间',self)

        self.btn_GetTime.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('获取内置信号的时间')
        self.lineEdit_emit.setText('获取自定义信号的时间')

        gridLayout=QGridLayout()
        gridLayout.addWidget(self.lineEdit_inner)
        gridLayout.addWidget(self.lineEdit_emit)
        gridLayout.addWidget(self.btn_GetTime)

        self.setLayout(gridLayout)
    
    def openDialog(self):
        dialog=DateDialog(self)
        #连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        #连接资产的自定义信号与主窗口的槽函数
        dialog.signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()
    
    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())
    
    def deal_emit_slot(self,dateStr):
        self.lineEdit_emit.setText(dateStr)

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())
