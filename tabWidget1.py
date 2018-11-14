from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QTabWidget,QFormLayout,QHBoxLayout,QLineEdit,QLabel,QCheckBox,QRadioButton
from PyQt5.QtGui import QIcon
import sys


class tabWidgetDemo(QWidget):

    def __init__(self,parent=None):
        super(tabWidgetDemo,self).__init__(parent)
        self.initUI()
    

    def initUI(self):
        #布局
        layout=QVBoxLayout()
        self.tabWidget=QTabWidget()
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabWidget.addTab(self.tab1,"tab1")
        self.tabWidget.addTab(self.tab2,"tab1")
        self.tabWidget.addTab(self.tab3,"tab1")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        layout.addWidget(self.tabWidget)
        self.setLayout(layout)
    
    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.tabWidget.setTabText(0,"联系方式")
        self.tab1.setLayout(layout)
    
    def tab2UI(self):
        personForm=QFormLayout()
        sexLayout=QHBoxLayout()
        sexLayout.addWidget(QRadioButton("男"))
        sexLayout.addWidget(QRadioButton("女"))
        personForm.addRow(QLabel("性别"),sexLayout)
        personForm.addRow("生日",QLineEdit())
        self.tabWidget.setTabText(1,"个人详情信息")
        self.tab2.setLayout(personForm)
    
    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.tabWidget.setTabText(2,"教育程度")
        self.tab3.setLayout(layout)
        


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=tabWidgetDemo()
    demo.show()
    sys.exit(app.exec_())