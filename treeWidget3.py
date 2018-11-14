from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidget,QTreeWidgetItem,QVBoxLayout,\
QMessageBox,QDirModel,QTreeView
from PyQt5.QtGui import QIcon
import sys


class TreeWidgetDemo(QWidget):

    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)
        self.initUI()
    

    def initUI(self):
        #布局
        layout=QVBoxLayout()
        #windows提供的模式
        model=QDirModel()
        #初始化treewidget
        self.tree=QTreeView()
        self.tree.setModel(model)
        #绑定事件
        self.tree.clicked.connect(self.onTreeClicked)

        #节点全部展开
        self.tree.expandAll()
        self.resize(640,480)
  
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