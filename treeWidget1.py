from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidget,QTreeWidgetItem,QVBoxLayout
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
        root.setIcon(0,QIcon('./images/test.ico'))
        #设置树形控件的宽度
        self.tree.setColumnWidth(0,160)


        #设置子节点1
        child1=QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'ios')
        child1.setIcon(0,QIcon('./images/test.ico'))

        #设置子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'java')
        child2.setIcon(0,QIcon('./images/test.ico'))

        #设置子节点3
        child3=QTreeWidgetItem(root)
        child3.setText(0,'child3')
        child3.setText(1,'python')
        child3.setIcon(0,QIcon('./images/test.ico'))

        self.tree.addTopLevelItem(root)

        #节点全部展开
        #self.tree.expandAll()
        layout.addWidget(self.tree)
        self.setLayout(layout)



if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=TreeWidgetDemo()
    demo.show()
    sys.exit(app.exec_())