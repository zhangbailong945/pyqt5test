from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QHBoxLayout,QTableWidgetItem,QHeaderView,QAbstractItemView,\
QComboBox,QPushButton
from PyQt5.QtGui import *
import sys

class TableWidgetDemo(QWidget):

    def __init__(self,parent=None):
        super(TableWidgetDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("TableWidget例子")
        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        #设置列
        tableWidget.setColumnCount(5)
        #设置行
        tableWidget.setRowCount(4)
        #设置水平表头标签
        h_title_list=['姓名','性别','体重(kg)','年龄','操作']
        tableWidget.setHorizontalHeaderLabels(h_title_list)
        #设置水平表头标签的
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #设置垂直表头标签
        v_title_list=['行1','行2','行3','行4']
        tableWidget.setVerticalHeaderLabels(v_title_list)

        #设置第一行第1列的项目
        item=QTableWidgetItem("张三")
        tableWidget.setItem(0,0,item)

        #设置第一行第2列的项目
        combox_sex=QComboBox()
        combox_sex.addItem("男")
        combox_sex.addItem("女")
        combox_sex.setStyleSheet("QComboBox(margin:3px);")
        tableWidget.setCellWidget(0,1,combox_sex)

        #设置第一行第3列的项目
        item=QTableWidgetItem("160")
        tableWidget.setItem(0,2,item)

        #设置第一行第4列的项目
        item=QTableWidgetItem("25")
        tableWidget.setItem(0,3,item)

        #设置第一行第5列的项目
        btn_add=QPushButton("新增")
        btn_add.setDown(True)
        btn_add.setStyleSheet("QPushButton(marin:3px);")
        tableWidget.setCellWidget(0,4,btn_add)
        

        #禁止表格编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #设置表格整行选中
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #设置行和列的宽度和高度随内容的宽度和高度而定
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        #隐藏水平、垂直表头标签
        #tableWidget.verticalHeader().setVisible(False)
        #tableWidget.horizontalHeader().setVisible(False)


        #垂直布局加入tableWidget
        layout.addWidget(tableWidget)
        self.resize(470,250)
        self.setLayout(layout)



if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=TableWidgetDemo()
    demo.show()
    sys.exit(app.exec_())