from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QHBoxLayout,QTableWidgetItem,QHeaderView,QAbstractItemView,\
QComboBox,QPushButton
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys


class TableWidgetDemo1(QWidget):

    def __init__(self,parent=None):
        super(TableWidgetDemo1,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("TableWidget例子")
        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        #设置列
        tableWidget.setColumnCount(4)
        #设置行
        tableWidget.setRowCount(30)

        for i in range(30):
            for j in range(4):
                itemCount='(%d,%d)'%(i,j)
                
                tableWidget.setItem(i,j,QTableWidgetItem(itemCount))
        


        #遍历表格查找对应项
        text="(28,1)"
        items=tableWidget.findItems(text,QtCore.Qt.MatchExactly)
        item=items[0]
        #选中单元格
        item.setSelected(True)
        #设置单元格背景颜色
        item.setForeground(QBrush(QColor(255,0,0)))
        row=item.row()
        #通过鼠标滚轮定位，快速定位到第11行
        tableWidget.verticalScrollBar().setSliderPosition(row)

        #设置排序
        #降序
        tableWidget.sortItems(2,QtCore.Qt.DescendingOrder)

        #升序
        #tableWidget.sortItems(1,QtCore.Qt.AscendingOrder)

        #合并单元格
        #tableWidget.setSpan(1,1,3,2)

        #设置单元格的大小
        tableWidget.setColumnWidth(0,60)
        tableWidget.setRowHeight(0,60)

        #不显示网格
        tableWidget.setShowGrid(False)

        #不需要垂直表头标签
        tableWidget.verticalHeader().setVisible(False)

        #垂直布局加入tableWidget
        layout.addWidget(tableWidget)
        self.resize(600,800)
        self.setLayout(layout




if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=TableWidgetDemo1()
    demo.show()
    sys.exit(app.exec_())