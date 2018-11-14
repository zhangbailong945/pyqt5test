from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidget,QTreeWidgetItem,QVBoxLayout,\
QMessageBox
from PyQt5.QtGui import QIcon
import sys


class TreeWidgetDemo(QWidget):

    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)
        self.initUI()
    

    def initUI(self):
        #布局
        layout=QVBoxLayout()
        #初始化treewidget
        self.tree=QTreeWidget()
        #设置列数
        self.tree.setColumnCount(2)
        #设置头部标签
        self.tree.setHeaderLabels(['key','value'])
        #设置节点
        root=QTreeWidgetItem(self.tree)
        root.setText(0,'root')

        #设置树形控件的宽度
        self.tree.setColumnWidth(0,160)

        rootlist=[]
        rootlist.append(root)

        #设置子节点1
        child1=QTreeWidgetItem()
        child1.setText(0,'手机端')
        child1.setText(1,'ios')
        child1.setIcon(0,QIcon("D:/pyqt5projects/pyqt5test/images/test.ico"))
        root.addChild(child1)

        #设置子节点2
        child2=QTreeWidgetItem()
        child2.setText(0,'手机端')
        child2.setText(1,'andord')
        child2.setIcon(0,QIcon("D:/pyqt5projects/pyqt5test/images/test.ico"))
        root.addChild(child2)
        #设置子节点2-1
        child2_1=QTreeWidgetItem()
        child2_1.setText(0,'手机端')
        child2_1.setText(1,'andord')
        child2_1.setIcon(0,QIcon("D:/pyqt5projects/pyqt5test/images/test.ico"))
        child2.addChild(child2_1)

        #选择
        child2.setCheckState(0,Qt.Checked)

        self.tree.insertTopLevelItems(0,rootlist)



        self.tree.addTopLevelItem(root)

        #绑定事件
        self.tree.clicked.connect(self.onTreeClicked)

        #节点全部展开
        self.tree.expandAll()
        layout.addWidget(self.tree)
        self.setLayout(layout)
    
    def onTreeClicked(self):
        item=self.tree.currentItem()
        QMessageBox.information(self,'提示','内容:'+item.text(1),QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)




if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=TreeWidgetDemo()
    demo.show()
    sys.exit(app.exec_())