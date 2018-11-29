import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery


## SQlite在PyQt5中的使用
# 

class MyWidget(QWidget):

    def __init__(self,parent=None):
        super(MyWidget,self).__init__(parent)
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('F:/PyQtProjects/pyqt5test/sqlite/test.db')
        #打开数据库
        self.db.open()
        self.initUI()
    
    def initUI(self):
        self.resize(400,300)
    
    def closeEvent(self,event):
        #关闭数据库
        self.db.close()


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=MyWidget()
    demo.show()
    sys.exit(app.exec_())

