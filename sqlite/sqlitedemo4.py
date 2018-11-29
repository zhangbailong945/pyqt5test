import sys,re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery,QSqlQueryModel
from PyQt5.QtCore import Qt


def createTable():
    #添加数据库
    db = QSqlDatabase.addDatabase("QSQLITE")
    #设置数据库名
    db.setDatabaseName('D:/PyQt5Projects/pyqt5test/sqlite/test.db')
    #判断是否打开数据库
    if not db.open():
        return False

    #声明数据库查询对象
    query = QSqlQuery()
    #创建表
    query.exec(
        "create table students(id int primary key,name varchar,sex varchar,age int,deparment varchar);")
    #添加记录
    query.exec("insert into students values(1,'张三','男',20,'计算机')")
    query.exec("insert into students values(2,'张方','男',20,'计算机')")
    query.exec("insert into students values(3,'张小丽','女',20,'计算机')")
    query.exec("insert into students values(1,'李四','男',20,'计算机')")
    query.exec("insert into students values(5,'赵六','男',20,'计算机')")
    query.exec("insert into students values(6,'赵丽颖','女',20,'计算机')")
    query.exec("insert into students values(7,'金汉','男',20,'计算机')")
    query.exec("insert into students values(8,'马超','男',20,'计算机')")
    query.exec("insert into students values(9,'孙尚香','女',20,'计算机')")
    query.exec("insert into students values(10,'关羽','男',20,'计算机')")
    query.exec("insert into students values(11,'小乔','女',20,'计算机')")
    query.exec("insert into students values(12,'大乔','女',20,'计算机')")
    query.exec("insert into students values(13,'刘备','男',20,'计算机')")
    query.exec("insert into students values(14,'李四2','女',19,'经管')")
    query.exec("insert into students values(15,'赵六3','男',21,'英语')")
    query.exec("insert into students values(16,'李四2','男',19,'法律')")
    query.exec("insert into students values(17,'小张2','女',22,'经管')")
    query.exec("insert into students values(18,'李四3','男',21,'英语')")
    query.exec("insert into students values(19,'小李3','女',19,'法律')")
    query.exec("insert into students values(20,'王五3','女',20,'机械')")
    query.exec("insert into students values(21,'张三4','男',22,'计算机')")
    query.exec("insert into students values(22,'小李2','男',20,'法律')")
    query.exec("insert into students values(23,'张三5','男',19,'经管')")
    query.exec("insert into students values(24,'小张3','女',20,'计算机')")
    query.exec("insert into students values(25,'李四4','男',22,'英语')")
    query.exec("insert into students values(26,'赵六2','男',20,'机械')")
    query.exec("insert into students values(27,'小李3','女',19,'英语')")
    query.exec("insert into students values(28,'王五4','男',21,'经管')")

    db.close()
    return True


class DataGrid(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("分页查询例子")
        self.resize(750, 300)

        #查询模型
        self.queryModel = None
        #数据表
        self.tableView = None
        #总页数文本
        self.totalPageLabel = None
        #当前页数文本
        self.currentPageLabel = None
        #转到页数输入框
        self.switchPageLineEdit = None
        #前一页按钮
        self.prevButton = None
        #后一页按钮
        self.nextButton = None
        #跳转页面按钮
        self.switchPageButton = None
        #当前页
        self.currentPage = 0
        #总页数
        self.totalPage=0
        #总记录数
        self.totalRecordCount = 0
        #每页显示记录数
        self.pageRecordCount = 5

        self.initUI()

    def initUI(self):
        #操作水平布局
        operatorLayout = QHBoxLayout()
        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.switchPageButton = QPushButton("Go")
        self.switchPageLineEdit = QLineEdit()
        self.switchPageLineEdit.setFixedWidth(40)
        label1 = QLabel('跳转到')
        label2 = QLabel('页')
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(label1)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(label2)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        #设置表格
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setTableView()

        #主布局 垂直
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tableView)
        self.setLayout(mainLayout)

        #按钮信号与槽函数
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)
    
    def onPrevButtonClick(self):
        limitIndex=(self.currentPage-2)*self.pageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage-=1

    
    def onNextButtonClick(self):
        limitIndex=self.currentPage*self.pageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage+=1
    
    def onSwitchPageButtonClick(self):
        #得到输入的数字
        szText=self.switchPageLineEdit.text()
        pattern=re.compile(r'^[1-9]\d*$')
        match=pattern.match(szText)

        #是否为数字
        if not match:
            QMessageBox.information(self,'提示','请输入数字')
            return
        
        if szText=='':
            QMessageBox.information(self,'提示','请输入跳转页码')
            return
        
        #得到页数
        pageIndex=int(szText)
        if pageIndex>self.totalPage or pageIndex<1:
            QMessageBox.information(self,'提示','没有指定的页面，请重新输入!')
            return
        
        #得到查询行号
        limitIndex=(pageIndex-1)*self.pageRecordCount
        #记录查询
        self.recordQuery(limitIndex)
    
    def setTableView(self):
        
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        #设置数据库名
        self.db.setDatabaseName('D:/PyQt5Projects/pyqt5test/sqlite/test.db')
        #打开数据库
        self.db.open()
        #声明查询对象
        self.queryModel=QSqlQueryModel(self)
        #记录查询
        self.recordQuery(0)
        #设置模型
        self.tableView.setModel(self.queryModel)
        #设置表头
        self.queryModel.setHeaderData(0,Qt.Horizontal,'编号')
        self.queryModel.setHeaderData(1,Qt.Horizontal,'姓名')
        self.queryModel.setHeaderData(2,Qt.Horizontal,'性别')
        self.queryModel.setHeaderData(3,Qt.Horizontal,'年龄')
        self.queryModel.setHeaderData(4,Qt.Horizontal,'院系')
    

    def Table(self,tablename):


        
    def recordQuery(self,limitIndex):
        szQuery=("select * from student limit %d,%d"%(limitIndex,self.pageRecordCount))
        self.queryModel.setQuery(szQuery)

    def closeEvent(self,event):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #createTable()
    demo=DataGrid()
    demo.show()
    sys.exit(app.exec_())
