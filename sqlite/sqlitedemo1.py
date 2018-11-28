import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery



def createDB():
    db=QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("F:/PyQtProjects/pyqt5test/sqlite/test.db")

    if not db.open():
        QMessageBox.critical(None,("无法打开数据库"),("无法建立到数据库的连接，这个列子需要SQLite支持，请检测数据库配置。\n\n 单击取消按钮退出应用。"),QMessageBox.Cancel)
        return False
    
    query=QSqlQuery()
    query.exec_("create table address(id int primary key,name varchar(20),address varchar(30))")
    query.exec_("insert into address values(1,'lisi','BeiJing')")
    query.exec_("insert into address values(2,'zhangbai','TianJing')")
    db.close()
    return True


if __name__=='__main__':
    app=QApplication(sys.argv)
    createDB()
    print('success')
    sys.exit(app.exec_())

