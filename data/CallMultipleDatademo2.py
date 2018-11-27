from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from multipleDatademo2 import DateDialog
import sys,time

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.resize(400,90)
        self.setWindowTitle('对话框关闭时返回给主窗口的列子')
        self.lineEdit=QLineEdit(self)

        self.btn1=QPushButton('弹出对话框1')
        self.btn1.clicked.connect(self.onBtn1Click)

        self.btn2=QPushButton('弹出对话框2')
        self.btn2.clicked.connect(self.onBtn2Click)

        gridLayout=QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.btn1)
        gridLayout.addWidget(self.btn2)
        self.setLayout(gridLayout)

    def onBtn1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec_()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n 1日期对话框的返回值')
        print('date=%s'% str(date.date()))
        print('time=%s'% str(date.time()))
        print('result=%s'% result)
        dialog.destroy()
    
    def onBtn2Click(self):
        date,time,result=DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n 2日志对话框的返回值')
        print('date=%s'% str(date))
        print('time=%s'% str(time))
        print('result=%s'% result)


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())


